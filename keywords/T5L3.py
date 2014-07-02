import autobot.helpers as helpers
import autobot.restclient as restclient
import autobot.test as test
import re


class T5L3(object):

    def __init__(self):
        pass

    def rest_add_vns_ip(self, tenant, vns, ipaddr, netmask, private=False):
        '''Create vns router interface via command "logical-router vns interface"

            Input:
                `tenant`        tenant name
                `vns`           vns interface name which must be similar to VNS
                `ipaddr`        interface ip address
                `netmask`       vns subnet mask
                `private`        true or false
            POST http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X1%22%5D/ip-subnet {"ip-cidr": "10.10.0.1/24", "private": false}
        REST-POST: POST http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X2%22%5D/ip-subnet {"ip-cidr": "10.10.111.1/24", "private": false}

            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns = %s ipaddr = %s netmask = %s private = %s " % (tenant, vns, ipaddr, netmask, private))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/ip-subnet' % (tenant, vns)
        ip_addr = ipaddr + "/" + netmask
        try:
            # c.rest.patch(url, {"ip-cidr": str(ip_addr)})
            # c.rest.post(url, {"segment": vns, "ip-cidr": str(ip_addr), "active": True})
#            c.rest.put(url, {"segment": vns, "ip-cidr": str(ip_addr)})
            c.rest.post(url, {"ip-cidr": str(ip_addr), "private": private})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_delete_vns_ip(self, tenant, vnsname, ipaddr, netmask):
        '''Create vns router interface via command "logical-router vns interface"

            Input:
                `tenant`        tenant name
                `vnsname`       vns interface name which must be similar to VNS
                `ipaddr`        interface ip address
                `netmask`       vns subnet mask
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X1%22%5D/ip-subnet/ip-cidr {}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X1%22%5D/ip-subnet/ip-cidr done 0:00:00.002873
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X1%22%5D/ip-subnet/private {}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X1%22%5D/ip-subnet/private done 0:00:00.002920
            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')
        helpers.test_log("Input arguments: tenant = %s vns = %s ipaddr = %s netmask = %s " % (tenant, vnsname, ipaddr, netmask))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/ip-subnet/ip-cidr' % (tenant, vnsname)
        ip_addr = ipaddr + "/" + netmask
        try:
            c.rest.delete(url, {})
        except:
            return False
            # helpers.test_failure(c.rest.error())
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True


    def rest_enable_router_intf(self, tenant, tenantIntf):
        '''Create vns router interface via command "logical-router vns interface"

            Input:
                `tenant`        tenant name
                `vnsname`       vns interface name which must be similar to VNS
                `ipaddr`        interface ip address
                `netmask`       vns subnet mask
                DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="X"]/logical-router/tenant-interfaces[tenant-name="system"]/shutdown {}
                DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="system"]/logical-router/tenant-interfaces[tenant-name="X"]/shutdown {}
                Return: true if configuration is successful, false otherwise
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s  " % (tenant, tenantIntf))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/tenant-interfaces[tenant-name="%s"]/shutdown' % (tenant, tenantIntf)
        try:
            c.rest.delete(url, {})
        except:
            return False
            # helpers.test_failure(c.rest.error())
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_disable_router_intf(self, tenant, tenantIntf):
        '''Disable logical router tenant interface"

            Input:
                `tenant`        tenant name
                `vnsname`       vns interface name which must be similar to VNS
                `ipaddr`        interface ip address
                `netmask`       vns subnet mask
                PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="system"]/logical-router/tenant-interfaces[tenant-name="X"] {"shutdown": true}
                PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="X"]/logical-router/tenant-interfaces[tenant-name="system"] {"shutdown": true}
                Return: true if configuration is successful, false otherwise
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s  " % (tenant, tenantIntf))
        url = 'api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/tenant-interfaces[tenant-name="%s"]' % (tenant, tenantIntf)
        try:
            c.rest.patch(url, {"shutdown": True})
        except:
            return False
            # helpers.test_failure(c.rest.error())
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True


    def rest_enable_router_segment_intf(self, tenant, vnsname):
        '''Create vns router interface via command "logical-router vns interface"

            Input:
                `tenant`        tenant name
                `vnsname`       vns interface name which must be similar to VNS
                `ipaddr`        interface ip address
                `netmask`       vns subnet mask
                DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="X"]/logical-router/segment-interface[segment="X2"]/shutdown {}
                Return: true if configuration is successful, false otherwise
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s  " % (tenant, vnsname))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/shutdown' % (tenant, vnsname)
        try:
            c.rest.delete(url, {})
        except:
            return False
            # helpers.test_failure(c.rest.error())
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_disable_router_segment_intf(self, tenant, vnsname):
        '''Disable logical router segment interface
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="X"]/logical-router/segment-interface[segment="X2"] {"shutdown": true}
            PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="X"]/logical-router/segment-interface[segment="X1"] {"shutdown": true}
         '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s  " % (tenant, vnsname))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]' % (tenant, vnsname)
        try:
            c.rest.patch(url, {"shutdown": True})
        except:
            return False
            # helpers.test_failure(c.rest.error())
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True


    def rest_add_tenant_routers_intf_to_system(self, tenant):
        '''Attach tenant router to system tenant"

            Input:
                `tenant`        tenant name

            Return: true if configuration is successful, false otherwise
REST-POST: PUT http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="system"]/logical-router/tenant-interfaces[tenant-name="A"] {"tenant-name": "A"}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="system"]/logical-router/tenant-interfaces[tenant-name="A"] reply: ""

        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s " % (tenant))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="system"]/logical-router/tenant-interfaces[tenant-name="%s"]' % (tenant)
        try:
            # c.rest.post(url, {"tenant-name": tenant, "active": True})
            c.rest.put(url, {"tenant-name": tenant})

        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_delete_tenant_routers_intf_to_system(self, tenant):
        '''detach tenant router to system tenant"

            Input:
                `tenant`        tenant name

            Return: true if configuration is successful, false otherwise
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="system"]/logical-router/tenant-interfaces[tenant-name="A"] {}
       '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s " % (tenant))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="system"]/logical-router/tenant-interfaces[tenant-name="%s"]' % (tenant)
        try:
            c.rest.delete(url, {})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_add_system_intf_to_tenant_routers(self, tenant):
        '''Attach system router to tenant router"

            Input:
                `tenant`        tenant name

            Return: true if configuration is successful, false otherwise

        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s " % (tenant))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/tenant-interfaces[tenant-name="system"]' % (tenant)
        try:
            # c.rest.post(url, {"tenant-name": "system", "active": True})
            c.rest.put(url, {"tenant-name": "system"})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_delete_system_intf_to_tenant_routers(self, tenant):
        '''detach system router from tenant router"

            Input:
                `tenant`        tenant name
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="B"]/logical-router/tenant-interfaces[tenant-name="system"] {}
            Return: true if configuration is successful, false otherwise

        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s " % (tenant))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/tenant-interfaces[tenant-name="system"]' % (tenant)
        try:
            c.rest.delete(url, {})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_add_static_routes(self, tenant, dstroute, nexthop=None):
        '''Add static routes to tenant router"

            Input:
                `tenant`          tenant name
                `dstroute`        destination subnet
                `nexthop`         nexthop IP address or nexthop tenant name or nexthop ecmp group name. e.g. of nexthop input is {"ip-address": "10.10.10.1"} or {"tenant-name": "B"} or {"ecmp-group-name": "e3"}
                more specific example REST add static routes(A, 10.10.11.0/24, {"ecmp-group-name": "e2"})

            Return: true if configuration is successful, false otherwise
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="X"]/logical-router/routes[dest-ip-subnet="10.10.0.0/16"] {"next-hop": {"tenant-name": "system"}, "dest-ip-subnet": "10.10.0.0/16"}
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="X"]/logical-router/routes[dest-ip-subnet="10.192.0.0/16"] {"dest-ip-subnet": "10.192.0.0/16"}

        '''

        t = test.Test()
        c = t.controller('master')
        helpers.test_log("Input arguments: tenant = %s dstroute = %s nexthop = %s " % (tenant, dstroute, nexthop))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/routes' % (tenant)

        if nexthop is not None:
            try:
                nexthop_dict = helpers.from_json(nexthop)
                c.rest.post(url, {"dest-ip-subnet": dstroute, "next-hop": nexthop_dict})
            except:
                helpers.test_failure(c.rest.error())
            else:
                helpers.test_log("Output: %s" % c.rest.result_json())
                return c.rest.content()
        else:
            try:
                c.rest.post(url, {"dest-ip-subnet": dstroute})
            except:
                helpers.test_failure(c.rest.error())
            else:
                helpers.test_log("Output: %s" % c.rest.result_json())
                return c.rest.content()


    def rest_delete_static_routes(self, tenant, dstroute):
        '''Add static routes to tenant router"

            Input:
                `tenant`          tenant name
                `dstroute`        destination subnet
                Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s dstroute = %s " % (tenant, dstroute))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/routes[dest-ip-subnet="%s"]' % (tenant, dstroute)
        try:
            # c.rest.delete(url, {"dest-ip-subnet": dstroute})
            c.rest.delete(url, {})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_show_endpoints(self):
        t = test.Test()
        c = t.controller('master')
        url = '/api/v1/data/controller/applications/bcf/info/endpoint-manager/endpoint'
        c.rest.get(url)
        helpers.log("Output: %s" % c.rest.result_json())
        data = c.rest.content()
        return data

    def rest_show_endpoints_name(self, endpointname):
        t = test.Test()
        c = t.controller('master')
        endptname = "%5Bname%3D%22" + endpointname + "%22%5D"
        url = '/api/v1/data/controller/applications/bcf/info/endpoint-manager/endpoint%s' % (endptname)
        c.rest.get(url)
        helpers.log("Output: %s" % c.rest.result_json())
        data = c.rest.content()
        return data

    def rest_show_endpoints_mac(self, mac):
        '''
        REST-SIMPLE: GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/endpoint-manager/endpoint%5Bmac%3D%2290%3Ae2%3Aba%3A4e%3Abb%3A90%22%5D

        %5Bmac%3D%2200%3A00%3A00%3A00%3A00%3A01%22%5D
        '''
        t = test.Test()
        c = t.controller('master')

#        str1 = mac.replace(":", "%3A")
#        str3 = str2.replace("\n", "")
#        str4 = str3.replace("\r", "")
#        str1 = str4.replace(" ", "")
#        mac_addr = "%5Bmac%3D%22" + str1 + "%22%5D"
#        url = '/api/v1/data/controller/applications/bcf/info/endpoint-manager/endpoints%s' % (mac_addr)
        url = '/api/v1/data/controller/applications/bcf/info/endpoint-manager/endpoint[mac="%s"]' % (mac)

        c.rest.get(url)
        helpers.log("Output: %s" % c.rest.result_json())
        data = c.rest.content()
#        match = re.search(r'None', data, re.S)
#       if match:
#          return ""
#        else:
#            return data
        helpers.log("data: %s" % data)
        return data

    def rest_count_endpoints_mac(self):
        data = self.rest_show_endpoints()
        return len(data)

    def rest_add_ecmp_group(self, tenant, ecmpgroup):
        '''Add ecmp groups aks gateway pool to tenant"

            Input:
                `tenant`          tenant name
                `ecmpgroup`        pool or ecmp groups name
            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s ecmpgroup = %s" % (tenant, ecmpgroup))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/ecmp-groups' % (tenant)
        try:
            c.rest.post(url, {"name": ecmpgroup})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_add_gw_pool_nexthop(self, tenant, ecmpgroup, nexthop):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"

            Input:
                `tenant`         tenant name
                `ecmpgroup`      pool or ecmp groups name
                `nexthop`        nexthop IP address
            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s ecmpgroup = %s nexthop = %s" % (tenant, ecmpgroup, nexthop))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/ecmp-groups[name="%s"]/ip-addresses' % (tenant, ecmpgroup)
        try:
