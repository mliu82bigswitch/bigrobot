import autobot.helpers as helpers
import autobot.test as test

class T5Platform(object):

    def __init__(self):
	pass
   
    def rest_configure_ntp(self, ntp_server):
        '''Configure the ntp server
        
            Input:
                    ntp_server        NTP server IP address
                                       
            Returns: True if policy configuration is successful, false otherwise  
        '''
        t = test.Test()
        c = t.controller()
                        
        url = '/api/v1/data/controller/action/time/ntp'      
        c.rest.put(url, {"ntp-server": ntp_server})
        
        if not c.rest.status_code_ok():
            helpers.test_failure(c.rest.error())
            return False

        return True

    def rest_show_ntp_servers(self):
        '''Return the list of NTP servers      
                    
            Returns: Output of 'ntpq -pn' which lists configured NTP servers and their status
        '''
        t = test.Test()
        c = t.controller()
        
        url = '/api/v1/data/controller/action/time/ntp/status '
        c.rest.get(url)
        
        return True
    
    
    def rest_verify_show_cluster(self):
        '''Using the 'show cluster' command verify the cluster formation across both nodes
	   Also check for the formation integrity
	'''
        try:
            t = test.Test()
            c1 = t.controller("c1")
            c2 = t.controller("c2")
            url = '/api/v1/data/controller/cluster'
            
            result = c1.rest.get(url)['content']
            reported_active_by_c1 = result[0]['status']['domain-leader']['leader-id']
            
            result = c2.rest.get(url)['content']
            reported_active_by_c2 = result[0]['status']['domain-leader']['leader-id']
            
            if(reported_active_by_c1 != reported_active_by_c2):
                helpers.log("Both controllers %s & %s are declaring themselves as active" \
                        % (reported_active_by_c1, reported_active_by_c2))
                helpers.test_failure("Error: Inconsistent active/stand-By cluster formation detected")
                return False
            else:
                helpers.log("Active controller id is: %s " % reported_active_by_c1)
                helpers.log("Pass: Consistent active/standby cluster formation verified")
                return True
            
        except Exception, err:
            helpers.test_failure("Exception in: rest_verify_ha_cluster %s : %s " % (Exception, err))
            return False



    def rest_cluster_take_leader(self):
        ''' Invoke "cluster election take-leader" command and verify the active controller change.
            Verify by executing on both the current-active and current-stdby controller
        '''
        try:
            t = test.Test()
            master = t.controller("master")

        except Exception, err:
            helpers.test_failure("Exception in: rest_cluster_take_leader %s : %s " % (Exception, err))
            return false








