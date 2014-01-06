import autobot.helpers as helpers
import autobot.test as test
import subprocess
from BigTapCommonShow import BigTapCommonShow
from Exscript.protocols import SSH2
from Exscript import Account, Host

class BsnCommonShow(object):

    def __init__(self):
        t = test.Test()
        self.btc=BigTapCommonShow()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8082
        else:
            c = t.controller('c2')
            c.http_port=8082
        url='http://%s:%s/auth/login' % (c.ip,c.http_port)   
        helpers.log("url: %s" % url)
        result = c.rest.post(url, {"user":"admin", "password":"adminadmin"})
        helpers.log("result: %s" % helpers.to_json(result))
        session_cookie = result['content']['session_cookie']
        c.rest.set_session_cookie(session_cookie)


#Generic Sleep Function
    def sleepnow(self,intTime):
        helpers.sleep(float(intTime))

#   Objective: Execute CLI command "show version"
#   Input: N/A
#   Return Value:  Version String
    def rest_show_version(self):
        t = test.Test()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8000
        else:
            c = t.controller('c2')
            c.http_port=8000
        url='http://%s:%s/rest/v1/system/version' % (c.ip,c.http_port)
        c.rest.get(url)
        content = c.rest.content()
        helpers.log("Output: %s" % content[0]['controller'])
        return content[0]['controller']


#   Objective: Return Current Controller Role viz. Master/Slave
#   Input: N/A
#   Return Value:  Current Controller Role viz. Master/Slave
    def rest_ha_role(self):
        t = test.Test()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8000
        else:
            c = t.controller('c2')
            c.http_port=8000
        url = '%s/system/ha/role'  % (c.base_url)
        c.rest.get(url)
        helpers.test_log("Ouput: %s" % c.rest.result_json())
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())
        content = c.rest.content()
        return content['role']

#   Objective: Return Current Controller ID
#   Input: N/A
#   Return Value:  Return Current Controller ID
    def rest_controller_id(self):
        t = test.Test()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8000
        else:
            c = t.controller('c2')
            c.http_port=8000
        url='http://%s:%s/rest/v1/system/controller' % (c.ip,c.http_port)
        c.rest.get(url)
        content = c.rest.content()
        helpers.log("Output: %s" % content['id'])
        return content['id']

#   Objective: Execute CLI Command "show snmp"
#   Input: N/A
#   Return Value:  Return a dictionary of SNMP related values
    def rest_snmp_show(self):
        t = test.Test()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8000
        else:
            c = t.controller('c2')
            c.http_port=8000
        url='http://%s:%s/rest/v1/model/snmp-server-config/' % (c.ip,c.http_port)
        c.rest.get(url)
        content = c.rest.content()
        helpers.log("Output: %s" % content)
        return content
    
#   Objective: Given a dictionary, return the value for a particular key
#   Input: Dictionary, index and required key.
#   Return Value:  return the value for a particular key
    def rest_verify_dict_key(self,content,index,key):
        return content[int(index)][str(key)]
    
#   Objective: Execute SNMP Walk from local machine for a particular SNMP OID
#   Input: SNMP Community and OID 
#   Return Value:  return the SNMP Walk O/P
    def rest_snmp_get(self,snmpCommunity,snmpOID):
        t = test.Test()
        c = t.controller()
        url="/usr/bin/snmpwalk -v2c -c %s %s %s" % (str(snmpCommunity),c.ip,str(snmpOID))
        returnVal = subprocess.Popen([url], stdout=subprocess.PIPE, shell=True)
        (out, err) = returnVal.communicate()
        helpers.log("URL: %s Output: %s" % (url, out))
        return out
    
#   Objective: Execute snmpgetnext from local machine for a particular SNMP OID
#   Input: SNMP Community and OID 
#   Return Value:  return the SNMP Walk O/P
    def rest_snmp_getnext(self,snmpCommunity,snmpOID):
        t = test.Test()
        c = t.controller()
        url="/usr/bin/snmpgetnext -v2c -c %s %s %s" % (str(snmpCommunity),c.ip,str(snmpOID))
        returnVal = subprocess.Popen([url], stdout=subprocess.PIPE, shell=True)
        (out, err) = returnVal.communicate()
        helpers.log("URL: %s Output: %s" % (url, out))
        return out
    
    
#   Objective: Execute snmpgetnext from local machine for a particular SNMP OID
#   Input: SNMP Community and OID 
#   Return Value:  return the SNMP Walk O/P
    def rest_snmp_cmd(self,snmp_cmd,snmpOptions,snmpCommunity,snmpOID):
        t = test.Test()
        c = t.controller()
        if snmpOptions == "None" or snmpOptions == "none":
                snmpOptions =" "
        url="/usr/bin/%s -v2c %s -c %s %s %s" % (str(snmp_cmd),str(snmpOptions),str(snmpCommunity),c.ip,str(snmpOID))
        returnVal = subprocess.Popen([url], stdout=subprocess.PIPE, shell=True)
        (out, err) = returnVal.communicate()
        helpers.log("URL: %s Output: %s" % (url, out))
        return out

# Objective: Return dictionary containing DPID,IP Addresses for every switch connected to current controller
# Input : N/A
# Output: Dictionary of Switch DPID and IP Addresses
    def rest_show_switch(self):
        t = test.Test()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8082
        else:
            c = t.controller('c2')
            c.http_port=8082
        url='http://%s:%s/api/v1/data/controller/core/switch' % (c.ip,c.http_port)
        helpers.log("URL is %s  " %url)
        c.rest.get(url)
        content = c.rest.content()
        switchDict ={}
        for x in range (0,len(content)):
            switchDict[str(content[x]['inet-address']['ip'])] = str(content[x]['dpid'])
        return switchDict

