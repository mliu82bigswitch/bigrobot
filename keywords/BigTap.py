''' 
###  WARNING !!!!!!!
###  This is where common code for BigTap will go in.
###  WARNING !!!!!!!
###  To commit new code, please contact the Library Owner: 
###  Animesh Patcha (animesh.patcha@bigswitch.com)
###  WARNING !!!!!!!
###  DO NOT COMMIT CODE WITHOUT APPROVAL FROM LIBRARY OWNER
###  WARNING !!!!!!!
'''

import autobot.helpers as helpers
import autobot.test as test

class BigTap(object):
    
    def __init__(self):
        pass

###################################################
# All Bigtap Show Commands Go Here:
###################################################
    def rest_show_bigtap_policy(self, policy_name,num_filter_intf,num_delivery_intf):
        '''
        Objective:
        Parse the output of cli command 'show bigtap policy <policy_name>'
              
        Inputs:
        | `policy_name` | Name of the policy being parsed | 
        | `num_filter_intf` | Number of configured Filter Interfaces in the policy | 
        | `num_delivery_intf` | Number of configured Delivery Interfaces in the policy | 
        
        Description:
        The function executes a REST GET for http://<CONTROLLER_IP>:8082/api/v1/data/controller/applications/bigtap/view/policy[name="<POLICY_NAME>"]/info
        The policy returns True if and only if all the following conditions are True 
        - Policy name is seen correctly in the output
        - Config-Status is either "active and forwarding" or "active and rate measure"
        - Type is "Configured"
        - Runtime Status is "installed"
        - Delivery interface count is num_delivery_intf
        - Filter Interface count is num_filter_intf
        - Detailed status is either "installed to forward" or "installed to measure rate"        
        
        Return value: 
        - True on success
        - False otherwise
        '''
        try:
            t = test.Test()
            c= t.controller('master')
            url ='/api/v1/data/controller/applications/bigtap/view/policy[name="%s"]/info' % (policy_name)
            c.rest.get(url)
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())
            content = c.rest.content()
        except:
            helpers.test_failure("Could not execute command")
            return False
        else:      
            if content[0]['name'] == str(policy_name):
                    helpers.test_log("Policy correctly reports policy name as : %s" % content[0]['name'])
            else:
                    helpers.test_failure("Policy does not correctly report policy name  : %s" % content[0]['name'])                
                    return False
                  
            if content[0]['config-status'] == "active and forwarding":
                    helpers.test_log("Policy correctly reports config status as : %s" % content[0]['config-status'])
            elif content[0]['config-status'] == "active and rate measure":
                    helpers.test_log("Policy correctly reports config status as : %s" % content[0]['config-status'])          
            else:
                    helpers.test_failure("Policy does not correctly report config status as : %s" % content[0]['config-status'])
                    return False
                  
            if content[0]['type'] == "Configured":
                    helpers.test_log("Policy correctly reports type as : %s" % content[0]['type'])         
            else:
                    helpers.test_failure("Policy does not correctly report type as : %s" % content[0]['type'])
                    return False
                  
            if content[0]['runtime-status'] == "installed":
                    helpers.test_log("Policy correctly reports runtime status as : %s" % content[0]['runtime-status'])         
            else:
                    helpers.test_failure("Policy does not correctly report runtime status as : %s" % content[0]['runtime-status'])
                    return False
                
            if content[0]['delivery-interface-count'] == int(num_delivery_intf) :
                    helpers.test_log("Policy correctly reports number of delivery interfaces as : %s" % content[0]['delivery-interface-count'])
            else:
                    helpers.test_failure("Policy does not correctly report number of delivery interfaces  : %s" % content[0]['delivery-interface-count'])                
                    return False
                          
            if content[0]['filter-interface-count'] == int(num_filter_intf):
                    helpers.test_log("Policy correctly reports number of filter interfaces as : %s" % content[0]['filter-interface-count'])
            else:
                    helpers.test_failure("Policy does not correctly report number of filter interfaces  : %s" % content[0]['filter-interface-count'])                
                    return False
                
            if content[0]['detailed-status'] == "installed to forward":
                    helpers.test_log("Policy correctly reports detailed status as : %s" % content[0]['detailed-status'])
            elif content[0]['detailed-status'] == "installed to measure rate":
                    helpers.test_log("Policy correctly reports detailed status as : %s" % content[0]['detailed-status'])
            else:
                    helpers.test_failure("Policy does not correctly report detailed status as : %s" % content[0]['detailed-status'])
                    return False
            return True

    def rest_show_switch_dpid(self,switch_alias):
        '''
        Objective: Returns switch DPID, given a switch alias
        
        Input:  
        | `switch_alias` |  User defined switch alias | 
        
        Description:
        The function 
        - executes a REST GET for http://<CONTROLLER_IP>:8082/api/v1/data/controller/core/switch?select=alias
        - and greps for switch-alias, and returns switch-dpid
        
        Return value
        - Switch DPID
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url ='/api/v1/data/controller/core/switch?select=alias'
                c.rest.get(url)
                content = c.rest.content()
                for x in range (0,len(content)):
                    if str(content[x]['alias']) == str(switch_alias):
                        return content[x]['dpid']
                return False
            except:
                return False
    
    def rest_show_switch_flow(self,switch_alias=None, sw_dpid=None):
        '''
        Objective: 
        - Returns number of flows on a switch
        
        Input: 
        | 'switch_dpid' |  Datapath ID of the switch | 
        
        Description:
        - The function executes a REST GET for http://<CONTROLLER_IP>:8082/api/v1/data/controller/core/switch[dpid="<SWITCH_DPID>"]?select=stats/table
        - Returns number of active flows
        
        Return value: 
        - Number of active flows on the switch
        '''
        t=test.Test()
        try:
            c= t.controller('master')
        except:
            return False

        else:
            try:
                if (switch_alias is None and sw_dpid is not None):
                    switch_dpid = sw_dpid
                elif (switch_alias is None and sw_dpid is None):
                    helpers.log('Either Switch DPID or Switch Alias has to be provided')
                    return False
                elif (switch_alias is not None and sw_dpid is None):
                    switch_dpid = self.rest_get_switch_dpid(switch_alias)
                else:
                    switch_dpid = sw_dpid
                url = '/api/v1/data/controller/core/switch[dpid="%s"]?select=stats/table' % (str(switch_dpid))
                c.rest.get(url)
                content = c.rest.content()
            except:
                helpers.test_failure("Could not execute command")
                return False
            else:
                helpers.log("Return value for number of flows is %s" % content[0]['stats']['table'][1]['active-count'])
                return content[0]['stats']['table'][1]['active-count']

###################################################
# All Bigtap Verify Commands Go Here:
###################################################

    def rest_verify_policy_key(self,policy_name,method,index,key):
        '''
            Objective:
            - Execute a rest get and verify if a particular key exists in a policy
        
            Inputs
            | `policy_name` |  Policy Name being tested for| 
            | `method`    |  Methods can be info/rule/filter-interface/delivery-interface/service-interface/core-interface/failed-paths| 
            | `index`    |  Index in the array| 
            | `key`      |  Particular key we are looking for.| 
            
            Description:
                rest_check_policy_key('testPolicy','ip-proto',0,'rule') would check execute a REST get on "http://<CONTROLLER_IP>:8082/api/v1/data/controller/applications/bigtap/view/policy[name="testPolicy"]/rule
                and return the value "ip-proto"
            
            Return Value: 
            - Value of key if the key exists, 
            - False if it does not.
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url = '/api/v1/data/controller/applications/bigtap/view/policy[name="%s"]/%s' % (str(policy_name),str(method))
                c.rest.get(url)
            except:
                return False
            else:
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                if(c.rest.content()):
                    content = c.rest.content()
                    return content[index][key]
                else :
                    helpers.test_log("ERROR Policy %s does not exist. Error seen: %s" % (str(policy_name),c.rest.result_json()))
                    return False
