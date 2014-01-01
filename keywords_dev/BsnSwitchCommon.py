import autobot.helpers as helpers
import autobot.test as test
from Exscript.protocols import SSH2
from Exscript import Account, Host
import subprocess
import string
import telnetlib
import time

class BsnSwitchCommon(object):

    def __init__(self):
        t = test.Test()
        c = t.controller()
        url = '%s/auth/login' % c.base_url
        helpers.log("url: %s" % url)
        result = c.rest.post(url, {"user":"admin", "password":"adminadmin"})
        helpers.log("result: %s" % helpers.to_json(result))
        session_cookie = result['content']['session_cookie']
        c.rest.set_session_cookie(session_cookie)

    def activate_deactivate_controller(self,ip_address,iteration):
        """Activate and deactivate controller configuration on switch"""
        t = test.Test()
        c = t.controller()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        mycount = 1
        while (mycount<=iteration):
            conn.execute('enable')
            conn.execute('conf t')
            inp = "no controller " + str(c.ip)
            conn.execute(inp)
            conn.execute('end')
            conn.execute('show running-config openflow')
            print conn.response
            helpers.sleep(10)
            conn.execute('conf t')
            inp = "controller " + str(c.ip)
            conn.execute(inp)
            conn.execute('end')
            conn.execute('show running-config openflow')
            print conn.response
            if iteration > mycount :
                mycount=mycount+1
                helpers.sleep(10)
            elif mycount == iteration :
                conn.send('exit\r')
                conn.send('exit\r')
                conn.send('exit\r')
                conn.close()
        return True
    
    def configure_snmp_keyword(self,ip_address,snmpKey,snmpValue):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        input="snmp-server %s %s" % (str(snmpKey),str(snmpValue))
        conn.execute(input)
        conn.send('exit\r')
        conn.send('exit\r')
        conn.send('exit\r')
        conn.close()
        return True
    
    def delete_snmp_keyword(self,ip_address,snmpKey,snmpValue):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        input="no snmp-server %s %s" % (str(snmpKey),str(snmpValue))
        conn.execute(input)
        conn.send('exit\r')
        conn.send('exit\r')
        conn.send('exit\r')
        conn.close()
        return True
    
    def configure_snmp_host(self,ip_address,remHostIP,snmpKey,snmpCommunity,snmpPort):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        if snmpKey == "traps" or snmpKey == "trap":
            snmpKey == "traps"
        else:
            snmpKey == "informs"
        input="snmp-server host %s %s %s udp-port %s" % (str(remHostIP),str(snmpKey),str(snmpCommunity),str(snmpPort))
        conn.execute(input)
        conn.send('exit\r')
        conn.send('exit\r')
        conn.send('exit\r')
        conn.close()
        return True

    def delete_snmp_host(self,ip_address,remHostIP,snmpKey,snmpCommunity,snmpPort):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        if snmpKey == "traps" or snmpKey == "trap":
            snmpKey == "traps"
        else:
            snmpKey == "informs"
        input="no snmp-server host %s %s %s udp-port %s" % (str(remHostIP),str(snmpKey),str(snmpCommunity),str(snmpPort))
        conn.execute(input)
        conn.send('exit\r')
        conn.send('exit\r')
        conn.send('exit\r')
        conn.close()
        return True

    def enable_snmp(self,ip_address):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        conn.execute("snmp-server enable")
        conn.send('exit\r')
        conn.send('exit\r')
        conn.send('exit\r')
        conn.close()
        return True

    def disable_switch_snmp(self,ip_address):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        conn.execute("no snmp-server enable")
        conn.send('exit\r')
        conn.send('exit\r')
        conn.send('exit\r')
        conn.close()
        return True

    def snmp_show(self,ip_address):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute("show snmp-server")
        return conn.response
    
