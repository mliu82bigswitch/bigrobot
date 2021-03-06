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


"""Lists capabilities"""
from baseCmd import *
from baseResponse import *
class listCapabilitiesCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        self.required = []

class listCapabilitiesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """true if regular user is allowed to create projects"""
        self.allowusercreateprojects = None
        self.typeInfo['allowusercreateprojects'] = 'boolean'
        """time interval (in seconds) to reset api count"""
        self.apilimitinterval = None
        self.typeInfo['apilimitinterval'] = 'integer'
        """Max allowed number of api requests within the specified interval"""
        self.apilimitmax = None
        self.typeInfo['apilimitmax'] = 'integer'
        """version of the cloud stack"""
        self.cloudstackversion = None
        self.typeInfo['cloudstackversion'] = 'string'
        """maximum size that can be specified when create disk from disk offering with custom size"""
        self.customdiskofferingmaxsize = None
        self.typeInfo['customdiskofferingmaxsize'] = 'long'
        """minimum size that can be specified when create disk from disk offering with custom size"""
        self.customdiskofferingminsize = None
        self.typeInfo['customdiskofferingminsize'] = 'long'
        """true if snapshot is supported for KVM host, false otherwise"""
        self.kvmsnapshotenabled = None
        self.typeInfo['kvmsnapshotenabled'] = 'boolean'
        """If invitation confirmation is required when add account to project"""
        self.projectinviterequired = None
        self.typeInfo['projectinviterequired'] = 'boolean'
        """true if region wide secondary is enabled, false otherwise"""
        self.regionsecondaryenabled = None
        self.typeInfo['regionsecondaryenabled'] = 'boolean'
        """true if security groups support is enabled, false otherwise"""
        self.securitygroupsenabled = None
        self.typeInfo['securitygroupsenabled'] = 'boolean'
        """true if region supports elastic load balancer on basic zones"""
        self.supportELB = None
        self.typeInfo['supportELB'] = 'string'
        """true if user and domain admins can set templates to be shared, false otherwise"""
        self.userpublictemplateenabled = None
        self.typeInfo['userpublictemplateenabled'] = 'boolean'

