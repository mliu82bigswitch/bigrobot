#!/usr/bin/env python
"""
"""

import os
import sys
import re
import xmltodict
import argparse
import robot
from pymongo import MongoClient


# Determine BigRobot path(s) based on this executable (which resides in
# the bin/ directory.
bigrobot_path = os.path.dirname(__file__) + '/..'
exscript_path = bigrobot_path + '/vendors/exscript/src'

sys.path.insert(0, bigrobot_path)
sys.path.insert(1, exscript_path)

import autobot.helpers as helpers
# import autobot.devconf as devconf

helpers.set_env('IS_GOBOT', 'False')
helpers.set_env('AUTOBOT_LOG', './myrobot.log')

DB_SERVER = 'qadashboard-mongo.bigswitch.com'
DB_PORT = 27017

# Normalize the Git authors. Map them to their LDAP names.
AUTHORS = {
           "SureshVoora": "suresh",
           "prashanth": "padubiry",
           "amallina": "arunamallina",
           "Vui Le": "vui",
           "Animesh Patcha": "animesh",
           "songbeng": "slim",
           "tomaszklimczyk": "tomasz",
           "Tomasz Klimczyk": "tomasz",
           "Mingtao Yang": "mingtao",
           "Don Jayakody": "don",
           "Cliff DeGuzman": "cliff",
           "kranti": "kranti",
           "William Tan": "wtan",
           "fc7737": "wtan",
           "Sakshi Kalra": "sakshikalra",
           }

def format_robot_timestamp(ts, is_datestamp=False):
    """
    Robot Framework uses the following timestamp format:
        20140523 16:49:38.051
    Concert it to UTC ISO time format:
        2014-05-23T23:49:38.051Z
    """
    match = re.match(r'(\d{4})(\d{2})(\d{2})\s+(\d+):(\d+):(\d+)\.(\d+)$', ts)
    if not match:
        helpers.environment_failure("Incorrect time format: '%s'" % ts)
    (year, month, date, hour, minute, sec, msec) = match.groups()
    hour = int(hour) + 7  # change PST to UTC
    if is_datestamp:
        s = '%s-%s-%s' % (year, month, date)
    else:
        s = '%s-%s-%sT%s:%s:%s.%sZ' % (year, month, date,
                                       hour, minute, sec, msec)
    return s


def format_robot_datestamp(ts):
    return format_robot_timestamp(ts, is_datestamp=True)


