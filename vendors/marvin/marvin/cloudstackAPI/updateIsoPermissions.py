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


"""Updates iso permissions"""
from baseCmd import *
from baseResponse import *
class updateIsoPermissionsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the template ID"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """a comma delimited list of accounts. If specified, "op" parameter has to be passed in."""
        self.accounts = []
        self.typeInfo['accounts'] = 'list'
        """true if the template/iso is extractable, false other wise. Can be set only by root admin"""
        self.isextractable = None
        self.typeInfo['isextractable'] = 'boolean'
        """true for featured template/iso, false otherwise"""
        self.isfeatured = None
        self.typeInfo['isfeatured'] = 'boolean'
        """true for public template/iso, false for private templates/isos"""
        self.ispublic = None
        self.typeInfo['ispublic'] = 'boolean'
        """permission operator (add, remove, reset)"""
        self.op = None
        self.typeInfo['op'] = 'string'
        """a comma delimited list of projects. If specified, "op" parameter has to be passed in."""
        self.projectids = []
        self.typeInfo['projectids'] = 'list'
        self.required = ["id",]

class updateIsoPermissionsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