###################################################
# All Bigtap Configuration Commands Go Here:
###################################################    
    def rest_add_interface_role(self,intf_name,intf_type,intf_nickname,switch_alias=None, sw_dpid=None):
        '''
            Objective:
            - Execute the CLI command 'bigtap role filter interface-name F1'
        
            Input: 
            | `switch_dpid` |  DPID of the switch | 
            | `intf_name`    |  Interface Name viz. etherenet1, ethernet2 etc. | 
            | `intf_type`    |  Interface Type viz. filter, delivery, service | 
            | `intf_nickname` |  Nickname for the interface for eg. F1, D1, S1 etc. | 
            
            Return Value: 
            - True if configuration is successful
            - False otherwise
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                if (switch_alias is None and sw_dpid is not None):
                    switch_dpid = sw_dpid
                elif (switch_alias is None and sw_dpid is None):
                    helpers.log('Either Switch DPID or Switch Alias has to be provided')
                    return False
                elif (switch_alias is not None and sw_dpid is None):
                    switch_dpid = self.rest_get_switch_dpid(switch_alias)
                else:
                    switch_dpid = sw_dpid
                url = '/api/v1/data/controller/applications/bigtap/interface-config[interface="%s"][switch="%s"]' % (str(intf_name), str(switch_dpid))
                c.rest.put(url, {"interface": str(intf_name), "switch": str(switch_dpid), 'role':str(intf_type),'name':str(intf_nickname)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True

    def rest_delete_interface_role(self,intf_name,intf_type,intf_nickname,switch_alias=None, sw_dpid=None):
        '''
            Objective:
            - Delete filter/service/delivery interface from switch configuration. 
         
            Input: 
             | `switch_dpid` | Datapath ID of the switch | 
             | `intf_name` |  Interface Name viz. etherenet1, ethernet2 etc. | 
             | `intf_type` | Interface Type viz. filter, delivery, service | 
             | `intf_nickname` | Nickname for the interface for eg. F1, D1, S1 etc. | 
                
            Description:
            - Similar to executing the CLI command 'no bigtap role filter interface-name F1'
            
            Return Value: 
            - True if configuration is successful
            - False otherwise    
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                if (switch_alias is None and sw_dpid is not None):
                    switch_dpid = sw_dpid
                elif (switch_alias is None and sw_dpid is None):
                    helpers.log('Either Switch DPID or Switch Alias has to be provided')
                    return False
                elif (switch_alias is not None and sw_dpid is None):
                    switch_dpid = self.rest_get_switch_dpid(switch_alias)
                else:
                    switch_dpid = sw_dpid
    
                url='/api/v1/data/controller/applications/bigtap/interface-config[interface="%s"][switch="%s"]' % (str(intf_name), str(switch_dpid)) 
                c.rest.delete(url, {'role':str(intf_type), "name": str(intf_nickname)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:            
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    return True

    def rest_delete_interface(self,intf_name,switch_alias=None, sw_dpid=None):
        '''
            Objective
            - Delete interface from switch
         
            Input: 
             | `switch_dpid` | DPID of the switch | 
             | `intf_name` | Interface Name viz. etherenet1, ethernet2 etc. | 
            
            Return Value: 
            - True if configuration delete is successful
            - False otherwise       
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                if (switch_alias is None and sw_dpid is not None):
                    switch_dpid = sw_dpid
                elif (switch_alias is None and sw_dpid is None):
                    helpers.log('Either Switch DPID or Switch Alias has to be provided')
                    return False
                elif (switch_alias is not None and sw_dpid is None):
                    switch_dpid = self.rest_get_switch_dpid(switch_alias)
                else:
                    switch_dpid = sw_dpid
                url='/api/v1/data/controller/core/switch[dpid="%s"]/interface[name=""]'  % (str(switch_dpid), str(intf_name))
                c.rest.delete(url, {})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    return True

    def rest_add_policy(self,rbac_view_name,policy_name,policy_action="inactive"):
        '''
            Objective:
            - Add a bigtap policy.
        
            Input:
             | rbac_view_name` | RBAC View Name for eg. admin-view | 
             | `policy_name` | Policy Name | 
             | `policy_action` | Policy action. The permitted values are "forward" or "rate-measure", default is inactive | 
            
            Return Value: 
            - True if configuration is successful
            - False otherwise       
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]' % (str(rbac_view_name), str(policy_name))
                c.rest.put(url,{'name':str(policy_name)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                try:
                    c.rest.patch(url,{"action": str(policy_action) })
                except:
                    helpers.test_failure(c.rest.error())
                    return False
                else:          
                    return True

    def rest_delete_policy(self,rbac_view_name,policy_name):
        '''
            Objective:
            - Delete a bigtap policy.
        
            Input:
             | `rbac_view_name` | RBAC View Name for eg. admin-view | 
             | `policy_name` | Policy Name | 
            
            Return Value: 
            - True if configuration delete is successful
            - False if configuration delete is unsuccessful          
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]' % (str(rbac_view_name), str(policy_name))
                c.rest.delete(url,{})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    return True

    def rest_add_policy_interface(self,rbac_view_name,policy_name,intf_nickname,intf_type):
        '''
            Objective:
            - Add a bigtap policy interface viz. Add a filter-interface and/or delivery-interface under a bigtap policy.
        
            Input:
             | `rbac_view_name` |   RBAC View Name for eg. admin-view| 
             | `policy_name` |  Policy Name| 
             | `intf_nickname` |  Interface Nick-Name for eg. F1 or D1 | 
             | `intf_type` |  Interface Type. Allowed values are `filter` or `delivery` | 
            
            Return Value: 
            - True if configuration delete is successful
            - False if configuration delete is unsuccessful     
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                if "filter" in str(intf_type) :
                    intf_type = "filter-group"
                else :
                    intf_type = "delivery-group"
                url='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]/%s[name="%s"]' % (str(rbac_view_name), str(policy_name),str(intf_type),str(intf_nickname))
                c.rest.put(url,{"name": str(intf_nickname)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    return True
    
    def rest_delete_policy_interface(self,rbac_view_name,policy_name,intf_nickname,intf_type):
        '''
            Objective:
            - Delete a bigtap policy interface viz. 
            - Delete a filter-interface and/or delivery-interface from a bigtap policy.
        
            Input:
            | `rbac_view_name` | RBAC View Name for eg. admin-view | 
            | `policy_name` | Policy Name | 
            | `intf_nickname` | Interface Nick-Name for eg. F1 or D1 | 
            | `intf_type` | Interface Type. Allowed values are `filter` or `delivery` | 
            
            Return Value: 
            - True if configuration delete is successful
            - False if configuration delete is unsuccessful    
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                if "filter" in str(intf_type) :
                    intf_type = "filter-group"
                else :
                    intf_type = "delivery-group"
                url='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]/%s[name="%s"]' % (str(rbac_view_name), str(policy_name),str(intf_type),str(intf_nickname))
                c.rest.delete(url,{})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    return True
  
    def rest_add_policy_match(self,rbac_view_name,policy_name,match_number,data):
        '''
            Objective:
            - Add a bigtap policy match condition.
        
            Input:
            | `rbac_view_name`| RBAC View Name for eg. admin-view | 
            | `policy_name` | Policy Name | 
            | `match_number` |  Match number like the '1' in  '1 match tcp | 
            | `data` | Formatted data field like  {"ether-type": 2048, "dst-tp-port": 80, "ip-proto": 6, "sequence": 1} | 
            
            Return Value: 
            - True if configuration add is successful
            - False if configuration add is unsuccessful         
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]/rule[sequence=%s]'  % (str(rbac_view_name),str(policy_name),str(match_number))
                data_dict = helpers.from_json(data)
                c.rest.put(url,data_dict)
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    return True
    
    def rest_delete_policy_match(self,rbac_view_name,policy_name,match_number):
        '''
            Objective:
            - Delete a bigtap policy match condition.
        
            Input:
            | `rbac_view_name` |  RBAC View Name for eg. admin-view | 
            | `policy_name` | Policy Name | 
            | `match_number` |  Match number like the '1' in  '1 match tcp | 
            
            Return Value: 
            - True if configuration delete is successful
            - False if configuration delete is unsuccessful         
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]/rule[sequence="%s"]'  % (str(rbac_view_name),str(policy_name),str(match_number))
                c.rest.delete(url,{})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                return True
        
# Add a service with Pre-Service and Post Service interface.
    def rest_add_service(self,service_name,pre_service_intf_nickname,post_service_intf_nickname):
        '''
            Objective:
            - Add a bigtap service.
        
            Input:
            | `service_name`| Name of Service | 
            | `pre_service_intf_nickname`| Name of pre-service interface | 
            | `post_service_intf_nickname`| Name of post-service interface | 
            
            Return Value: 
            - True if configuration add is successful
            - False if configuration add is unsuccessful  
        
            Examples:
                | rest add bigtap service  |  S1-LB7  |  S1-LB7_E3-HP1_E3-PRE  |  S1-LB7_E4-HP1_E4-POST  |  
                Result is 
                bigtap service S1-LB7
                  post-service S1-LB7_E4-HP1_E4-POST
                  pre-service S1-LB7_E3-HP1_E3-PRE
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url='/api/v1/data/controller/applications/bigtap/service[name="%s"]' % (str(service_name))
                c.rest.put(url,{"name":str(service_name)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                try:
                    #Add Pre-Service Interface
                    url_add_intf ='/api/v1/data/controller/applications/bigtap/service[name="%s"]/pre-group[name="%s"]'  % (str(service_name),str(pre_service_intf_nickname))
                    c.rest.put(url_add_intf, {"name":str(pre_service_intf_nickname)})
                except:
                    helpers.test_failure(c.rest.error())
                    return False
                else:     
                    try:
                        #Add Post-Service Interface
                        url_add_intf ='/api/v1/data/controller/applications/bigtap/service[name="%s"]/post-group[name="%s"]'  % (str(service_name),str(post_service_intf_nickname))
                        c.rest.put(url_add_intf, {"name":str(post_service_intf_nickname)})
                    except:
                        helpers.test_failure(c.rest.error())
                        return False
                    else:  
                        helpers.test_log(c.rest.content_json())
                        return True
 
# Delete a service
    def rest_delete_service(self,service_name) :
        '''
            Objective:
            - Delete a bigtap service.
        
            Input:
            | `service_name` | Name of Service |
            
            Return Value: 
            - True if configuration delete is successful
            - False if configuration delete is unsuccessful  
        
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url='/api/v1/data/controller/applications/bigtap/service[name="%s"]'  % (str(service_name))
                c.rest.delete(url,{})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True
    
    def rest_add_interface_service(self,service_name,intf_type,intf_nickname):
        '''
            Objective:
            - Add a service interface to a service. 
            - This is similar to executing CLI command "post-service S1-LB7_E4-HP1_E4-POST"
        
            Input:
            | `service_name` | Name of Service |
            | `intf_type`  | Interface Type. Acceptable values are `pre` or `post` |
            | `post_service_intf_nickname` | Name of pre/post-service interface for e.g. S1-LB7_E4-HP1_E4-POST |
            
            Return Value: 
            - True if configuration add is successful
            - False if configuration add is unsuccessful  
        
            Examples:
                | rest add interface service  |  S1-LB7  |  post  |  S1-LB7_E4-HP1_E4-POST  |  
                Result is 
                bigtap service S1-LB7
                  post-service S1-LB7_E4-HP1_E4-POST
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                if "pre" in str(intf_type) :
                    url_add_intf ='/api/v1/data/controller/applications/bigtap/service[name="%s"]/pre-group[name="%s"]'  % (str(service_name),str(intf_nickname))
                else :
                    url_add_intf ='/api/v1/data/controller/applications/bigtap/service[name="%s"]/post-group[name="%s"]'  % (str(service_name),str(intf_nickname))
                c.rest.post(url_add_intf, {"name":str(intf_nickname)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True

    def rest_delete_interface_service(self,service_name,intf_nickname,intf_type) :
        '''
            Objective:
            - Delete an interface from a service. This is similar to executing CLI command "no post-service S1-LB7_E4-HP1_E4-POST"
        
            Input:
            | `service_name` | Name of Service |
            | `intf_type` | Interface Type. Acceptable values are `pre` or `post` |
            | `post_service_intf_nickname` | Name of pre/post-service interface for e.g. S1-LB7_E4-HP1_E4-POST |
            
            Return Value: 
            - True if configuration add is successful
            - False if configuration add is unsuccessful  
        
            Examples:
                | rest delete interface service  |  S1-LB7  |  post  |  S1-LB7_E4-HP1_E4-POST  |  
                Result is 
                bigtap service S1-LB7
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                if "pre" in str(intf_type) :
                    url_add_intf ='/api/v1/data/controller/applications/bigtap/service[name="%s"]/pre-group[name="%s"]'  % (str(service_name),str(intf_nickname))
                else :
                    url_add_intf ='/api/v1/data/controller/applications/bigtap/service[name="%s"]/post-group[name="%s"]'  % (str(service_name),str(intf_nickname))
                c.rest.delete(url_add_intf, {})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True

    def rest_add_service_to_policy(self,rbac_view_name,policy_name,service_name,sequence_number) :
        '''
          Objective:
          - Add a service to a policy. This is similar to executing CLI command "use-service S1-LB7 sequence 1"
        
          Input:
            |`rbac_view_name` | RBAC View Name for eg. admin-view |
            |`policy_name` | Policy Name |
            |`service_name` | Name of Service |
            |`sequence_number`| Sequence number of the policy, to determine order in which policies are processed |
            
          Return Value:
            - True if action add for policy is successful
            - False if action add for policy is unsuccessful
        
          Examples:
                | rest add service to policy  |  admin-view  |  testPolicy  |  S1-LB7  |  1  |  
                Result is 
                bigtap policy testPolicy rbac-permission admin-view
                    ...
                    ...
                    ...
                    use-service S1-LB7 sequence 1
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url_to_add ='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]/service[sequence=%s]' % (str(rbac_view_name),str(policy_name),str(sequence_number))
                c.rest.put(url_to_add, {"name":str(service_name), "sequence" : int(sequence_number)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True

    def rest_delete_service_from_policy(self,rbac_view_name,policy_name,service_name) :
        '''
            Objective:
            - Delete a service from a policy. This is similar to executing CLI command "no use-service S1-LB7 sequence 1"
        
            Input:
            |`rbac_view_name`| RBAC View Name for eg. admin-view |
            |`policy_name` | Policy Name |
            |`service_name` | Name of Service |
            
            Return Value:
            - True if action delete for policy is successful
            - False if action delete for policy is unsuccessful
        
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url ='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]/service[name="%s"]' % (str(rbac_view_name),str(policy_name),str(service_name))
                c.rest.delete(url, {})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True

#Change policy action
    def rest_add_policy_action(self,rbac_view_name,policy_name,policy_action):
        '''
          Objective:
          - Change the action field in a bigtap policy
        
          Input:
           |`rbac_view_name`|RBAC View Name for eg. admin-view |    
           |`policy_name`|Policy Name |
           |`policy_action`|Desired action. Values are `forward`, `rate-measure` and `inactive` |

          
          Description: 
          Change a bigtap policy action from 
          - Forward --> Rate-Measure, 
          - Forward --> Inactive, 
          - Rate-Measure--> Forward, 
          - Rate-Measure--> Inactive
          
          Return Value:
            - True if action change for policy is successful
            - False if action change for policy is unsuccessful

          Examples:
                | rest change policy action  |  admin-view  |  testPolicy  |  rate-measure |  
                Result is 
                bigtap policy testPolicy rbac-permission admin-view
                    action rate-measure
                    ...
                    ...
                    ...
        
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url ='/api/v1/data/controller/applications/bigtap/view[name="%s"]/policy[name="%s"]' % (str(rbac_view_name),str(policy_name))
                c.rest.patch(url,{"action":str(policy_action)})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True

#Alias
    def rest_update_policy_action(self,rbac_view_name,policy_name,policy_action):
        return self.rest_add_policy_action(rbac_view_name, policy_name, policy_action)


#Disable bigtap feature overlap/inport-mask/tracked-host/l3-l4-mode
    def rest_disable_feature(self,feature_name):
        '''
            Objective:
            - Disable a bigtap feature
        
           Input:
            | `feature_name` | Bigtap Feature Name. \n Currently allowed feature names are `overlap`,`inport-mask`,`tracked-host`,`l3-l4-mode` | 
            
            Return Value 
            - True if feature is enabled
            - False if feature could not be enabled
            
            Examples:
                | rest disable feature  |  overlap |  
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url ='/api/v1/data/controller/applications/bigtap/feature'
                c.rest.patch(url,{str(feature_name): False})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True
    
#Enable bigtap feature overlap/inport-mask/tracked-host/l3-l4-mode
    def rest_enable_feature(self,feature_name):
        '''
            Objective:
            - Enable a bigtap feature
        
           Input:
            | `feature_name` | Bigtap Feature Name. \n Currently allowed feature names are `overlap`,`inport-mask`,`tracked-host`,`l3-l4-mode` | 
            
            Return Value 
            - True if feature is enabled
            - False if feature could not be enabled
            
            Examples:
                | rest enable feature  |  overlap |  
        '''
        try:
            t = test.Test()
        except:
            return False
        else:
            c= t.controller('master')
            try:
                url ='/api/v1/data/controller/applications/bigtap/feature'
                c.rest.patch(url,{str(feature_name): True})
            except:
                helpers.test_failure(c.rest.error())
                return False
            else:  
                if not c.rest.status_code_ok():
                    helpers.test_failure(c.rest.error())
                    return False
                else:
                    helpers.test_log(c.rest.content_json())
                    return True
        
#Compare coreswitch flows
    def rest_verify_coreswitch_flows(self,flow_1,flow_2,flow_value_1,flow_value_2):
        '''
            Objective
            - Compare coreswitch flow counts. Useful when we have multiple core-switches.
        
            Inputs:
            | flow_1 | Number of flows on core switch 1 | 
            | flow_2 | Number of flows on core switch 2 | 
            | flow_value_1 | Desired number of flows on switch 1 or switch 2 | 
            | flow_value_2 | Desired number of flows on switch 1 or switch 2 | 
        
            Return Value 
            - True if flow is found on switch
            - False if flow is not found on switch
        '''
        if ((flow_1 == flow_value_1) and (flow_2 == flow_value_2 )) or ((flow_2 == flow_value_1) and (flow_1 == flow_value_2 )) :
            return True
        else :
            return False