class TestSuite(object):
    def __init__(self, filename, is_regression=False):
        """
        filename: output.xml file (with path)
        """
        self._suite = {}
        self._tests = []
        self._total_tests = 0
        self._filename = filename
        self._db = None

        self._is_regression = is_regression

        client = MongoClient(DB_SERVER, DB_PORT)
        self._db = client.test_catalog2

        # Remove first line: <?xml version="1.0" encoding="UTF-8"?>
        self.xml_str = ''.join(helpers.file_read_once(self._filename,
                                                      to_list=True)[1:])

        self._data = xmltodict.parse(self.xml_str)

    def db(self):
        return self._db

    def db_count_testcases(self):
        testcases = self.db().test_cases
        count = testcases.count()
        return count

    def db_insert_testcase_archive(self, rec):
        testcases = self.db().test_cases_archive
        tc = testcases.insert(rec)

        # Side effect of insert operation is that it will insert the ObjectID
        # into rec, which may cause subsequent operations to fail (e.g.,
        # to_json(). So we remove the ObjectID.
        del rec['_id']
        return tc

    def db_insert_testcase(self, rec):
        testcases = self.db().test_cases
        tc = testcases.insert(rec)

        # Side effect of insert operation is that it will insert the ObjectID
        # into rec, which may cause subsequent operations to fail (e.g.,
        # to_json(). So we remove the ObjectID.
        del rec['_id']
        return tc

    def db_insert_suite(self, rec):
        suites = self.db().test_suites
        suite = suites.insert(rec)

        # Side effect of insert operation is that it will insert the ObjectID
        # into rec, which may cause subsequent operations to fail (e.g.,
        # to_json(). So we remove the ObjectID.
        del rec['_id']
        return suite

    def db_find_and_modify_regression_testcase(self, rec):
        testcases = self.db().test_cases_archive

        tc = testcases.find_and_modify(
                query={ "name": rec['name'],
                        "product_suite" : rec['product_suite'],
                        "build_name": rec['build_name'] },
                        # "build_number": rec['build_number'] },
                        # "starttime_datestamp" : rec['starttime_datestamp'],
                update={ "$set": rec },  # update entire record
                upsert=True
                )
        if tc:
            print('Successfully updated Regression "test_cases_archive" record'
                  ' (name:"%s", product_suite:"%s", date:"%s", status:"%s")'
                  % (rec['name'], rec['product_suite'],
                     rec['starttime_datestamp'], rec['status']))
        else:
            print('Did not find Regression "test_cases_archive" record'
                  ' (name:"%s", product_suite:"%s", date:"%s")'
                  % (rec['name'], rec['product_suite'],
                     rec['starttime_datestamp']))

    def db_find_and_modify_testcase(self, rec):
        testcases = self.db().test_cases

        tc = testcases.find_and_modify(
                query={ "name": rec['name'],
                        "product_suite" : rec['product_suite'],
                        },
                update={ "$set": rec },
                # upsert=True
                )
        if tc:
            print('Successfully updated "test_cases" record'
                  ' (name:"%s", product_suite:"%s", date:"%s", status:"%s")'
                  % (rec['name'], rec['product_suite'],
                     rec['starttime_datestamp'], rec['status']))
        else:
            print('CRITICAL ERROR: Did not find "test_cases" record'
                  ' (name:"%s", product_suite:"%s", date:"%s")'
                  % (rec['name'], rec['product_suite'],
                     rec['starttime_datestamp']))

    def db_add_if_not_found_suite(self, rec):
        suites = self.db().test_suites

        suite = suites.find_one({ "product_suite" : rec['product_suite'] })
        if suite:
            print('Found suite record (name:"%s", product_suite:"%s").'
                  ' Skipping insertion.'
                  % (rec['name'], rec['product_suite']))
        else:
            print('Did not find suite record (name:"%s", product_suite:"%s").'
                  ' Inserting new record.'
                  % (rec['name'], rec['product_suite']))
            self.db_insert_suite(rec)

    def db_add_if_not_found_testcase(self, rec):
        testcases = self.db().test_cases

        tc = testcases.find_one({ "name": rec['name'],
                                  "product_suite" : rec['product_suite'], })
        if tc:
            print('Found test case record (name:"%s", product_suite:"%s").'
                  ' Skipping insertion.'
                  % (rec['name'], rec['product_suite']))
        else:
            print('Did not find test case record'
                  ' (name:"%s", product_suite:"%s"). Inserting new record.'
                  % (rec['name'], rec['product_suite']))
            self.db_insert_testcase(rec)

    def data(self):
        """
        Handle to the XML data from input file (output.xml).
        """
        if 'robot' not in self._data:
            helpers.environment_failure(
                    "Fatal error: expecting data['robot']")
        if 'suite' not in self._data['robot']:
            helpers.environment_failure(
                    "Fatal error: expecting data['robot']['suite']")
        if 'test' not in self._data['robot']['suite']:
            helpers.environment_failure(
                    "Fatal error: expecting data['robot']['suite']['test']")
        return self._data

    def git_auth(self, filename):
        filename = re.sub(r'.*bigrobot/', '../', filename)
        (_, output) = helpers.run_cmd("./git-auth " + filename, shell=False)
        output = output.strip()
        if output in AUTHORS:
            return AUTHORS[output]
        else:
            helpers.environment_failure(
                    "AUTHORS dictionary does not contain '%s'" % output)

    def check_topo_type(self, suite):
        """
        Give the 'suite' input which is the path to a suite file (minus the
        '.txt' extension). Check whether it has <suite>.virtual.topo or
        <suite>.physical.topo.

        Return value:
          'virtual'
          'physical'
          'unknown'  - neither virtual nor physical
        """
        if helpers.file_exists(suite + ".virtual.topo"):
            return "virtual"
        if helpers.file_exists(suite + ".physical.topo"):
            return "physical"
        return "unknown"

    def extract_suite_attributes(self):
        suite = self.data()['robot']['suite']
        timestamp = format_robot_timestamp(self.data()['robot']['@generated'])
        datestamp = format_robot_datestamp(self.data()['robot']['@generated'])
        source = source_file = helpers.utf8(suite['@source'])
        match = re.match(r'.+bigrobot/(\w+/([\w-]+)/.+)$', source)
        if match:
            source = "bigrobot/" + match.group(1)
            github_link = ('https://github.com/bigswitch/bigrobot/blob/master/'
                           + match.group(1))
            product = match.group(2)
        else:
            helpers.environment_failure(
                "Fatal error: Source file has invalid format ('%s')" % source)
        author = self.git_auth(source)
        name_actual = os.path.splitext(os.path.basename(source))[0]
        product_suite = os.path.splitext(source)[0]
        product_suite = re.sub(r'.*bigrobot/testsuites/', '', product_suite)
        topo_type = self.check_topo_type(os.path.splitext(source_file)[0])

        self._suite = {
                    'source': source,
                    'timestamp': helpers.utf8(timestamp),
                    'datestamp': helpers.utf8(datestamp),
                    'github_link': github_link,
                    'name_actual': name_actual,
                    'name': helpers.utf8(suite['@name']),
                    'product': product,
                    'product_suite': product_suite,
                    'author': author,
                    'total_tests': None,
                    'topo_type': topo_type,
                    'notes': None,
                    }
        if self._is_regression:
            pass
        else:
            # Baselining
            self.db_add_if_not_found_suite(self._suite)


    def extract_test_attributes(self):
        tests = self.data()['robot']['suite']['test']

        if not helpers.is_list(tests):
            # In a suite with only a single test case, convert into list
            tests = [tests]

        if self._is_regression:
            helpers.debug("DB testcase count (BEFORE): %s"
                          % self.db_count_testcases())

        for a_test in tests:
            # print "['@id']: " + '@id'
            # print "a_test['@id']: " + a_test['@id']
            # print "*** a_test: %s" % a_test
            test_id = helpers.utf8(a_test['@id'])
            name = helpers.utf8(a_test['@name'])
            if (('tags' in a_test and a_test['tags'] != None)
                and 'tag' in a_test['tags']):
                tags = helpers.utf8(a_test['tags']['tag'])

                # Normalize data - convert tags to lowercase
                tags = [x.lower() for x in tags]
            else:
                tags = []

            if self._is_regression:
                # Analyzing regression results which should have PASS/FAIL
                # status.
                status = helpers.utf8(a_test['status']['@status'])
                starttime = format_robot_timestamp(
                                helpers.utf8(a_test['status']['@starttime']))
                starttime_datestamp = format_robot_datestamp(
                                helpers.utf8(a_test['status']['@starttime']))
                endtime = format_robot_timestamp(
                                helpers.utf8(a_test['status']['@endtime']))
                endtime_datestamp = format_robot_datestamp(
                                helpers.utf8(a_test['status']['@endtime']))
                executed = True
            else:
                status = starttime = endtime = endtime_datestamp = None
                executed = False
                starttime_datestamp = self._suite['datestamp']
                # starttime_datestamp = '2014-05-28'

            # This should contain the complete list of attributes. Some may
            # be populated by the Script Catalog while others may be populated
            # later by Regression execution.
            test = {'test_id': test_id,
                    'name': name,
                    'tags': tags,
                    'executed': executed,
                    'status': status,
                    'starttime': starttime,
                    'starttime_datestamp': starttime_datestamp,
                    'endtime': endtime,
                    'endtime_datestamp': endtime_datestamp,
                    'duration': None,
                    'origin_script_catalog': not self._is_regression,
                    'origin_regression_catalog': self._is_regression,
                    'product_suite': self._suite['product_suite'],
                    'build_number': None,
                    'build_url': None,
                    'build_name': None,
                    'notes': None,
                    }

            if self._is_regression:
                if 'BUILD_NUMBER' in os.environ:
                    test['build_number'] = os.environ['BUILD_NUMBER']
                if 'BUILD_URL' in os.environ:
                    test['build_url'] = os.environ['BUILD_URL']
                if 'BUILD_NAME' in os.environ:
                    test['build_name'] = os.environ['BUILD_NAME']
                self.db_find_and_modify_testcase(test)
                self.db_find_and_modify_regression_testcase(test)
                # self.db_insert_testcase_archive(test)
            else:
                # Baselining
                self.db_add_if_not_found_testcase(test)

            self._tests.append(test)

            # Add test cases to test suite
            # self._suite['tests'] = self._tests
        if self._is_regression:
            helpers.debug("DB testcase count (AFTER): %s"
                          % self.db_count_testcases())
        self.total_tests()

    def suite_name(self):
        return self._suite['name']

    def suite(self):
        return self._suite

    def tests(self):
        return self._tests

    def total_tests(self):
        self._suite['total_tests'] = len(self.tests())
        return self._suite['total_tests']

    def dump_suite(self, to_file=None, to_json=False):
        if to_json:
            if to_file:
                helpers.file_write_append_once(to_file,
                                               helpers.to_json(self.suite())
                                               + '\n')
            else:
                print(helpers.to_json(self.suite()))
        else:
            if to_file:
                helpers.file_write_append_once(to_file,
                                               helpers.prettify(self.suite())
                                               + '\n')
            else:
                print(helpers.prettify(self.suite()))

    def dump_suite_to_file(self, filename, to_json=False):
        self.dump_suite(filename, to_json)

    def dump_tests(self, to_file=None, to_json=False):
        if to_json:
            if to_file:
                helpers.log("Writing to file '%s'" % to_file)
                helpers.file_write_append_once(to_file,
                                               helpers.to_json(self.tests())
                                               + '\n')
            else:
                print(helpers.to_json(self.tests()))
        else:
            if to_file:
                helpers.log("Writing to file '%s'" % to_file)
                helpers.file_write_append_once(to_file,
                                               helpers.prettify(self.tests())
                                               + '\n')
            else:
                print(helpers.prettify(self.tests()))

    def dump_tests_to_file(self, filename, to_json=False):
        self.dump_tests(filename, to_json)

    def dump_raw(self):
        print(helpers.prettify(self.data()))

    def dump_xml(self):
        print("%s" % helpers.prettify_xml(self.xml_str))