#            c.rest.put(url, {"ip-address": nexthop})
            c.rest.post(url, {"ip-address": nexthop})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()



    def rest_add_endpoint_ip(self, tenant, vnsname, endpointname, ipaddr):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"

            Input:
                `tenant`          tenant name
                `vnsname`         vns name
                `endpointname`    endpoint name
                `ipaddr`          host IP address
            Return: true if configuration is successful, false otherwise
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="A"]/segment[name="A1"]/endpoint[name="H1"] {"name": "H1"}

        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s ipaddress = %s" % (tenant, vnsname, endpointname, ipaddr))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]' % (tenant, vnsname, endpointname)
        try:
            c.rest.patch(url, {"ip-address": ipaddr})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_delete_endpoint_ip(self, tenant, vnsname, endpointname, ipaddr):
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s ip address = %s" % (tenant, vnsname, endpointname, ipaddr))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]/ip-address' % (tenant, vnsname, endpointname)
        try:
            c.rest.delete(url, {})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_add_endpoint_mac(self, tenant, vnsname, endpointname, mac):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"

            Input:
                `tenant`          tenant name
                `vnsname`         vns name
                `endpointname`    endpoint name
                `mac`          host mac address
            Return: true if configuration is successful, false otherwise
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="A"]/segment[name="A1"]/endpoint[name="H1"] {"name": "H1"}

        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s mac address = %s" % (tenant, vnsname, endpointname, mac))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]' % (tenant, vnsname, endpointname)
        try:
            c.rest.patch(url, {"mac": mac})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_delete_endpoint_mac(self, tenant, vnsname, endpointname, mac):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"

            Input:
                `tenant`          tenant name
                `vnsname`         vns name
                `endpointname`    endpoint name
                `mac`          host mac address
            Return: true if configuration is successful, false otherwise
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="A"]/segment[name="A1"]/endpoint[name="H1"] {"name": "H1"}
            DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="A"]/segment[name="A1"]/endpoint[name="bm0"]/mac {}

        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s mac address = %s" % (tenant, vnsname, endpointname, mac))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]/mac' % (tenant, vnsname, endpointname)
        try:
            c.rest.delete(url, {})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_add_endpoint_portgroup_attachment(self, tenant, vnsname, endpointname, portgroupname, vlan):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"

            Input:
                `tenant`          tenant name
                `vnsname`         vns name
                `endpointname`    endpoint name
                `portgroupname`   port-group name
                `vlan`            vlan id or -1 for untagged
            Return: true if configuration is successful, false otherwise
            curl -gX PATCH -H 'Cookie: session_cookie=RKIUFOl07Dqiz10nXJcbquvUcWVJ3xYM' -d '{"port-group-name": "leaf4", "vlan": -1}' 'localhost:8080/api/v1/data/controller/applications/bcf/tenant[name="B"]/segment[name="B1"]/endpoints[name="B1-H1"]/attachment-point'
            REST-POST: PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point {"vlan": 200, "port-group": "leaf0-pc1"}
            REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point done 0:00:00.005086

        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s portgroup = %s vlan = %s" % (tenant, vnsname, endpointname, portgroupname, vlan))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]/attachment-point' % (tenant, vnsname, endpointname)
        try:
            c.rest.post(url, {"vlan": vlan, "port-group": portgroupname})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()




    def rest_delete_endpoint_portgroup_attachment(self, tenant, vnsname, endpointname, portgroupname, vlan):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"

            Input:
                `tenant`          tenant name
                `vnsname`         vns name
                `endpointname`    endpoint name
                `portgroupname`   port-group name
                `vlan`            vlan id or -1 for untagged
            Return: true if configuration is successful, false otherwise
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point {"vlan": 200, "port-group": "leaf0-pc1"}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point done 0:00:00.004887
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point {"vlan": 200, "port-group": "leaf0-pc1"}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point done 0:00:00.002376
      '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s portgroup = %s vlan = %s" % (tenant, vnsname, endpointname, portgroupname, vlan))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]/attachment-point' % (tenant, vnsname, endpointname)
        try:
            c.rest.delete(url, {"vlan": vlan, "port-group": portgroupname})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()



    def rest_add_endpoint_switch_attachment(self, tenant, vnsname, endpointname, switchname, switchinterface, vlan):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"
            Input:
                `tenant`          tenant name
                `vnsname`         vns name
                `endpointname`    endpoint name
                `switchname`       name of switch
                `switchinterface`    switch port
                `vlan`            vlan id or -1 for untagged
            Return: true if configuration is successful, false otherwise
     REST-POST: PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point {"interface": "ethernet22", "switch": "leaf0-a", "vlan": 10}
    REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point done 0:00:00.004528
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s switchname = %s switch interface = %s vlan = %s" % (tenant, vnsname, endpointname, switchname, switchinterface, vlan))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]/attachment-point' % (tenant, vnsname, endpointname)
        try:
            c.rest.post(url, {"interface": switchinterface, "switch": switchname, "vlan": vlan})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_delete_endpoint_switch_attachment(self, tenant, vnsname, endpointname, switchname, switchinterface, vlan):
        '''Add nexthop to ecmp groups aks gateway pool in tenant"

            Input:
                `tenant`          tenant name
                `vnsname`         vns name
                `endpointname`    endpoint name
                `switchname`       name of switch
                `switchinterface`    switch port
                `vlan`            vlan id or -1 for untagged
            Return: true if configuration is successful, false otherwise
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point {"interface": "ethernet22", "switch": "leaf0-a", "vlan": 10}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point done 0:00:00.010011
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point {"interface": "ethernet22", "switch": "leaf0-a", "vlan": 10}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point done 0:00:00.003425
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/segment%5Bname%3D%22X1%22%5D/endpoint%5Bname%3D%22H1%22%5D/attachment-point {"interface": "ethernet22", "switch": "leaf0-a", "vlan": 10}

       '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vnsname = %s endpointname = %s switchname = %s switch interface = %s vlan = %s" % (tenant, vnsname, endpointname, switchname, switchinterface, vlan))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/endpoint[name="%s"]/attachment-point' % (tenant, vnsname, endpointname)
        try:
            c.rest.delete(url, {"interface": switchinterface, "switch": switchname, "vlan": vlan})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_add_dhcp_relay(self, tenant, vnsname, dhcpserverip):
        '''Create dhcp server on tenant VNS"

            Input:
                `tenant`          tenant name
                `vnsname`         name of vns interface
                `dhcpserverip`    IP address of dhcp server
            Return: true if configuration is successful, false otherwise
