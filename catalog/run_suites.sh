#!/bin/sh -x
# Usage:
#   $ cd .../bigrobot/catalog
#   $ ./run_suites.sh dump_suites_by_areas.sh.T5.text_files
# Description:
#   Take an input file which contains a list of test suites (with full path).
#   Then execute Gobot dryrun against these files to produce the Robot data
#   file (output.xml).
# Assumptions:
#   - This script can only be executed inside the bigrobot/catalog/ directory.

usage() {
    echo "Usage: $0 <input_file>"
    exit 0
}

if [ ! -x ../bin/gobot ]; then
    echo "Error: This script must be executed in the bigrobot/catalog/ directory."
    exit 1
fi

if [ $# -ne 1 ]; then
    usage
fi

f=$1

if [ ! -f $f ]; then
    echo "Error: File '$f' is not found."
    exit 1
fi

unset BIGROBOT_TESTBED
unset BIGROBOT_PARAMS_INPUT
export BIGROBOT_CI=True
if [ "$BIGROBOT_PATH"x = x ]; then
    export BIGROBOT_PATH=`pwd`/..
fi
export BIGROBOT_LOG_PATH=${BIGROBOT_PATH}/catalog/bigrobot_logs

rm -rf $BIGROBOT_LOG_PATH
for x in `cat $f`; do
    echo Running $x
    y=`echo $x | sed 's/.txt//'`

    ls -la ${y}*

    # Notes:
    #   We need to count the test cases which are tagged as 'manual-untested'
    #   as well.
    BIGROBOT_SUITE=$y ../bin/gobot test --dryrun --include-manual-untested
done

find $BIGROBOT_LOG_PATH -name output.xml > $f.dryrun.output_xml.log