#   Objective: Execute snmpgetnext from local machine for a particular SNMP OID
#   Input: SNMP Community and OID 
#   Return Value:  return the SNMP Walk O/P
    def snmp_cmd(self,ip_address,snmp_cmd,snmpCommunity,snmpOID):
        t = test.Test()
        url="/usr/bin/%s -v2c -c %s %s %s" % (str(snmp_cmd),str(snmpCommunity),ip_address,str(snmpOID))
        returnVal = subprocess.Popen([url], stdout=subprocess.PIPE, shell=True)
        (out, err) = returnVal.communicate()
        helpers.log("URL: %s Output: %s" % (url, out))
        return out
        
    def snmp_cmd_opt(self,ip_address,snmp_cmd,snmpOpt, snmpCommunity,snmpOID):
        t = test.Test()
        url="/usr/bin/%s  -v2c %s -c %s %s %s" % (str(snmp_cmd),str(snmpOpt),str(snmpCommunity),ip_address,str(snmpOID))
        returnVal = subprocess.Popen([url], stdout=subprocess.PIPE, shell=True)
        (out, err) = returnVal.communicate()
        helpers.log("URL: %s Output: %s" % (url, out))
        return out

    def restart_process(self,ip_address,processName):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        input='debug ofad "help; service ' + str(processName) +  ' restart"'
        conn.execute(input)
        conn.send('logout\r')
        conn.close()
        return True
    
    def configure_portchannel(self,ip_address,pcNumber,portList,hashMode):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        input_value = "port-channel " + str(pcNumber) + " interface-list " + str(portList) + "  hash " + str(hashMode)
        helpers.log("Input is %s" % input_value )
        try:
            conn.execute(input_value)
        except:
            return False            
        return True

    def unconfigure_portchannel(self,ip_address,pcNumber):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        input = "no port-channel " + str(pcNumber) + " "
        conn.execute(input)
        conn.send('logout\r')
        conn.close()
        return True
        
    def return_intf_macaddress(self,ip_address,intf_name):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        input = "show interface " + str(intf_name) + " detail"
        conn.execute(input)
        content = string.split(conn.response, '\n')
        (firstvalue,colon,lastvalue) = content[2].strip().partition(':')
        lastvalue=str(lastvalue).rstrip('\n').replace(" ", "")
        mac_address = lastvalue.rstrip('\n')
        helpers.log("Value in content[1] is %s \n and mac address is %s" %(content[1],mac_address))
        return mac_address

    def return_intf_state(self,ip_address,intf_name):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        input = "show interface " + str(intf_name) + " detail"
        conn.execute(input)
        content = string.split(conn.response, '\n')
        helpers.log("Value in content[1] is '%s' " %(content[1]))
        (firstvalue,colon,lastvalue) = content[1].rstrip('\n').strip().split(' ')
        intf_state = lastvalue.rstrip('\n')
        helpers.log("Value in content[1] is %s \n and intf_state is %s" %(content[1],intf_state))
        return intf_state

    def verify_portchannel(self,ip_address,pcNumber):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        intf_name = "port-channel"+pcNumber
        input = "show interface " + intf_name
        conn.execute(input)
        helpers.log("Multiline is %s" % (string.split(conn.response, '\n')))
        lagNumber = 60 + int(pcNumber)
        input1=str(lagNumber) + "* " + intf_name
        if str(input1) in conn.response:
                return True
        else:
                return False
    
    def verify_portchannel_members(self,ip_address,pc_number,intf_name):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        input = "show port-channel " + str(pc_number)
        conn.execute(input)
        content = string.split(conn.response, '\n')
        helpers.log("Length of content %d" % (len(content)))
        if len(content) < 8 :
            return False
        else :
            for i in range(8,len(content)):
                intfName = ' '.join(content[i].split()).split(" ",2)
                helpers.log('intfName is %s' % intfName)
                if len(intfName) >1 and intfName[1] == intf_name :
                        helpers.log("IntfName is %s \n" % (intfName[1]))
                        return True
        return False

    def verify_portchannel_member_state(self,ip_address,pc_number,intf_name):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        input = "show port-channel " + str(pc_number)
        conn.execute(input)
        content = string.split(conn.response, '\n')
        helpers.log("Length of content %d" % (len(content)))
        if len(content) < 8 :
            return False
        else :
            for i in range(8,len(content)):
                intfName = ' '.join(content[i].split()).split(" ",2)
                if len(intfName) >1 and intfName[1] == intf_name :
                        if intfName[0] == "*" :
                            helpers.log("Intf Name is %s and state is %s \n" % (intfName[1], intfName[0]))
                            return True
                        else:
                            helpers.log("Intf Name is %s and state is %s \n" % (intfName[1], intfName[0]))
                            return False
        return False

#Objective: Shut/Unshut interface
#Inputs: Switch IP Address (ip_address), Interface Name and State (Yes="shutdown", No="no shutdown")
#Output: Shut/No-Shut interface

    def change_interface_state(self,ip_address,interface_name,state):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        if state =="yes" or state =="Yes":
                input = "interface " + str(interface_name) + " shutdown"
        else:
                input = "no interface " + str(interface_name) + " shutdown"
        conn.execute(input)
        conn.send('logout\r')
        conn.close()
        return True

#Objective:  Shut/Unshut interface via broadcom shell command.
#Inputs: Switch IP Address (ip_address), Interface Number and State (Yes="shutdown", No="no shutdown")
#Output: Shut/No-Shut interface
    def change_interface_state_bshell(self,ip_address,interface_num,state):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute('conf t')
        if state =="yes" or state =="Yes":
                input = 'debug ofad "help; ofad-ctl bshell port ' + str(interface_num) + ' enable=0"'
        else:
                input = 'debug ofad "help; ofad-ctl bshell port ' + str(interface_num) + ' enable=1"'
        conn.execute(input)
        conn.send('logout\r')
        conn.close()
        return True

#Objective: Grep syslog on switch for string
#Input:     IP Address of Switch, string to grep for.
#Output:    Output string.
    def execute_switch_command_return_output(self,ip_address,input):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
#        input="debug ofad 'help; cat /var/log/syslog | grep \"" + str(string_to_grep) + "\"'"
        conn.execute(input)
        output = conn.response
        conn.send('logout\r')
        conn.close()
        return output

#Objective: Execute CLI commands on switch, where we do not care for ouput from switch.
#Input:  IP Address of Switch, CLI command
#Output: Always True
    def execute_switch_command(self,ip_address,cli_cmd):
        t = test.Test()
        conn = SSH2()
        conn.connect(ip_address)
        conn.login(Account("admin","adminadmin"))
        conn.execute('enable')
        conn.execute(cli_cmd)
        conn.send('logout\r')
        conn.close()
        return True 

    def flap_interface_ma1(self,conIP,conPort):
        user = "admin"
        password = "adminadmin"
        tn = telnetlib.Telnet(str(conIP),int(conPort))
        tn.read_until("login: ", 3)
        tn.write(user + "\r\n")
        tn.read_until("Password: ", 3)
        tn.write(password + "\r\n")
        tn.read_until('')
        tn.write("\r\n" + "show running-config" + "\r\n")
        tn.write("\r\n" + "debug bash" + "\r\n")
        tn.write("ifconfig ma1 " + "\r\n")
        tn.write("ifconfig ma1 down" + "\r\n")
        time.sleep(2)
        tn.write("ifconfig ma1 up" + "\r\n")
        tn.write("exit" + "\r\n")
        tn.write("exit" + "\r\n")
        tn.close()
        return True 