# Objective: Return DPID of switch, when IP Address is provided
# Input : dictionary of switch 
# Output: Dictionary of Switch DPID and IP Addresses
    def return_switch_dpid(self,switchDict,ipAddr):
            helpers.log('Dictionary is %s' % switchDict)
            return switchDict[str(ipAddr)]


# Objective: Return the MAC/Hardware Address of a given interface
# Input: Switch DPID and Interface Name
# Output: Hardware/MAC Address of Interface
    def return_switch_interface_mac(self,switchDpid,interfaceName):
        t=test.Test()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8082
        else:
            c = t.controller('c2')
            c.http_port=8082
        url='http://%s:%s/api/v1/data/controller/core/switch[interface/name="%s"][dpid="%s"]?select=interface[name="%s"]' %(c.ip,c.http_port,interfaceName,switchDpid,interfaceName)
        c.rest.get(url)
        helpers.test_log("Ouput: %s" % c.rest.result_json())
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())
        content = c.rest.content()
        return content[0]['interface'][0]['hardware-address']
    
    def verify_interface_is_up(self,switchDpid,interfaceName):
        t=test.Test()
        if(self.btc.rest_is_c1_master_controller()):
            c = t.controller('c1')
            c.http_port=8082
        else:
            c = t.controller('c2')
            c.http_port=8082
        url='http://%s:%s/api/v1/data/controller/core/switch[interface/name="%s"][dpid="%s"]?select=interface[name="%s"]' %(c.ip,c.http_port,interfaceName,switchDpid,interfaceName)
        c.rest.get(url)
        helpers.test_log("Ouput: %s" % c.rest.result_json())
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())
        content = c.rest.content()
        if (content[0]['interface'][0]['state-flags'] == 0):
                return True
        else:
                return False

    def restart_process_controller(self,process_name,controllerRole):
        '''Restart a process on controller
        
            Input:
               processName        Name of process to be restarted
               controllerRole        Where to execute the command. Accepted values are `Master` and `Slave`
        '''
        t=test.Test()
        if(self.btc.rest_is_c1_master_controller() and controllerRole=='Master' ) :
            c = t.controller('c1')
        elif (self.btc.rest_is_c1_master_controller() and controllerRole=='Slave' ):
            c = t.controller('c2')
        elif (not self.btc.rest_is_c1_master_controller() and controllerRole=='Master'):
            c = t.controller('c2')
        else:
            c = t.controller('c1')
        conn = SSH2()
        conn.connect(c.ip)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('debug bash')
        input='service ' + str(process_name) +  ' restart'
        conn.execute(input)
        conn.send('logout\r')
        conn.send('logout\r')
        conn.close()
        return True         

    def execute_controller_command_return_output(self,input,controllerRole):
        '''Execute a generic command on the controller and return ouput.
        
            Input:
                controllerRole        Where to execute the command. Accepted values are `Master` and `Slave`
                input            Command to be executed on switch
                
            Return Value: Output from command execution
            
            Example:
            
            |${syslog_op}=  |  execute switch command return output | 10.192.75.7  |  debug ofad 'help; cat /var/log/syslog | grep \"Disabling port port-channel1\"' |
                    
        '''
        t=test.Test()
        if(self.btc.rest_is_c1_master_controller() and controllerRole=='Master' ) :
            c = t.controller('c1')
        elif (self.btc.rest_is_c1_master_controller() and controllerRole=='Slave' ):
            c = t.controller('c2')            
        elif (not self.btc.rest_is_c1_master_controller() and controllerRole=='Master'):
            c = t.controller('c2')
        else:
            c = t.controller('c1')
        conn = SSH2()
        conn.connect(c.ip)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('debug bash')
        conn.execute(input)
        output = conn.response
        conn.send('logout\r')
        conn.send('logout\r')
        conn.close()
        return output

    def return_master_slave_ip_address(self):
        t=test.Test()
        ip_address_list={}
        try:
            t.controller('c2')
        except:
            return {'Master':str(t.controller('c1').ip)}
        else:
            if(self.btc.rest_is_c1_master_controller()):
                ip_address_list={'Master':str(t.controller('c1').ip), 'Slave':str(t.controller('c2').ip)}
                return (ip_address_list)
            else:
                ip_address_list={'Master':str(t.controller('c2').ip), 'Slave':str(t.controller('c1').ip)}
                return (ip_address_list)

    def rest_show_ntp(self):
        t=test.Test()
        try:
            t.controller('c2')
        except:
            c = t.controller('c1')
            c.http_port=8000
        else:
            if(self.btc.rest_is_c1_master_controller()):
                c = t.controller('c1')
                c.http_port=8000
            else:
                c = t.controller('c2')
                c.http_port=8000            
        url='http://%s:%s/rest/v1/model/ntp-server/' % (c.ip,c.http_port)
        helpers.log("URL is %s  " %url)
        c.rest.get(url)
        content = c.rest.content()
        return content[0]


    def rest_show_syslog(self):
        t=test.Test()
        try:
            t.controller('c2')
        except:
            c = t.controller('c1')
            c.http_port=8000
        else:
            if(self.btc.rest_is_c1_master_controller()):
                c = t.controller('c1')
                c.http_port=8000
            else:
                c = t.controller('c2')
                c.http_port=8000            
        url='http://%s:%s/rest/v1/model/syslog-server/' % (c.ip,c.http_port)
        helpers.log("URL is %s  " %url)
        c.rest.get(url)
        content = c.rest.content()
        return content[0]