class TestCatalog(object):
    def __init__(self, in_files, out_suites, out_testcases,
                 is_regression=False):
        self._suites = []
        self._input_files = in_files
        self._output_suites = out_suites
        self._output_testcases = out_testcases
        self._is_regression = is_regression

    def load_suites(self):
        for filename in self._input_files:
            filename = filename.strip()

            if helpers.file_not_empty(filename):
                print("Reading %s" % filename)
                suite = TestSuite(filename, is_regression=self._is_regression)
                suite.extract_suite_attributes()
                suite.extract_test_attributes()
                suite.dump_suite_to_file(self._output_suites, to_json=True)
                suite.dump_tests_to_file(self._output_testcases, to_json=True)
                self._suites.append(suite)

    def suites(self):
        return self._suites

    def total_suites(self):
        return len(self.suites())

    def total_tests(self):
        tests = 0
        i = 0
        for suite in self.suites():
            i += 1
            tests += suite.total_tests()
            print "Suite %02d: %s (%s tests)" % (i,
                                                 suite.suite_name(),
                                                 suite.total_tests())
        return tests

if __name__ == '__main__':

    descr = """\
Parse the Robot output.xml files to generate the collections for the
Test Catalog (MongoDB) database.
"""
    parser = argparse.ArgumentParser(prog='parse_test_xml_output',
                                     description=descr)
    parser.add_argument('--input', required=True,
                        help=("Contains a list of Robot output.xml files"
                              "  with complete pathnames"))
    parser.add_argument('--output-suites', required=True,
                        help=("JSON output file containing test suites"))
    parser.add_argument('--output-testcases', required=True,
                        help=("JSON output file containing test cases"))
    parser.add_argument('--is-regression',
                        action='store_true', default=False,
                        help=("Specify this option if analyzing regression results"))
    args = parser.parse_args()

    input_files = helpers.file_read_once(args.input, to_list=True)
    t = TestCatalog(in_files=input_files,
                    out_suites=args.output_suites,
                    out_testcases=args.output_testcases,
                    is_regression=args.is_regression)
    t.load_suites()
    print "Total suites: %s" % t.total_suites()
    print "Total tests: %s" % t.total_tests()
