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


"""Lists affinity groups"""
from baseCmd import *
from baseResponse import *
class listAffinityGroupsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list the affinity group by the id provided"""
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
        """lists affinity groups by name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """lists affinity groups by type"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """lists affinity groups by virtual machine id"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'uuid'
        self.required = []

class listAffinityGroupsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the affinity group"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the affinity group"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the description of the affinity group"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """the domain name of the affinity group"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the affinity group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the name of the affinity group"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the type of the affinity group"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """virtual machine Ids associated with this affinity group"""
        self.virtualmachineIds = None
        self.typeInfo['virtualmachineIds'] = 'list'

