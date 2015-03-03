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


"""Add a new guest OS type"""
from baseCmd import *
from baseResponse import *
class addGuestOsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """ID of Guest OS category"""
        """Required"""
        self.oscategoryid = None
        self.typeInfo['oscategoryid'] = 'uuid'
        """Unique display name for Guest OS"""
        """Required"""
        self.osdisplayname = None
        self.typeInfo['osdisplayname'] = 'string'
        """Optional name for Guest OS"""
        self.name = None
        self.typeInfo['name'] = 'string'
        self.required = ["oscategoryid","osdisplayname",]

class addGuestOsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the OS type"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the name/description of the OS type"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """is the guest OS user defined"""
        self.isuserdefined = None
        self.typeInfo['isuserdefined'] = 'string'
        """the ID of the OS category"""
        self.oscategoryid = None
        self.typeInfo['oscategoryid'] = 'string'

