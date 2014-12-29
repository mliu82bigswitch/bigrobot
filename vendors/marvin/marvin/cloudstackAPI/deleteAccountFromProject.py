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


"""Deletes account from the project"""
from baseCmd import *
from baseResponse import *
class deleteAccountFromProjectCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """name of the account to be removed from the project"""
        """Required"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """id of the project to remove the account from"""
        """Required"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["account","projectid",]

class deleteAccountFromProjectResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

