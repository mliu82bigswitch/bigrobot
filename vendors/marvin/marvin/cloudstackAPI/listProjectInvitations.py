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


"""Lists project invitations and provides detailed information for listed invitations"""
from baseCmd import *
from baseResponse import *
class listProjectInvitationsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """if true, list only active invitations - having Pending state and ones that are not timed out yet"""
        self.activeonly = None
        self.typeInfo['activeonly'] = 'boolean'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list invitations by id"""
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
        """list by project id"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """list invitations by state"""
        self.state = None
        self.typeInfo['state'] = 'string'
        self.required = []

class listProjectInvitationsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the id of the invitation"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account name of the project's owner"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain name where the project belongs to"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id the project belongs to"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the email the invitation was sent to"""
        self.email = None
        self.typeInfo['email'] = 'string'
        """the name of the project"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the id of the project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the invitation state"""
        self.state = None
        self.typeInfo['state'] = 'string'

