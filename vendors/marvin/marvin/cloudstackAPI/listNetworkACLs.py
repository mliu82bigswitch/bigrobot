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


"""Lists all network ACL items"""
from baseCmd import *
from baseResponse import *
class listNetworkACLsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list network ACL Items by ACL Id"""
        self.aclid = None
        self.typeInfo['aclid'] = 'uuid'
        """list network ACL Items by Action"""
        self.action = None
        self.typeInfo['action'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list resources by display flag; only ROOT admin is eligible to pass this parameter"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """Lists network ACL Item with the specified ID"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """list network ACL Items by network Id"""
        self.networkid = None
        self.typeInfo['networkid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """list network ACL Items by Protocol"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """List resources by tags (key/value pairs)"""
        self.tags = []
        self.typeInfo['tags'] = 'map'
        """list network ACL Items by traffic type - Ingress or Egress"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        self.required = []

class listNetworkACLsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the ACL Item"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the ID of the ACL this item belongs to"""
        self.aclid = None
        self.typeInfo['aclid'] = 'string'
        """Action of ACL Item. Allow/Deny"""
        self.action = None
        self.typeInfo['action'] = 'string'
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """the ending port of ACL's port range"""
        self.endport = None
        self.typeInfo['endport'] = 'string'
        """is rule for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """error code for this icmp message"""
        self.icmpcode = None
        self.typeInfo['icmpcode'] = 'integer'
        """type of the icmp message being sent"""
        self.icmptype = None
        self.typeInfo['icmptype'] = 'integer'
        """Number of the ACL Item"""
        self.number = None
        self.typeInfo['number'] = 'integer'
        """the protocol of the ACL"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the starting port of ACL's port range"""
        self.startport = None
        self.typeInfo['startport'] = 'string'
        """the state of the rule"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the traffic type for the ACL"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        """the list of resource tags associated with the network ACLs"""
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

