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


"""Creates a Network ACL for the given VPC"""
from baseCmd import *
from baseResponse import *
class createNetworkACLListCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """Name of the network ACL List"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Id of the VPC associated with this network ACL List"""
        """Required"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        """Description of the network ACL List"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """an optional field, whether to the display the list to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["name","vpcid",]

class createNetworkACLListResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the ACL"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Description of the ACL"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """is ACL for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the Name of the ACL"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Id of the VPC this ACL is associated with"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'

