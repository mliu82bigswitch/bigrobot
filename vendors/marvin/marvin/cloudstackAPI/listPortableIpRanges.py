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


"""list portable IP ranges"""
from baseCmd import *
from baseResponse import *
class listPortableIpRangesCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """Id of the portable ip range"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """Id of a Region"""
        self.regionid = None
        self.typeInfo['regionid'] = 'integer'
        self.required = []

class listPortableIpRangesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """portable IP range ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the end ip of the portable IP range"""
        self.endip = None
        self.typeInfo['endip'] = 'string'
        """the gateway of the VLAN IP range"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """the netmask of the VLAN IP range"""
        self.netmask = None
        self.typeInfo['netmask'] = 'string'
        """Region Id in which portable ip range is provisioned"""
        self.regionid = None
        self.typeInfo['regionid'] = 'integer'
        """the start ip of the portable IP range"""
        self.startip = None
        self.typeInfo['startip'] = 'string'
        """the ID or VID of the VLAN."""
        self.vlan = None
        self.typeInfo['vlan'] = 'string'
        """List of portable IP and association with zone/network/vpc details that are part of GSLB rule"""
        self.portableipaddress = []

class portableipaddress:
    def __init__(self):
        """"the account ID the portable IP address is associated with"""
        self.accountid = None
        """"date the portal IP address was acquired"""
        self.allocated = None
        """"the domain ID the portable IP address is associated with"""
        self.domainid = None
        """"public IP address"""
        self.ipaddress = None
        """"the ID of the Network where ip belongs to"""
        self.networkid = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"Region Id in which global load balancer is created"""
        self.regionid = None
        """"State of the ip address. Can be: Allocatin, Allocated and Releasing"""
        self.state = None
        """"VPC the ip belongs to"""
        self.vpcid = None
        """"the ID of the zone the public IP address belongs to"""
        self.zoneid = None

