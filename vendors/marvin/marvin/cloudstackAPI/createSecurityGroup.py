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


"""Creates a security group"""
from baseCmd import *
from baseResponse import *
class createSecurityGroupCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """name of the security group"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """an optional account for the security group. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the description of the security group"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """an optional domainId for the security group. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """Create security group for project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["name",]

class createSecurityGroupResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the security group"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the security group"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the description of the security group"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """the domain name of the security group"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the security group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the name of the security group"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project name of the group"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the group"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the list of egress rules associated with the security group"""
        self.egressrule = []
        """the list of ingress rules associated with the security group"""
        self.ingressrule = []
        """the list of resource tags associated with the rule"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        self.typeInfo['jobid'] = ''
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = ''

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

class egressrule:
    def __init__(self):
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
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

class ingressrule:
    def __init__(self):
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
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

