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


"""List the counters"""
from baseCmd import *
from baseResponse import *
class listCountersCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """ID of the Counter."""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """Name of the counter."""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """Source of the counter."""
        self.source = None
        self.typeInfo['source'] = 'string'
        self.required = []

class listCountersResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the id of the Counter"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Name of the counter."""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Source of the counter."""
        self.source = None
        self.typeInfo['source'] = 'string'
        """Value in case of snmp or other specific counters."""
        self.value = None
        self.typeInfo['value'] = 'string'
        """zone id of counter"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'

