import autobot.helpers as helpers
import autobot.restclient as restclient
import autobot.test as test
import keywords.Host as Host
import re
import os
import paramiko

class T5_longevity(object):
# This is for all the common function   - Mingtao
    def __init__(self):
        pass

 
    def copy_pkg_from_jenkins(self):
        '''copy_pkg_from_jenkins
            copy the latest upgrade package from Jenkin
        
        '''
        t = test.Test()
        c = t.controller('master')
        image = self.cli_check_image()
        helpers.log('INFO: *******system image is: %s ' % image)
        if str(image) == '-1':
            helpers.log("INFO: system NOT have image, copying image")
            c.config('')
            string = 'copy "scp://bsn@jenkins:/var/lib/jenkins/jobs/bvs master/lastSuccessful/archive/target/appliance/images/bvs/controller-upgrade-bvs-2.0.5-SNAPSHOT.pkg"'
            c.send(string + ' image://')
#            c.expect(r'[\r\n].+password: ') 
            c.expect(r'[\r\n].+password: |[\r\n].+(yes/no)?')
            content = c.cli_content()
            helpers.log("*****Output is :\n%s" % content)
            if re.match(r'.*password:.* ', content):
                helpers.log("INFO:  need to provide passwd " )
                c.send('bsn')
            elif re.match(r'.+(yes/no)?', content):
                helpers.log("INFO:  need to send yes, then provide passwd " )
                c.send('yes')
                c.expect(r'[\r\n].+password: ')
                c.send('bsn')
            
            try:
                c.expect(timeout=180)
            except:
                helpers.log('scp failed')
                return False
            else:
                helpers.log('scp completed successfully')
                image = self.cli_check_image()

        else:
            helpers.log("INFO: system has image: %s" % image)

        return image





    def cli_check_image(self):
        t = test.Test()
        c = t.controller('master')
        c.enable('')
        c.enable("show image")
        content = c.cli_content()
        helpers.log("*****Output is :\n%s" % content)
        temp = helpers.strip_cli_output(content)
        temp = helpers.str_to_list(temp)
        helpers.log("*****Output list   is :\n%s" % temp)
        if len(temp) == 1 and 'None.' in temp:
            helpers.log("INFO:  ***image is not in controller******")
            return -1
        else:
            temp.pop(0);temp.pop(0)
            helpers.log("INFO:  ***image is available: %s" % temp)
            line = temp[0].split()
            image = line[3]
            helpers.log("INFO: ***image is available: %s" % image)

        return image


    def cli_upgrade_stage(self, image=None):
        t = test.Test()
        c = t.controller('master')
        helpers.log('INFO: Entering ==> cli_upgrade_stage ')
        c.config('')
        if image is None:
            c.send('upgrade stage')
        else:
            c.send('upgrade stage ' + image)
        c.expect(r'[\r\n].+: ')
        content = c.cli_content()
        helpers.log("*****Output is :\n%s" % content)
        c.send("yes")
        try:
            c.expect(timeout=180)
        except:
            helpers.log('stage did not finish within 180 second ')
            return False
        else:
            content = c.cli_content()
            helpers.log("INFO:*****Content Output is :\n%s" % content)
            temp = helpers.str_to_list(content)
            helpers.log("INFO:*****temp Output is :\n%s" % temp)
            for line in temp:
                helpers.log("line is : %s" % line)
                if re.match(r'Upgrade stage: Upgrade Staged', line):
                    helpers.log('stage completed successfully')
                    return True
        return False

    def cli_upgrade_launch(self):
        t = test.Test()
        c = t.controller('master')
        helpers.log('INFO: Entering ==> cli_upgrade_launch ')
        c.config('')
        c.send('upgrade launch')
        c.expect(r'[\r\n].+: ')
        content = c.cli_content()
        helpers.log("*****Output is :\n%s" % content)
        c.send("yes")
         
        try:
            c.expect(r'[\r\n].+Rebooting.*')
        except:
            helpers.log('ERROR: upgrade launch NOT successfully')
            return False
        else:
            helpers.log('INFO: upgrade launch  successfully')
            return True
        return False

    def rest_get_node_role(self,device='c1'):
        ''' rest_get_node_role
           return the local node role:
           output:   active   
                     stand-by
        '''
        t = test.Test()
        c = t.controller(device)
        helpers.log('INFO: Entering ==> rest_get_node_role ')
        t = test.Test()
        
        url = '/api/v1/data/controller/cluster'  
        c.rest.get(url)
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())

        if(c.rest.content()):
            local_id = c.rest.content()[0]['status']['local-node-id']
            helpers.log("INFO: local node ID: %s" %  local_id)
            if c.rest.content()[0]['status']['domain-leader']:
                leader_id = c.rest.content()[0]['status']['domain-leader']['leader-id']
                helpers.log("INFO: domain-leader: %s" % c.rest.content()[0]['status']['domain-leader']['leader-id'])
                if local_id == leader_id:
                    return 'active'
                else:
                    return 'stand-by'
                
            else:
                helpers.log("ERROR: there is no domain-leader" ) 
                helpers.test_failure('ERROR: There is no domain-leader')
        return False     

      
 
    def cli_get_node_role(self,device='c1'):
        ''' rest_get_node_role
           return the local node role:
           output:   active   
                     stand-by
        '''
  
        t = test.Test()
        c = t.controller(device)
        helpers.log('INFO: Entering ==> cli_get_node_role ')
        t = test.Test()
        
        c.cli('show cluster' )
        content = c.cli_content()
        temp = helpers.strip_cli_output(content)
        temp = helpers.str_to_list(temp)
        for line in temp:          
            helpers.log("INFO: line is - %s" % line)
            match= re.match(r'.*(active|stand-by).* Current', line)
            if match:
                helpers.log("INFO: role is: %s" % match.group(1))                          
                return  match.group(1)
            else:
                helpers.log("INFO: not current node  %s" % line)   
        return False     




    def cli_show_walk(self, string='', file_name=None, padding=''):
        t = test.Test()
        c = t.controller('master')
        c.enable('')
        helpers.log("********* Entering CLI show  walk with ----> string: %s, file name: %s" % (string, file_name))
        if string =='':
            cli_string = '?' 
        else: 
            cli_string = string + ' ?'
        c.send(cli_string, no_cr=True)
        c.expect(r'[\r\n\x07][\w-]+[#>] ')
        content = c.cli_content()
        temp = helpers.strip_cli_output(content)
        temp = helpers.str_to_list(temp)
        helpers.log("******new_content:\n%s" % helpers.prettify(temp))
        c.send(helpers.ctrl('u'))
        c.expect()

        string_c = string
        helpers.log("string for this level is: %s" % string_c)
        helpers.log("The length of string: %d" % len(temp))

        if file_name:
            helpers.log("opening file: %s" % file_name)
            fo = open(file_name, 'a')
            lines = []
            lines.append((padding + string))
            lines.append((padding + '----------'))            
            for line in temp:
                lines.append((padding + line))
            lines.append((padding + '=================='))             
            content = '\n'.join(lines)
            fo.write(str(content))
            fo.write("\n")
            
            fo.close()

        num = len(temp)
        padding = "   " + padding
        for line in temp:
            string = string_c
            helpers.log(" line is - %s" % line)
            if re.match(r'For', line) or line == "Commands:":
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            if re.match(r'^<.+', line) and not re.match(r'^<cr>', line):
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config fabric port-group":
                helpers.log("GR - BSC-4724 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config switch":
                helpers.log("GR - BSC-4725 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config tenant":
                helpers.log("GR - BSC-4727 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show switch":
                helpers.log("GR - BSC-4729 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show test-packet-path":
                helpers.log("GR -   Ignoring line - %s" % line)
                num = num - 1
                continue

            keys = line.split(' ')
            key = keys.pop(0)
            helpers.log("*** key is - %s" % key)
            if key == '<cr>':
                helpers.log(" complete CLI show command: ******%s******" % string)
                c.enable(string)
                if num == 1:
                    return string
            else:
#                helpers.log(" string before add key --- ******%s******" % string )
                string = string + ' ' + key
                helpers.log("key - %s" % (key))
                helpers.log("***** Call the cli walk again with  --- %s" % string)
                self.cli_show_walk(string, file_name, padding)


    def cli_exec_walk(self, string='', file_name=None, padding=''):
        t = test.Test()
        c = t.controller('master')
        c.cli('')
        helpers.log("********* Entering cli_exec_walk ----> string: %s, file name: %s" % (string, file_name))
        if string =='':
            cli_string = '?' 
        else: 
            cli_string = string + ' ?'
        c.send(cli_string, no_cr=True)
        c.expect(r'[\r\n\x07][\w-]+[#>] ')
        content = c.cli_content()
        temp = helpers.strip_cli_output(content)
        temp = helpers.str_to_list(temp)
        helpers.log("******new_content:\n%s" % helpers.prettify(temp))
        c.send(helpers.ctrl('u'))
        c.expect()

        string_c = string
        helpers.log("string for this level is: %s" % string_c)
        helpers.log("The length of string: %d" % len(temp))

        if file_name:
            helpers.log("opening file: %s" % file_name)
            fo = open(file_name, 'a')
            lines = []
            lines.append((padding + string))
            lines.append((padding + '----------'))            
            for line in temp:
                lines.append((padding + line))
            lines.append((padding + '=================='))             
            content = '\n'.join(lines)
            fo.write(str(content))
            fo.write("\n")
            
            fo.close()

        num = len(temp)
        padding = "   " + padding
        for line in temp:
            string = string_c
            helpers.log(" line is - %s" % line)
            if re.match(r'For', line) or line == "Commands:":
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            if re.match(r'^<.+', line) and not re.match(r'^<cr>', line):
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config fabric port-group":
                helpers.log("GR - BSC-4724 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config switch":
                helpers.log("GR - BSC-4725 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config tenant":
                helpers.log("GR - BSC-4727 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show switch":
                helpers.log("GR - BSC-4729 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show test-packet-path":
                helpers.log("GR -   Ignoring line - %s" % line)
                num = num - 1
                continue

            keys = line.split(' ')
            key = keys.pop(0)
            helpers.log("*** key is - %s" % key)
            if key == '<cr>':
                helpers.log(" complete CLI show command: ******%s******" % string)
                c.cli(string)
                if num == 1:
                    return string
            else:
#                helpers.log(" string before add key --- ******%s******" % string )
                string = string + ' ' + key
                helpers.log("key - %s" % (key))
                helpers.log("***** Call the cli walk again with  --- %s" % string)
                self.cli_exec_walk(string, file_name, padding)


    def cli_config_walk(self, string='', file_name=None, padding=''):
        t = test.Test()
        c = t.controller('master')
        c.enable('')
        helpers.log("********* Entering CLI show  walk with ----> string: %s, file name: %s" % (string, file_name))
        if string =='':
            cli_string = '?' 
        else: 
            cli_string = string + ' ?'
        c.send(cli_string, no_cr=True)
        c.expect(r'[\r\n\x07][\w-]+[#>] ')
        content = c.cli_content()
        temp = helpers.strip_cli_output(content)
        temp = helpers.str_to_list(temp)
        helpers.log("******new_content:\n%s" % helpers.prettify(temp))
        c.send(helpers.ctrl('u'))
        c.expect()

        string_c = string
        helpers.log("string for this level is: %s" % string_c)
        helpers.log("The length of string: %d" % len(temp))

        if file_name:
            helpers.log("opening file: %s" % file_name)
            fo = open(file_name, 'a')
            lines = []
            lines.append((padding + string))
            lines.append((padding + '----------'))            
            for line in temp:
                lines.append((padding + line))
            lines.append((padding + '=================='))             
            content = '\n'.join(lines)
            fo.write(str(content))
            fo.write("\n")
            
            fo.close()

        num = len(temp)
        padding = "   " + padding
        for line in temp:
            string = string_c
            helpers.log(" line is - %s" % line)
            if re.match(r'For', line) or line == "Commands:":
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            if re.match(r'^<.+', line) and not re.match(r'^<cr>', line):
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config fabric port-group":
                helpers.log("GR - BSC-4724 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config switch":
                helpers.log("GR - BSC-4725 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show running-config tenant":
                helpers.log("GR - BSC-4727 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show switch":
                helpers.log("GR - BSC-4729 Ignoring line - %s" % line)
                num = num - 1
                continue
            if string == "show test-packet-path":
                helpers.log("GR -   Ignoring line - %s" % line)
                num = num - 1
                continue

            keys = line.split(' ')
            key = keys.pop(0)
            helpers.log("*** key is - %s" % key)
            if key == '<cr>':
                helpers.log(" complete CLI show command: ******%s******" % string)
                c.enable(string)
                if num == 1:
                    return string
            else:
#                helpers.log(" string before add key --- ******%s******" % string )
                string = string + ' ' + key
                helpers.log("key - %s" % (key))
                helpers.log("***** Call the cli walk again with  --- %s" % string)
                self.cli_show_walk(string, file_name, padding)










    def cli_walk(self, string=''):
        t = test.Test()
        c = t.controller('master')
        c.cli('')
        helpers.log("********* Entering CLI show  walk with ---->  %s" % string)
        if string == '':
            cli_string = '?'
        else:
            cli_string = string + ' ?'
        c.send(cli_string, no_cr=True)
        c.expect(r'[\r\n\x07][\w-]+[#>] ')
        content = c.cli_content()
        temp = helpers.strip_cli_output(content)
        temp = helpers.str_to_list(temp)
        helpers.log("******new_content:\n%s" % helpers.prettify(temp))
        c.send(helpers.ctrl('u'))
        c.expect()
        c.cli('')

        string_c = string
        helpers.log("string for this level is: %s" % string_c)
        helpers.log("The length of string: %d" % len(temp))
        num = len(temp)
        for line in temp:
            string = string_c
            helpers.log(" line is - %s" % line)
            line = line.lstrip()
            keys = line.split(' ')
            key = keys.pop(0)

            if key == "debug" or key == "reauth" or key == "echo" or key == "help" or key == "history" or key == "logout" or key == "ping" or key == "show" or key == "watch":
                helpers.log("Ignore line %s" % line)
                num = num - 1
                continue
            if re.match(r'For', line) or line == "Commands:":
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            if re.match(r'^<.+', line) and not re.match(r'^<cr>', line):
                helpers.log("Ignoring line - %s" % line)
                num = num - 1
                continue
            line = line.lstrip()
            keys = line.split(' ')
            key = keys.pop(0)
            helpers.log("*** key is - %s" % key)
            if key == '<cr>':
                helpers.log(" complete CLI show command: ******%s******" % string)
                helpers.log(" complete CLI show command: ******%d******" % num)
                c.cli(string)
                if num == 1:
                    helpers.log("AT END: ******%s******" % string)
                    return string
            else:
#                helpers.log(" string before add key --- ******%s******" % string )
                string = string + ' ' + key
                helpers.log("  key - %s" % (key))
                helpers.log("***** Call the cli walk again with  --- %s" % string)
                self.cli_walk(string)



