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


"""Lists autoscale policies."""
from baseCmd import *
from baseResponse import *
class listAutoScalePoliciesCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the action to be executed if all the conditions evaluate to true for the specified duration."""
        self.action = None
        self.typeInfo['action'] = 'string'
        """the ID of the condition of the policy"""
        self.conditionid = None
        self.typeInfo['conditionid'] = 'uuid'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """the ID of the autoscale policy"""
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
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """the ID of the autoscale vm group"""
        self.vmgroupid = None
        self.typeInfo['vmgroupid'] = 'uuid'
        self.required = []

class listAutoScalePoliciesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the autoscale policy ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the autoscale policy"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the action to be executed if all the conditions evaluate to true for the specified duration."""
        self.action = None
        self.typeInfo['action'] = 'string'
        """the list of IDs of the conditions that are being evaluated on every interval"""
        self.conditions = None
        self.typeInfo['conditions'] = 'list'
        """the domain name of the autoscale policy"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the autoscale policy"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the duration for which the conditions have to be true before action is taken"""
        self.duration = None
        self.typeInfo['duration'] = 'integer'
        """the project name of the autoscale policy"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id autoscale policy"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the cool down period for which the policy should not be evaluated after the action has been taken"""
        self.quiettime = None
        self.typeInfo['quiettime'] = 'integer'

