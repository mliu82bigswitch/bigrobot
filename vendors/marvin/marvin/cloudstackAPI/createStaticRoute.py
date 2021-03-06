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


"""Creates a static route"""
from baseCmd import *
from baseResponse import *
class createStaticRouteCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """static route cidr"""
        """Required"""
        self.cidr = None
        self.typeInfo['cidr'] = 'string'
        """the gateway id we are creating static route for"""
        """Required"""
        self.gatewayid = None
        self.typeInfo['gatewayid'] = 'uuid'
        self.required = ["cidr","gatewayid",]

class createStaticRouteResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of static route"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account associated with the static route"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """static route CIDR"""
        self.cidr = None
        self.typeInfo['cidr'] = 'string'
        """the domain associated with the static route"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the ID of the domain associated with the static route"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """VPC gateway the route is created for"""
        self.gatewayid = None
        self.typeInfo['gatewayid'] = 'string'
        """the project name of the static route"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the static route"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the state of the static route"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """VPC the static route belongs to"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'
        """the list of resource tags associated with static route"""
        self.tags = []

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

