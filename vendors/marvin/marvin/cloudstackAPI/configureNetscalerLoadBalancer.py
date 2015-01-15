# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


"""configures a netscaler load balancer device"""
from baseCmd import *
from baseResponse import *
class configureNetscalerLoadBalancerCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """Netscaler load balancer device ID"""
        """Required"""
        self.lbdeviceid = None
        self.typeInfo['lbdeviceid'] = 'uuid'
        """true if netscaler load balancer is intended to be used in in-line with firewall, false if netscaler load balancer will side-by-side with firewall"""
        self.inline = None
        self.typeInfo['inline'] = 'boolean'
        """capacity of the device, Capacity will be interpreted as number of networks device can handle"""
        self.lbdevicecapacity = None
        self.typeInfo['lbdevicecapacity'] = 'long'
        """true if this netscaler device to dedicated for a account, false if the netscaler device will be shared by multiple accounts"""
        self.lbdevicededicated = None
        self.typeInfo['lbdevicededicated'] = 'boolean'
        """Used when NetScaler device is provider of EIP service. This parameter represents the list of pod's, for which there exists a policy based route on datacenter L3 router to route pod's subnet IP to a NetScaler device."""
        self.podids = []
        self.typeInfo['podids'] = 'list'
        self.required = ["lbdeviceid",]

class configureNetscalerLoadBalancerResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """true if NetScaler device is provisioned to be a GSLB service provider"""
        self.gslbprovider = None
        self.typeInfo['gslbprovider'] = 'boolean'
        """private IP of the NetScaler representing GSLB site"""
        self.gslbproviderprivateip = None
        self.typeInfo['gslbproviderprivateip'] = 'string'
        """public IP of the NetScaler representing GSLB site"""
        self.gslbproviderpublicip = None
        self.typeInfo['gslbproviderpublicip'] = 'string'
        """the management IP address of the external load balancer"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """true if NetScaler device is provisioned exclusively to be a GSLB service provider"""
        self.isexclusivegslbprovider = None
        self.typeInfo['isexclusivegslbprovider'] = 'boolean'
        """device capacity"""
        self.lbdevicecapacity = None
        self.typeInfo['lbdevicecapacity'] = 'long'
        """true if device is dedicated for an account"""
        self.lbdevicededicated = None
        self.typeInfo['lbdevicededicated'] = 'boolean'
        """device id of the netscaler load balancer"""
        self.lbdeviceid = None
        self.typeInfo['lbdeviceid'] = 'string'
        """device name"""
        self.lbdevicename = None
        self.typeInfo['lbdevicename'] = 'string'
        """device state"""
        self.lbdevicestate = None
        self.typeInfo['lbdevicestate'] = 'string'
        """the physical network to which this netscaler device belongs to"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'string'
        """Used when NetScaler device is provider of EIP service. This parameter represents the list of pod's, for which there exists a policy based route on datacenter L3 router to route pod's subnet IP to a NetScaler device."""
        self.podids = None
        self.typeInfo['podids'] = 'list'
        """the private interface of the load balancer"""
        self.privateinterface = None
        self.typeInfo['privateinterface'] = 'string'
        """name of the provider"""
        self.provider = None
        self.typeInfo['provider'] = 'string'
        """the public interface of the load balancer"""
        self.publicinterface = None
        self.typeInfo['publicinterface'] = 'string'

