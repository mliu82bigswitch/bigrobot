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


"""Updates a physical network"""
from baseCmd import *
from baseResponse import *
class updatePhysicalNetworkCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """physical network id"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the speed for the physical network[1G/10G]"""
        self.networkspeed = None
        self.typeInfo['networkspeed'] = 'string'
        """Enabled/Disabled"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """Tag the physical network"""
        self.tags = []
        self.typeInfo['tags'] = 'list'
        """the VLAN for the physical network"""
        self.vlan = None
        self.typeInfo['vlan'] = 'string'
        self.required = ["id",]

class updatePhysicalNetworkResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the uuid of the physical network"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Broadcast domain range of the physical network"""
        self.broadcastdomainrange = None
        self.typeInfo['broadcastdomainrange'] = 'string'
        """the domain id of the physical network owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """isolation methods"""
        self.isolationmethods = None
        self.typeInfo['isolationmethods'] = 'string'
        """name of the physical network"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the speed of the physical network"""
        self.networkspeed = None
        self.typeInfo['networkspeed'] = 'string'
        """state of the physical network"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """comma separated tag"""
        self.tags = None
        self.typeInfo['tags'] = 'string'
        """the vlan of the physical network"""
        self.vlan = None
        self.typeInfo['vlan'] = 'string'
        """zone id of the physical network"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'

