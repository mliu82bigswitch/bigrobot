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


"""Updates site to site vpn connection"""
from baseCmd import *
from baseResponse import *
class updateVpnConnectionCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """id of vpn connection"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the vpn to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["id",]

class updateVpnConnectionResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the connection ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the owner"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """guest cidr list of the customer gateway"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """the date and time the host was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the domain name of the owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """if DPD is enabled for customer gateway"""
        self.dpd = None
        self.typeInfo['dpd'] = 'boolean'
        """Lifetime of ESP SA of customer gateway"""
        self.esplifetime = None
        self.typeInfo['esplifetime'] = 'long'
        """ESP policy of the customer gateway"""
        self.esppolicy = None
        self.typeInfo['esppolicy'] = 'string'
        """is connection for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """public ip address id of the customer gateway"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """Lifetime of IKE SA of customer gateway"""
        self.ikelifetime = None
        self.typeInfo['ikelifetime'] = 'long'
        """IKE policy of the customer gateway"""
        self.ikepolicy = None
        self.typeInfo['ikepolicy'] = 'string'
        """IPsec Preshared-Key of the customer gateway"""
        self.ipsecpsk = None
        self.typeInfo['ipsecpsk'] = 'string'
        """State of vpn connection"""
        self.passive = None
        self.typeInfo['passive'] = 'boolean'
        """the project name"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the public IP address"""
        self.publicip = None
        self.typeInfo['publicip'] = 'string'
        """the date and time the host was removed"""
        self.removed = None
        self.typeInfo['removed'] = 'date'
        """the customer gateway ID"""
        self.s2scustomergatewayid = None
        self.typeInfo['s2scustomergatewayid'] = 'string'
        """the vpn gateway ID"""
        self.s2svpngatewayid = None
        self.typeInfo['s2svpngatewayid'] = 'string'
        """State of vpn connection"""
        self.state = None
        self.typeInfo['state'] = 'string'

