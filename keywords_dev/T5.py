import autobot.helpers as helpers
import autobot.restclient as restclient
import autobot.test as test
import re


class T5(object):

    def __init__(self):
        t = test.Test()
        c = t.controller()
        
        url = '%s/api/v1/auth/login' % c.base_url
        result = c.rest.post(url, {"user":"admin", "password":"adminadmin"})
        session_cookie = result['content']['session_cookie']
        c.rest.set_session_cookie(session_cookie)
        
    def rest_create_tenant(self, tenant):
        
        t = test.Test()
        c = t.controller()

        helpers.log("Input arguments: tenant = %s" % tenant )
                
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]' % (c.base_url, tenant)
        c.rest.put(url, {"name": tenant})
        helpers.log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
        
    def _rest_show_tenant(self, tenant=None, negative=False):
        t = test.Test()
        c = t.controller()

        if tenant:
            # Show a specific tenant
            url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]' % (c.base_url, tenant)
        else:
            # Show all tenants
            url = '%s/api/v1/data/controller/applications/bvs/tenant' % (c.base_url)
            
        c.rest.get(url)
        helpers.log("Output: %s" % c.rest.result_json())
        
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        data = c.rest.content()

        # If showing all tenants, then we don't need to check further
        if tenant is None:
            return data
        
        # Search list of tenants to find a match
        for t in data:
            actual_tenant = t['name']
            if actual_tenant == tenant:
                helpers.log("Match: Actual tenant '%s' == expected tenant '%s'" % (actual_tenant, tenant))
                
                if negative:
                    helpers.test_failure("Unexpected match: Actual tenant '%s' == expected tenant '%s'" % (actual_tenant, tenant))
                else:
                    return data
            else:
                helpers.log("No match: Actual tenant '%s' != expected tenant '%s'" % (actual_tenant, tenant))
        
        # If we reach here, then we didn't find a matching tenant.
        if negative:
            helpers.log("Expected No match: For tenant '%s'" % tenant)
            return data
        else:
            helpers.test_failure("No match: For tenant '%s'." % tenant)

    def rest_show_tenant(self, tenant=None):
        helpers.log("Input arguments: tenant = %s" % tenant )
        return self._rest_show_tenant(tenant)
        
    def rest_show_tenant_gone(self, tenant=None):
        helpers.log("Input arguments: tenant = %s" % tenant )
        return self._rest_show_tenant(tenant, negative=True)
        
    def rest_delete_tenant(self, tenant=None):
        t = test.Test()
        c = t.controller()

        helpers.log("Input arguments: tenant = %s" % tenant )
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]' % (c.base_url, tenant)

        c.rest.delete(url, {"name": tenant})
        helpers.log("Ouput: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()

    def test_args(self, arg1, arg2, arg3):
        try:
            helpers.log("Input arguments: arg1 = %s" % arg1 )
            helpers.log("Input arguments: arg2 = %s" % arg2 )
            helpers.log("Input arguments: arg3 = %s" % arg3 )
        except:
            return False
        else:
            return True

    def rest_create_vns(self, tenant, vns):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s" % (tenant, vns ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]' % (c.base_url, tenant, vns)
        try:
            c.rest.put(url, {"name": vns})
        except:
            helpers.test_failure(c.rest.error())
        else:
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())
    
            return c.rest.content()
    
    def rest_delete_vns(self, tenant, vns=None):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s" % (tenant, vns ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]' % (c.base_url, tenant, vns)
        try:
            c.rest.delete(url, {"name": vns})
        except:
            helpers.test_log("Output: %s" % c.rest.result_json())
        else:
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())

            return c.rest.content()
    def rest_show_vns(self):
        t = test.Test()
        c = t.controller()
  
        url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/vnses' % (c.base_url)
       
        try:
            c.rest.get(url)
        except:
            helpers.test_log("Output: %s" % c.rest.result_json())
        else:
            if not c.rest.status_code_ok():
                helpers.test_failure(c.rest.error())

            return c.rest.content()
     
    def rest_create_portgroup(self, pg):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: port-group = %s" % pg )
        
        url = '%s/api/v1/data/controller/fabric/port-group[name="%s"]' % (c.base_url, pg)
        c.rest.put(url, {"name": pg})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
    
    def rest_delete_portgroup(self, pg=None):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: port-group = %s" % pg )
        
        url = '%s/api/v1/data/controller/fabric/port-group[name="%s"]' % (c.base_url, pg)
        c.rest.delete(url, {"name": pg})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()


    def rest_create_endpoint(self, tenant, vns, endpoint):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"
        
            Input:
                `tenant`          tenant name
                `vns`         vns name
                `endpoint`    endpoint name
            Return: true if configuration is successful, false otherwise
            http://127.0.0.1:8080/api/v1/data/controller/applications/bvs/tenant[name="A"]/vns[name="A1"]/endpoints[name="H1"] {"name": "H1"}

        '''
        
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s, vns = %s, endpoint = %s" % (tenant, vns, endpoint ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/endpoints' % (c.base_url, tenant, vns)
        try:
            c.rest.post(url, {"name": endpoint})
        except:
            helpers.test_failure(c.rest.error())
        else: 
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()                         

    
#    def rest_create_endpoint(self, tenant, vns, endpoint):
#        t = test.Test()
#        c = t.controller()
        
#        helpers.test_log("Input arguments: tenant = %s, vns = %s, endpoint = %s" % (tenant, vns, endpoint ))
        
#        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/endpoints[name="%s"]' % (c.base_url, tenant, vns, endpoint)
#        c.rest.put(url, {"name": endpoint})
#        helpers.test_log("Output: %s" % c.rest.result_json())

 #       if not c.rest.status_code_ok():
 #           helpers.test_failure(c.rest.error())

#        return c.rest.content()
    
    def rest_delete_endpoint(self, tenant, vns, endpoint=None):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s endpoint = %s" % (tenant, vns, endpoint ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/endpoints[name="%s"]' % (c.base_url, tenant, vns, endpoint)
        c.rest.delete(url, {"name": endpoint})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
   
    def rest_add_interface_to_portgroup(self, switch, intf, pg):
        t = test.Test()
        c = t.controller()
                       
        helpers.test_log("Input arguments: switch-name = %s Interface-name = %s port-group = %s" % (switch, intf, pg))
        
        url = '%s/api/v1/data/controller/core/switch-config[name="%s"]/interface[name="%s"]' % (c.base_url, switch, intf)
        c.rest.put(url, {"name": intf, "port-group-name": pg})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
    
    def rest_delete_interface_from_portgroup(self, switch, intf, pg):
        t = test.Test()
        c = t.controller()
                
        helpers.test_log("Input arguments: switch-name = %s Interface-name = %s port-group = %s" % (switch, intf, pg))
        
        url = '%s/api/v1/data/controller/core/switch-config[name="%s"]/interface[name="%s"]' % (c.base_url, switch, intf)
        c.rest.delete(url, {"core/switch-config/interface/port-group-name": pg})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
    
    def rest_add_portgroup_to_vns(self, tenant, vns, pg, vlan):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s port-group = %s vlan = %s" % (tenant, vns, pg, vlan ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/port-group-membership-rules[port-group-name="%s"]' % (c.base_url, tenant, vns, pg)
        c.rest.put(url, {"vlan": vlan, "port-group-name": pg})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
            
    def rest_add_portgroup_to_endpoint(self, tenant, vns, endpoint, pg, vlan):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s endpoint = %s port-group = %s vlan = %s" % (tenant, vns, endpoint, pg, vlan ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/endpoints[name="%s"]/attachment-point' % (c.base_url, tenant, vns, endpoint)
        c.rest.put(url, {"port-group-name": pg, "vlan": vlan})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
            
    def rest_delete_portgroup_from_vns(self, tenant, vns, pg, vlan):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s port-group = %s vlan = %s" % (tenant, vns, pg, vlan ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/port-group-membership-rules[port-group-name="%s"]' % (c.base_url, tenant, vns, pg)
        c.rest.delete(url, {"vlan": vlan})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
            
    def rest_add_interface_to_vns(self, tenant, vns, switch, intf, vlan):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s switch-name = %s interface-name = %s vlan = %s" % (tenant, vns, switch, intf, vlan ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/switch-port-membership-rules[switch-name="%s"][interface-name="%s"]' % (c.base_url, tenant, vns, switch, intf)
        c.rest.put(url, {"switch-name": switch, "interface-name": intf, "vlan": vlan})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content() 
      
    def rest_delete_interface_from_vns(self, tenant, vns, switch, intf, vlan):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s switch-name = %s interface-name = %s vlan = %s" % (tenant, vns, switch, intf, vlan ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/switch-port-membership-rules[switch-name="%s"][interface-name="%s"]' % (c.base_url, tenant, vns, switch, intf)
        c.rest.delete(url, {"vlan": vlan})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        return c.rest.content()
            
    def rest_add_interface_to_endpoint(self, tenant, vns, endpoint, switch, intf, vlan):
        t = test.Test()
        c = t.controller()
        
        helpers.test_log("Input arguments: tenant = %s vns = %s endpoint = %s switch-name = %s interface-name = %s vlan = %s" % (tenant, vns, endpoint, switch, intf, vlan ))
        
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/endpoints[name="%s"]/attachment-point' % (c.base_url, tenant, vns, endpoint)
        c.rest.put(url, {"switch-name": switch, "interface-name": intf, "vlan": vlan})
        helpers.test_log("Output: %s" % c.rest.result_json())

        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())
            
        return c.rest.content()
    
    def rest_configure_ip_endpoint(self, tenant, vns, endpoint, ip):
        t = test.Test()
        c = t.controller()
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/endpoints[name="%s"]' % (c.base_url, tenant, vns, endpoint)
        c.rest.patch(url, {"ip-address": ip})
        helpers.test_log("Output: %s" % c.rest.result_json())
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())
        return c.rest.content()
    
    def rest_configure_mac_endpoint(self, tenant, vns, endpoint, mac):
        t = test.Test()
        c = t.controller()
        url = '%s/api/v1/data/controller/applications/bvs/tenant[name="%s"]/vns[name="%s"]/endpoints[name="%s"]' % (c.base_url, tenant, vns, endpoint)
        c.rest.patch(url, {"mac": mac})
        helpers.test_log("Output: %s" % c.rest.result_json())
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())
        return c.rest.content()
    
    def rest_verify_vns(self):
        '''Verify VNS information
        
            Input:           
            
            Return: true if it matches the created VNS (string starts with "v")
        '''
        t = test.Test()
        c = t.controller()
        url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/vnses' % (c.base_url)
        c.rest.get(url)
        data = c.rest.content()
        for i in range(0,len(data)):
                if len(data) != 0:
                     if (int(data[i]["internal-vlan"]) != 0):
                         helpers.log("Expected VNS's are present in the config")
                         return True
                     else:
                         helpers.test_failure("Expected VNS's are not present in the config")  
                         return False     
                else:
                     helpers.log("No VNS are configured")
                     return False
        
    def rest_verify_tenant(self):
        '''Verify CLI tenant information
        
            Input:   None        
            
            Return: true if it matches the created tenant (string starts with "t")
        '''
        t = test.Test()
        c = t.controller()
        url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/tenants' % (c.base_url)
        c.rest.get(url)
        data = c.rest.content()
        for i in range(0,len(data)):
                if len(data) != 0:
                    if data[i]["tenant-name"] == re.search('t\B', 'data[i]["tenant-name"]'):
                        helpers.log("Expected Tenants are present in the config")
                        return True
                    else:
                        helpers.test_failure("Expected Tenants are not present in the config")
                        return False 
                else:
                     helpers.log("No tenants are configured")
                     return False       
       
            
    def rest_verify_endpoint(self, vns, vlan, ipaddr, switch, intf):
         '''Verify Dynamic Endpoint entry
        
            Input: vns name , vlan ID , ipaddress , switch name, expected switch interface          
            
            Return: true if it matches Value specified
         '''
         t = test.Test()
         c = t.controller()
         url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/endpoints' % (c.base_url)
         c.rest.get(url)
         data = c.rest.content()
         if len(data) != 0:
             for i in range(0,len(data)):
                 if str(data[i]["vns-name"]) == vns:
                     if str(data[i]["attachment-point"]["vlan"]) == str(vlan):
                         if (data[i]["ip-address"] == str(ipaddr)) :
                             if (data[i]["attachment-point"]["switch-name"] == switch) :
                                 if (data[i]["attachment-point"]["interface-name"] == str(intf)) :
                                     helpers.log("Expected Endpoints are created data matches is %s" % data[i]["ip-address"] )
                                     return True
                                 else:
                                    helpers.test_failure("Expected endpoints %s are not created" % (str(ipaddr)))
                                    return False
         else:
              helpers.test_failure("Expected vns are not created %s" % vns)
              return False
            
    def rest_verify_endpoint_static(self, vns, vlan, ipaddr, switch, intf):
         '''Verify Static Endpoint entry
        
            Input: vns name , vlan ID , ipaddress , switch name, expected switch interface          
            
            Return: true if it matches Value specified and configured attachment point is true
         '''
         t = test.Test()
         c = t.controller()
         url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/endpoints' % (c.base_url)
         c.rest.get(url)
         data = c.rest.content()
         if len(data) != 0:
             for i in range(0,len(data)):
                 if str(data[i]["vns-name"]) == vns:
                     if str(data[i]["attachment-point"]["vlan"]) == str(vlan):
                         if (data[i]["ip-address"] == str(ipaddr)) :
                             if (data[i]["attachment-point"]["switch-name"] == switch) :
                                 if (data[i]["attachment-point"]["interface-name"] == str(intf)) :
                                     if (data[i]["configured-endpoint"] == True) :
                                          helpers.log("Expected Endpoints are created data matches is %s" % data[i]["ip-address"] )
                                          return True
                                     else:
                                          helpers.test_failure("Expected endpoints %s are not created" % (str(ipaddr)))
                                          return False
         else:
              helpers.test_failure("Expected vns are not created %s" % vns)
              return False
            

    def rest_verify_endpoint_portgroup(self, vns, vlan, ipaddr, pg):
         '''Verify Dynamic Endpoint entry
        
            Input: vns name , vlan ID , ipaddress , portgroup name          
            
            Return: true if it matches Value specified
         '''
         t = test.Test()
         c = t.controller()
         url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/endpoints' % (c.base_url)
         c.rest.get(url)
         data = c.rest.content()
         if len(data) != 0:
             for i in range(0,len(data)):
                 if str(data[i]["vns-name"]) == vns:
                     if str(data[i]["attachment-point"]["vlan"]) == str(vlan):
                         if (data[i]["ip-address"] == str(ipaddr)) :
                             if (data[i]["attachment-point"]["port-group-name"] == pg) :
                                  helpers.log("Expected Endpoints are created data matches is %s" % data[i]["ip-address"] )
                                  return True
                             else:
                                  helpers.test_failure("Expected endpoints %s are not created" % (str(ipaddr)))
                                  return False
         else:
              helpers.test_failure("Expected vns are not created %s" % vns)
              return False       
   
    def rest_verify_endpoint_static_portgroup(self, vns, vlan, ipaddr, pg):
         '''Verify Static Endpoint entry
        
            Input: vns name , vlan ID , ipaddress , portgroup name          
            
            Return: true if it matches Value specified and configured attachment point is true
         '''
         t = test.Test()
         c = t.controller()
         url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/endpoints' % (c.base_url)
         c.rest.get(url)
         data = c.rest.content()
         if len(data) != 0:
             for i in range(0,len(data)):
                 if str(data[i]["vns-name"]) == vns:
                     if str(data[i]["attachment-point"]["vlan"]) == str(vlan):
                         if (data[i]["ip-address"] == str(ipaddr)) :
                             if (data[i]["attachment-point"]["port-group-name"] == pg) :
                                 if (data[i]["configured-endpoint"] == True) :
                                     helpers.log("Expected Endpoints are created data matches is %s" % data[i]["ip-address"] )
                                     return True
                                 else:
                                     helpers.test_failure("Expected endpoints %s are not created" % (str(ipaddr)))
                                     return False
         else:
              helpers.test_failure("Expected vns are not created %s" % vns)
              return False
    
    def rest_verify_vns_interface(self, vns, intf_num):
        '''Verify VNS Membership Interface information
        
            Input:  specific VNS Name  and number of interfaces to be present in the VNS       
            
            Return: Num of ports part of the specific VNS
        '''
        t = test.Test()
        c = t.controller()
        url = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/vnses[name="%s"]' % (c.base_url, vns)
        c.rest.get(url)
        data = c.rest.content()
        if data[0]["name"] == vns:
            if (int(data[0]["num-ports"]) == int(intf_num)) :
                   helpers.log("Expected Member port counts in VNS are correct %d = %d" % (int(intf_num), int(data[0]["num-ports"])))
                   return True
            else:
                   helpers.test_failure("Membership count in VNS are not correct %d = %d" % (int(intf_num), int(data[0]["num-ports"])))  
                   return False     
        else:
             helpers.log("Expected VNS are configured")
             return False

        
    def rest_verify_forwarding_vlan(self, dpid):
        '''Verify VNS(VLAN) Information in Controller Forwarding Table
        
            Input:  Specific DPID of the switch      
            
            Return: vlan table from the forwarding table with membership ports.
        '''
        t = test.Test()
        c = t.controller()
        url = '%s/api/v1/data/controller/applications/bvs/info/forwarding/network/switch[switch-id="%s"]/vlan-table' % (c.base_url, dpid)
        c.rest.get(url)
        data = c.rest.content()
        no_of_vlans = len(data)
        url1 = '%s/api/v1/data/controller/applications/bvs/info/endpoint-manager/vnses' % (c.base_url)
        data1 = c.rest.content()
        no_of_vns = len(data1)
        if (int(no_of_vns) == int(no_of_vlans)):
              helpers.log("Vlan Entries are present in forwarding table Actual:%d = Expected:%d" % (int(no_of_vns), int(no_of_vlans)))
              return True
        else:
              helpers.test_failure("Vlan Entries are inconsistent in forwarding table %d = %d" % (int(no_of_vns), int(no_of_vlans)))  
              return False     
         
    def rest_verify_forwarding_port(self, dpid):
        '''Verify Edge port  Information in Controller Forwarding Table
        
            Input:  Specific DPID of the switch      
            
            Return: port table with associated Lag id will be provided
        '''
        t = test.Test()
        c = t.controller()
        url = '%s/api/v1/data/controller/applications/bvs/info/forwarding/network/switch[switch-id="%s"]/port-table' % (c.base_url, dpid)
        c.rest.get(url)
        data = c.rest.content()
        for i in range(0,len(data)):
          if ((data[i]["lag-id"]) == 0):
              helpers.test_failure("Lag-Id for the edge interface (switch=%s,interface=%s) is showing 0" % (dpid, data[i]["port-num"]))
              return False
        helpers.log("Proper Lag-Id created for All edge Interfaces")         
        

          
 

        
        

