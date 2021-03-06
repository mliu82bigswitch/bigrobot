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


"""Updates a vm group"""
from baseCmd import *
from baseResponse import *
class updateInstanceGroupCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """Instance group ID"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """new instance group name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        self.required = ["id",]

class updateInstanceGroupResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the id of the instance group"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account owning the instance group"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """time and date the instance group was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the domain name of the instance group"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the instance group"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the name of the instance group"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project name of the group"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the group"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'

