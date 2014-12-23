'''
###  WARNING !!!!!!!
###  This is where common code for BigChain will go in.
###
###  To commit new code, please contact the Library Owner:
###  Animesh Patcha (animesh.patcha@bigswitch.com)
###
###  DO NOT COMMIT CODE WITHOUT APPROVAL FROM LIBRARY OWNER
###
###  Last Updated: 12/22/2014
###
###  WARNING !!!!!!!
'''
import autobot.helpers as helpers
import autobot.test as test
import keywords.AppController as AppController
# import json
# import re

class BigChain(object):

    def __init__(self):
        pass

###################################################
# All BigChain CLI Commands Go Here:
###################################################

###################################################
# All BigChain REST Commands Go Here:
###################################################
###################################################
##### SHOW COMMANDS
###################################################

    def rest_verify_switch_mode_show(self, node, mode='bigchain', switch_alias=None, sw_dpid=None):
        '''
            Objective:
                -- Verify a switch role via command "show switch <switch_alias>"
        '''
        try:
            t = test.Test()
            c = t.controller('master')
            AppCommon = AppController.AppController()
            if (switch_alias is None and sw_dpid is not None):
                switch_dpid = sw_dpid
            elif (switch_alias is None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_ip(node)
            elif (switch_alias is not None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_alias(switch_alias)
            else:
                switch_dpid = sw_dpid
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            url = '/api/v1/data/controller/core/switch[dpid="%s"]' % str(switch_dpid)
            c.rest.get(url)
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())
            content = c.rest.content()
            if (content[0]['pipeline-mode']) == str(mode):
                helpers.log("Switch Mode %s is reported correctly" % str(mode))
                return True
            else:
                helpers.log("Switch Mode %s is not reported correctly" % str(mode))
                return False

    def rest_verify_switch_mode_config(self, node, mode='bigchain', switch_alias=None, sw_dpid=None):
        '''
            Objective:
                -- Verify a switch role via command "show running-config"
        '''
        try:
            t = test.Test()
            c = t.controller('master')
            AppCommon = AppController.AppController()
            if (switch_alias is None and sw_dpid is not None):
                switch_dpid = sw_dpid
            elif (switch_alias is None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_ip(node)
            elif (switch_alias is not None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_alias(switch_alias)
            else:
                switch_dpid = sw_dpid
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            url = '/api/v1/data/controller/applications/bigtap/switch-config?config=true'
            c.rest.get(url)
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())
            content = c.rest.content()
            for switch in content:
                if switch['switch'] == str(switch_dpid) and switch['role'] == str(mode):
                    return True
            return False

    def rest_show_bigchain(self, desired_output="state"):
        '''
            Objective:
                -- Return desired value after executing cli command "show bigchain"
        '''
        try:
            t = test.Test()
            c = t.controller('master')
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            url = '/api/v1/data/controller/applications/bigchain/info'
            c.rest.get(url)
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())
            content = c.rest.content()
            if desired_output is "max-delivery-bandwidth":
                return content['max-delivery-bandwidth-bps']
            elif desired_output is "max-filter-bandwidth":
                return content['max-filter-bandwidth-bps']
            elif desired_output is "post-service":
                return content['max-post-service-bandwidth-bps']
            elif desired_output is "pre-service":
                return content['max-pre-service-bandwidth-bps']
            elif desired_output is "active-chain-count":
                return content['num-active-chains']
            elif desired_output is "chain-count":
                return content['num-chains']
            elif desired_output is "service-count":
                return content['num-services']
            elif desired_output is "switch-count":
                return content['num-total-switches']
            elif desired_output is "total-delivery-traffic":
                return content['total-delivery-traffic-bps']
            elif desired_output is "total-filter-traffic":
                return content['total-filter-traffic-bps']
            elif desired_output is "total-post-service-traffic":
                return content['total-post-service-traffic-bps']
            elif desired_output is "total-pre-service-traffic":
                return content['total-pre-service-traffic-bps']
            elif desired_output is "uptime":
                return content['uptime']
            else:
                return content['state']

    def rest_show_bigchain_chain(self, chain_name, desired_output):
        '''
            Objective:
                -- Return desired value after executing cli command "show bigchain chain"       
        '''
        try:
            t = test.Test()
            c = t.controller('master')
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            url = '/api/v1/data/controller/applications/bigchain/chain[name="%s"]?select=status' % str(chain_name)
            c.rest.get(url)
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())
            content = c.rest.content()
            if desired_output is "name":
                return content[0]['name']
            elif desired_output is "detailed-status":
                return content[0]['status']['detailed-status']
            elif desired_output is "from":
                return content[0]['status']['from']
            elif desired_output is "from-drop":
                return content[0]['status']['from-drop']
            elif desired_output is "name-in-status":
                return content[0]['status']['name']
            elif desired_output is "runtime-status":
                return content[0]['status']['runtime-status']
            elif desired_output is "services":
                return content[0]['status']['services']
            elif desired_output is "switch":
                return content[0]['status']['switch']
            elif desired_output is "to":
                return content[0]['status']['to']
            elif desired_output is "to-drop":
                return content[0]['status']['to-drop']
            else:
                helpers.test_log("Requested object does not exist")
                return False

    def rest_verify_bigchain_chain(self, node, chain_name=None, interface1=None, interface2=None, switch_alias=None, sw_dpid=None, service1=None, service2=None, service3=None, service4=None):
        '''
            Objective:
                -- Verify cli command "show bigchain chain <chain_name>"     
        '''
        try:
            t = test.Test()
            c = t.controller('master')
            AppCommon = AppController.AppController()
            if (switch_alias is None and sw_dpid is not None):
                switch_dpid = sw_dpid
            elif (switch_alias is None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_ip(node)
            elif (switch_alias is not None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_alias(switch_alias)
            else:
                switch_dpid = sw_dpid
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            if((chain_name is None)  or (interface1 is None) or (interface2 is None)) :
                helpers.log("FAIL: Cannot add a endpoint pair without specifying a chain name or endpoint interfaces")
                return False
            else:
                url = '/api/v1/data/controller/applications/bigchain/chain[name="%s"]' % str(chain_name)
                c.rest.get(url)
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                content = c.rest.content()
                pass_count = 0
                if content[0]['name'] == str(chain_name) :
                    helpers.log("Chain Name %s is reported correctly" % str(chain_name))
                else:
                    helpers.log("Chain Name %s is not reported correctly" % str(chain_name))
                    return False

                if (content[0]['status']['from'] == str(interface1)) :
                    helpers.log("Interface %s is reported correctly" % str(interface1))
                else:
                    helpers.log("Interface %s is not reported correctly" % str(interface1))
                    return False

                if (content[0]['status']['to'] == str(interface2)) :
                    pass_count = pass_count + 1
                    helpers.log("Interface %s is reported correctly" % str(interface2))
                else:
                    helpers.log("Interface %s is not reported correctly" % str(interface2))
                    return False

                if (content[0]['status']['switch'] == str(switch_dpid)) :
                    pass_count = pass_count + 1
                    helpers.log("Switch DPID %s is reported correctly" % str(switch_dpid))
                else:
                    helpers.log("Switch DPID %s is not reported correctly" % str(switch_dpid))
                    return False
                if service1 is not None and service2 is None:
                    if (content[0]['status']['services'] == str(service1)):
                        helpers.log("Service %s is reported correctly" % str(service1))
                    else:
                        helpers.log("Service %s is not reported correctly" % str(service1))
                        return False
                else:
                    temp = content[0]['status']['services']
                    temp_array = temp.split(',')
                    if temp_array[3] == str(service1):
                        helpers.log("Service %s is reported correctly" % str(service1))
                    else:
                        helpers.log("Service %s is not reported correctly" % str(service1))
                        return False
                    if service2 is not None :
                        if temp_array[2] == str(service2):
                            helpers.log("Service %s is reported correctly" % str(service2))
                        else:
                            helpers.log("Service %s is not reported correctly" % str(service2))
                            return False
                    if service3 is not None:
                        if temp_array[1] == str(service3):
                            helpers.log("Service %s is reported correctly" % str(service3))
                        else:
                            helpers.log("Service %s is not reported correctly" % str(service3))
                            return False
                    if service4 is not None:
                        if temp_array[0] == str(service4):
                            helpers.log("Service %s is reported correctly" % str(service4))
                        else:
                            helpers.log("Service %s is not reported correctly" % str(service4))
                            return False
                return True

    def rest_verify_bichain_chain_config(self, node, chain_name=None, endpoint1=None, endpoint2=None, switch_alias=None, sw_dpid=None):
        '''
            Objective:
                -- Verify a bigchain chain configuration role via command "show running-config bigchain chain <chain_name>"
        '''
        try:
            t = test.Test()
            c = t.controller('master')
            AppCommon = AppController.AppController()
            if (switch_alias is None and sw_dpid is not None):
                switch_dpid = sw_dpid
            elif (switch_alias is None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_ip(node)
            elif (switch_alias is not None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_alias(switch_alias)
            else:
                switch_dpid = sw_dpid
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            url = '/api/v1/data/controller/applications/bigchain/chain[name="%s"]?config=true' % str(chain_name)
            c.rest.get(url)
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())
            content = c.rest.content()
            if content[0]['name'] == str(chain_name) :
                helpers.log("Chain Name %s is reported correctly" % str(chain_name))
            else:
                helpers.log("Chain Name %s is not reported correctly" % str(chain_name))
                return False
            if content[0]['endpoint-pair']['from'] == str(endpoint1) :
                helpers.log("End Point 1 %s is reported correctly" % str(endpoint1))
            else:
                helpers.log("End Point 1 %s is not reported correctly" % str(endpoint1))
                return False
            if content[0]['endpoint-pair']['to'] == str(endpoint2) :
                helpers.log("End Point 2 %s is reported correctly" % str(endpoint2))
            else:
                helpers.log("End Point 2 %s is not reported correctly" % str(endpoint2))
                return False
            if content[0]['endpoint-pair']['switch'] == str(switch_dpid) :
                helpers.log("Switch DPID  %s is reported correctly" % str(switch_dpid))
            else:
                helpers.log("Switch DPID %s is not reported correctly" % str(switch_dpid))
                return False
            return True

###################################################
##### CONFIG COMMANDS
###################################################

    def rest_add_switch_role(self, node, switch_alias=None, sw_dpid=None, mode='bigchain'):
        '''
            Objective:
                -- Add a switch role via command "deployment role <mode>"
        '''
        try:
            t = test.Test()
            c = t.controller('master')
            AppCommon = AppController.AppController()
            if (switch_alias is None and sw_dpid is not None):
                switch_dpid = sw_dpid
            elif (switch_alias is None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_ip(node)
            elif (switch_alias is not None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_alias(switch_alias)
            else:
                switch_dpid = sw_dpid
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            url = '/api/v1/data/controller/applications/bigtap/switch-config[switch="%s"]' % str(switch_dpid)
            try:
                c.rest.put(url, {"switch": str(switch_dpid), "role": str(mode)})
            except:
                helpers.test_log(c.rest.error())
                return False
            else:
                return True

    def rest_add_a_chain(self, chain_name=None):
        '''
            Objective:
                -- Add a chain via command "bigchain chain <chain_name>"       
        '''
        try:
            t = test.Test()
            c = t.controller('master')
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            if chain_name is None:
                helpers.log("FAIL: Cannot add a chain without specifying a name")
                return False
            else:
                url = '/api/v1/data/controller/applications/bigchain/chain[name="%s"]' % str(chain_name)
                try:
                    c.rest.put(url, {'name':str(chain_name)})
                except:
                    helpers.test_log(c.rest.error())
                    return False
                else:
                    return True

    def rest_add_chain_endpoint(self, node, chain_name=None, interface1=None, interface2=None, switch_alias=None, sw_dpid=None):
        '''
            Objective:
                -- Add an endpoint to a chain via command "endpoint-pair switch app-as5710-1 endpoint1 ethernet21 endpoint2 ethernet22"       
        '''
        try:
            t = test.Test()
            c = t.controller('master')
            AppCommon = AppController.AppController()
            if (switch_alias is None and sw_dpid is not None):
                switch_dpid = sw_dpid
            elif (switch_alias is None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_ip(node)
            elif (switch_alias is not None and sw_dpid is None):
                switch_dpid = AppCommon.rest_return_switch_dpid_from_alias(switch_alias)
            else:
                switch_dpid = sw_dpid
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            if((chain_name is None)  or (interface1 is None) or (interface2 is None)) :
                helpers.log("FAIL: Cannot add a endpoint pair without specifying a chain name or endpoint interfaces")
                return False
            else:
                url = '/api/v1/data/controller/applications/bigchain/chain[name="%s"]/endpoint-pair' % str(chain_name)
                try:
                    c.rest.patch(url, {"to": str(interface2), "switch": str(switch_dpid), "from": str(interface1)})
                except:
                    helpers.test_log(c.rest.error())
                    return False
                else:
                    return True

    def rest_add_service_to_chain(self, chain_name=None, service_name=None, instance=1, sequence=1):
        '''
            Objective:
                -- Add a service to a chain via command "use-service C1S1 instance 1 sequence 1"
       '''
        try:
            t = test.Test()
            c = t.controller('master')
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            if((chain_name is None)  or (service_name is None)) :
                helpers.log("FAIL: Cannot add a endpoint pair without specifying a chain name or endpoint interfaces")
                return False
            else:
                url = '/api/v1/data/controller/applications/bigchain/chain[name="%s"]/service[sequence=%s]' % (str(chain_name), str(sequence))
                try:
                    c.rest.put(url, {"service-name": str(service_name), "instance": int(instance), "sequence": int(sequence)})
                except:
                    helpers.test_log(c.rest.error())
                    return False
                else:
                    return True
    def rest_delete_bigchain_chain(self, chain_name=None):
        '''
            Objective:
                -- Delete a chain via command "no bigchain chain <chain_name>"       
        '''
        try:
            t = test.Test()
            c = t.controller('master')
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:
            if chain_name is None:
                helpers.log("FAIL: Cannot delete a chain without specifying a chain name")
                return False
            else:
                url = '/api/v1/data/controller/applications/bigchain/chain[name="%s"]' % str(chain_name)
                try:
                    c.rest.delete(url, {})
                except:
                    helpers.test_log(c.rest.error())
                    return False
                else:
                    return True