REST-POST: PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] {"dhcp-server-ip": "10.2.1.1"}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] reply:
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns name = %s relay-ip = %s" % (tenant, vnsname, dhcpserverip))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/dhcp-relay' % (tenant, vnsname)
        try:
            c.rest.patch(url, {"dhcp-server-ip": dhcpserverip})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_enable_dhcp_relay(self, tenant, vnsname):
        '''Enable dhcp relay on tenant VNS"

            Input:
                `tenant`          tenant name
                `vnsname`         name of vns interface
            Return: true if configuration is successful, false otherwise
REST-POST: PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"]/dhcp-relay {"dhcp-relay-enable": true}
<<<<<<< HEAD
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] reply: ""
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] reply: ""
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns name = %s " % (tenant, vnsname))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/dhcp-relay' % (tenant, vnsname)
        try:
            c.rest.patch(url, {"dhcp-relay-enable": True})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_disable_dhcp_relay(self, tenant, vnsname):
        '''Enable dhcp relay on tenant VNS"

            Input:
                `tenant`          tenant name
                `vnsname`         name of vns interface
            Return: true if configuration is successful, false otherwise
REST-POST: PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] {"dhcp-relay-enable": true}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] reply: ""
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns name = %s " % (tenant, vnsname))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/dhcp-relay' % (tenant, vnsname)
        try:
            c.rest.patch(url, {"dhcp-relay-enable": False})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_add_dhcprelay_circuitid(self, tenant, vnsname, circuitid):
        '''Set dhcp relay circuit id"

            Input:
                `tenant`          tenant name
                `vnsname`         name of vns interface
                `circuitid`      Circuit id, can be a string upto 15 characters
            Return: true if configuration is successful, false otherwise
REST-POST: PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] {"dhcp-circuit-id": "this is a test"}
<<<<<<< HEAD
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="C"]/logical-router/segment-interface[segment="C1"] reply: ""
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns name = %s circuit id = %s" % (tenant, vnsname, circuitid))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/dhcp-relay' % (tenant, vnsname)
        try:
            c.rest.patch(url, {"dhcp-circuit-id": circuitid})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()


    def rest_delete_dhcp_relay(self, tenant, vnsname, dhcpserverip, dhcpcircuitid=None):
        '''Delete dhcp server "

            Input:
                `tenant`          tenant name
                `vnsname`         name of vns interface
                `dhcpserverip`       DHCP server IP, can be anything since it will delete everything under the vns
            Return: true if configuration is successful, false otherwise
