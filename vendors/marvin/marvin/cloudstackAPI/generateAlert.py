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


"""Generates an alert"""
from baseCmd import *
from baseResponse import *
class generateAlertCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """Alert description"""
        """Required"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """Name of the alert"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Type of the alert"""
        """Required"""
        self.type = None
        self.typeInfo['type'] = 'short'
        """Pod id for which alert is generated"""
        self.podid = None
        self.typeInfo['podid'] = 'uuid'
        """Zone id for which alert is generated"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["description","name","type",]

class generateAlertResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