REST-POST: PATCH http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22Z%22%5D/logical-router/segment-interface%5Bsegment%3D%22Z1%22%5D/dhcp-relay {"dhcp-relay-enable": false}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22Z%22%5D/logical-router/segment-interface%5Bsegment%3D%22Z1%22%5D/dhcp-relay done 0:00:00.008562
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22Z%22%5D/logical-router/segment-interface%5Bsegment%3D%22Z1%22%5D/dhcp-relay/dhcp-server-ip {}
REST-POST: http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22Z%22%5D/logical-router/segment-interface%5Bsegment%3D%22Z1%22%5D/dhcp-relay/dhcp-server-ip done 0:00:00.008065
REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22Z%22%5D/logical-router/segment-interface%5Bsegment%3D%22Z1%22%5D/dhcp-relay/dhcp-relay-enable {}

REST-POST: DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="B"]/logical-router/segment-interface[segment="B1"]/dhcp-server-ip {}
<<<<<<< HEAD

        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns name = %s dhcp server ip = %s" % (tenant, vnsname, dhcpserverip))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/dhcp-relay/dhcp-server-ip' % (tenant, vnsname)
        try:

#            self.rest_disable_dhcp_relay(tenant, vnsname)
            c.rest.delete(url, {})
        except:
            helpers.test_failure(c.rest.error())
        else:
            helpers.test_log("Output: %s" % c.rest.result_json())
            return c.rest.content()

    def rest_show_forwarding_switch_l3_host_route(self, switch):
        '''
    GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/switch%5Bswitch-name%3D%22leaf0a%22%5D/l3-host-route-table
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: switch = %s " % (switch))
        url = '/api/v1/data/controller/applications/bcf/info/forwarding/network/switch[switch-name="%s"]/l3-host-route-table' % (switch)
        try:
            c.rest.get(url)
        except:
            helpers.test_failure(c.rest.error())
        else:
            return c.rest.content()

    def rest_show_forwarding_switch_l3_cidr_route(self, switch):
        '''
    GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/switch%5Bswitch-name%3D%22leaf0a%22%5D/l3-cidr-route-table
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: switch = %s " % (switch))
        url = '/api/v1/data/controller/applications/bcf/info/forwarding/network/switch[switch-name="%s"]/l3-cidr-route-table' % (switch)
        try:
            c.rest.get(url)
        except:
            helpers.test_failure(c.rest.error())
        else:
            return c.rest.content()

    def rest_show_l3_cidr_table(self):
        '''
        GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/global/l3-cidr-table
        GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/l3-cidr-table
        '''
        t = test.Test()
        c = t.controller('master')
        url = '/api/v1/data/controller/applications/bcf/info/forwarding/network/global/l3-cidr-table'
        try:
            c.rest.get(url)
        except:
            helpers.test_failure(c.rest.error())
        else:
            return c.rest.content()

    def rest_show_l3_host_table(self):
        '''
        GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/global/l3-host-table

        GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/l3-host-table
        '''
        t = test.Test()
        c = t.controller('master')

        url = '/api/v1/data/controller/applications/bcf/info/forwarding/network/global/l3-host-table'
        try:
            c.rest.get(url)
        except:
            helpers.test_failure(c.rest.error())
        else:
            return c.rest.content()


    def rest_add_policy(self, tenant, polname):
        '''Create a tenant policy

            Input:
                `tenant`        tenant name
                `polname`        name of policy

            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s policy name = %s  " % (tenant, polname))

        # url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface' % (tenant)
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/policy-lists[name="%s"]' % (tenant, polname)
        try:
            c.rest.post(url, {"name": polname})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_delete_policy(self, tenant, polname):
        ''' Deleting a tenant policy
            Input:
                    'tenant'        tenant name
                    'polname'        policy name to be deleted

            Return: treu if deletetion successful, else false
        '''
        t = test.Test()
        c = t.controller('master')

        helpers.test_log("To be deleted: Input arguments: tenant = %s policy name = %s  " % (tenant, polname))

        # url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface' % (tenant)
        # url_delete = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/policy-lists[name="%s"] {}'
        url_delete_polname = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/policy-lists[name="%s"]' % (tenant, polname)
        try:
            c.rest.delete(url_delete_polname, {})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True


    def rest_apply_policy_on_vns(self, tenant, vnsname, polname):
        '''Create a tenant policy

            Input:
                `tenant`        tenant name
                `vnsname`        vns name
                `polname`        name of policy

            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns name = %s policy name = %s  " % (tenant, vnsname, polname))

        # url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface' % (tenant)
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router' % (tenant)
        try:
            c.rest.patch(url, {"inbound-policy-name": polname})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_remove_policy_on_vns(self, tenant, vnsname, polname):
        '''Remove a tenant policy

            Input:
                `tenant`        tenant name
                `vnsname`        vns name
                `polname`        name of policy

            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns name = %s policy name = %s  " % (tenant, vnsname, polname))

        # url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface' % (tenant)
        url_remove_policy = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/inbound-policy-name' % (tenant)
        try:
            c.rest.delete(url_remove_policy, {})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True


    def rest_apply_policy_on_tenant(self, tenant, polname, intf="system"):
        '''Create a tenant policy

            Input:
                `tenant`        tenant name
                `vnsname`        vns name
                `polname`        name of policy

            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s interface = %s policy name = %s  " % (tenant, intf, polname))

        # url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface' % (tenant)
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router' % (tenant)
        try:
            c.rest.patch(url, {"inbound-policy-name": polname})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_remove_policy_on_tenant(self, tenant, polname, intf="system"):
        '''Remove a tenant policy

            Input:
                `tenant`        tenant name
                `vnsname`        vns name
                `polname`        name of policy

            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')
        helpers.test_log("Input arguments: tenant = %s interface = %s policy name = %s  " % (tenant, intf, polname))

        # url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface' % (tenant)
        url_remove_policy = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/inbound-policy-name' % (tenant)
        try:
            c.rest.delete(url_remove_policy, {})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True


    def rest_add_policy_item(self, tenant, polname, seqnum, polaction, srcdata, dstdata):
        '''add a policy item

            Input:
                `tenant`        tenant name
                `polname`       name of policy
                `seqnum`        sequence number
                `src-data`      Source policy data
                `dst-data`      Destination policy data
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="A"]/logical-router/policy-lists[name="p2"]/rules[seq=10] {"src": {"segment": "A1", "tenant-name": "A"}, "seq": 10, "dst": {"cidr": "10.1.1.1/24"}, "ip-proto": 6, "action": "next-hop", "next-hop": {"ip-address": "10.1.1.1"}}
            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s policy name = %s sequence number = %s src-data = %s dst-data = %s action = %s " % (tenant, polname, str(seqnum), str(srcdata), str(dstdata), polaction))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/policy-lists[name="%s"]/rules[seq=%s]' % (tenant, polname, seqnum)
        try:
            c.rest.put(url, {"src":srcdata, "seq": str(seqnum), "dst":dstdata, "action": str(polaction)})

        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_add_router_intf(self, tenant, vns):
        '''Create vns router interface via command "logical-router vns interface"

            Input:
                `tenant`        tenant name
                `vns`           vns interface name which must be similar to VNS
            PUT http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X1%22%5D {"segment": "X1"}
            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns = %s " % (tenant, vns))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]' % (tenant, vns)
        try:
            c.rest.put(url, {"segment": vns})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True

    def rest_del_router_intf(self, tenant, vns):
        '''Create vns router interface via command "logical-router vns interface"

            Input:
                `tenant`        tenant name
                `vns`           vns interface name which must be similar to VNS
             DELETE http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant%5Bname%3D%22X%22%5D/logical-router/segment-interface%5Bsegment%3D%22X1%22%5D {}
            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')

        helpers.test_log("Input arguments: tenant = %s vns = %s " % (tenant, vns))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/segment-interface[segment="%s"]' % (tenant, vns)
        try:
            c.rest.delete(url, {})
        except:
            # helpers.test_failure(c.rest.error())
            return False
        else:
            # helpers.test_log("Output: %s" % c.rest.result_json())
            # return c.rest.content()
            return True




    def rest_add_policy_item_example(self, **kwargs):
        '''add a policy item

            Input:
                `tenant`        tenant name
                `polname`       name of policy
                `seqnum`        sequence number
                `src-data`      Source policy data
                `dst-data`      Destination policy data
            http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/tenant[name="A"]/logical-router/policy-lists[name="p2"]/rules[seq=10] {"src": {"segment": "A1", "tenant-name": "A"}, "seq": 10, "dst": {"cidr": "10.1.1.1/24"}, "ip-proto": 6, "action": "next-hop", "next-hop": {"ip-address": "10.1.1.1"}}
            Return: true if configuration is successful, false otherwise
        '''

        t = test.Test()
        c = t.controller('master')
        # src_mac = kwargs.get('src_mac', '00:11:23:00:00:01')
        seqnum = kwargs.get('seqnum')
        action = kwargs.get('action')
        srcdata = kwargs.get('srcdata', None)
        dstdata = kwargs.get('dstdata', None)
        ip_proto = kwargs.get('proto', None)
        next_hop = kwargs.get('next-hop', None)
        tenant = kwargs.get('tenant', None)
        polname = kwargs.get('polname', None)
        #log = kwargs.get('log', None)
        segment = kwargs.get('segment-interface', None)

        if (tenant is None or polname is None or seqnum is None):
            helpers.test_failure("Tenant and Polname are Null")



        helpers.test_log("Input arguments: tenant = %s" \
                         " policy name = %s" \
                         " sequence number = %s " \
                         " src-data = %s " \
                         " dst-data = %s " \
                         " action = %s " \
                         " ip-proto = %s " \
                         " segment-interface = %s" \
                         " next-hop = %s " % (tenant, polname, str(seqnum), str(srcdata), str(dstdata), action, ip_proto, segment, next_hop))
        url = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/logical-router/policy-lists[name="%s"]/rules[seq=%s]' % (tenant, polname, seqnum)
        if (next_hop is None and ip_proto is None):
            if (srcdata is not None and dstdata is not None):
                data = {"src":srcdata, "seq": str(seqnum), "dst":dstdata, "action": str(action)}
                try:
                    helpers.log("**** url: %s" % url)
                    c.rest.put(url, data)
                except:
                    helpers.log("Error happend Output: %s " % c.rest.result_json())
                    return False
                else:
                    helpers.test_log("Output: %s" % c.rest.result_json())
                    return c.rest.content()
                    return True

            if (srcdata is None):
                data = {"seq": str(seqnum), "dst":dstdata, "action": str(action)}
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None):
                data = {"src":srcdata, "seq": str(seqnum), "action": str(action)}
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None and srcdata is None):
                data = { "seq": str(seqnum), "action": str(action)}
                try:
                    c.rest.put(url,)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

        if (next_hop is None and ip_proto is not None):
            if (srcdata is not None and dstdata is not None):
                data = {"src":srcdata, "seq": str(seqnum), "dst":dstdata, "action": str(action), "ip-proto":ip_proto}
                try:
                    c.rest.put(url, data)

                except:
                        # helpers.test_failure(c.rest.error())
                        return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (srcdata is None):
                data = {"seq": str(seqnum), "dst":dstdata, "action": str(action), "ip-proto":ip_proto}
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None):
                data = {"src":srcdata, "seq": str(seqnum), "action": str(action), "ip-proto":ip_proto}
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None and srcdata is None):
                data = { "seq": str(seqnum), "action": str(action), "ip-proto":ip_proto}
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

        if (next_hop is not None and ip_proto is not None and action is "next-hop"):
            if (srcdata is not None and dstdata is not None):
                if (segment is not None):
                    data = {"src":srcdata, "seq": str(seqnum), "dst":dstdata, "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = {"src":srcdata, "seq": str(seqnum), "dst":dstdata, "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop}
                
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (srcdata is None):
                if (segment is not None):
                    data = {"seq": str(seqnum), "dst":dstdata, "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = {"seq": str(seqnum), "dst":dstdata, "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop}
                
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None):
                if (segment is not None):
                    data = {"src":srcdata, "seq": str(seqnum), "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = {"src":srcdata, "seq": str(seqnum), "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop}
                
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None and srcdata is None):
                if (segment is not None):
                    data = { "seq": str(seqnum), "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = { "seq": str(seqnum), "action": str(action), "ip-proto":ip_proto, "next-hop":next_hop}
                    
                try:
                    c.rest.put(url,)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

        if (next_hop is not None and ip_proto is None and action is "next-hop"):
            if (srcdata is not None and dstdata is not None):
                if (segment is not None):
                    data = {"src":srcdata, "seq": str(seqnum), "dst":dstdata, "action": str(action), "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = {"src":srcdata, "seq": str(seqnum), "dst":dstdata, "action": str(action), "next-hop":next_hop}
                    
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (srcdata is None):
                if (segment is not None):
                    data = {"seq": str(seqnum), "dst":dstdata, "action": str(action), "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = {"seq": str(seqnum), "dst":dstdata, "action": str(action), "next-hop":next_hop}
                    
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None):
                if (segment is not None):
                    data = {"src":srcdata, "seq": str(seqnum), "action": str(action), "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = {"src":srcdata, "seq": str(seqnum), "action": str(action), "next-hop":next_hop}
                    
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

            if (dstdata is None and srcdata is None):
                if (segment is not None):
                    data = { "seq": str(seqnum), "action": str(action), "next-hop":next_hop, "segment-interface":segment}
                else:
                    data = { "seq": str(seqnum), "action": str(action), "next-hop":next_hop}
                    
                try:
                    c.rest.put(url, data)

                except:
                    # helpers.test_failure(c.rest.error())
                    return False
                else:
                    # helpers.test_log("Output: %s" % c.rest.result_json())
                    # return c.rest.content()
                    return True

    def rest_show_forwarding_dhcp_table(self):
        '''
       GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/global/dhcp-table
     '''
        t = test.Test()
        c = t.controller('master')
        url = '/api/v1/data/controller/applications/bcf/info/forwarding/network/global/dhcp-table'
        try:
            c.rest.get(url)
        except:
            helpers.test_failure(c.rest.error())
        else:
            return c.rest.content()

    def rest_show_forwarding_ecmp_table(self):
        '''
        GET http://127.0.0.1:8080/api/v1/data/controller/applications/bcf/info/forwarding/network/global/ecmp-table

     '''
        t = test.Test()
        c = t.controller('master')
        url = '/api/v1/data/controller/applications/bcf/info/forwarding/network/global/ecmp-table'
        try:
            c.rest.get(url)
        except:
            helpers.test_failure(c.rest.error())
        else:
            return c.rest.content()
