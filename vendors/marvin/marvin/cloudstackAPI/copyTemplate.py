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


"""Copies a template from one zone to another."""
from baseCmd import *
from baseResponse import *
class copyTemplateCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """Template ID."""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """ID of the zone the template is being copied to."""
        """Required"""
        self.destzoneid = None
        self.typeInfo['destzoneid'] = 'uuid'
        """ID of the zone the template is currently hosted on. If not specified and template is cross-zone, then we will sync this template to region wide image store."""
        self.sourcezoneid = None
        self.typeInfo['sourcezoneid'] = 'uuid'
        self.required = ["id","destzoneid",]

class copyTemplateResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the template ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account name to which the template belongs"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the account id to which the template belongs"""
        self.accountid = None
        self.typeInfo['accountid'] = 'string'
        """true if the ISO is bootable, false otherwise"""
        self.bootable = None
        self.typeInfo['bootable'] = 'boolean'
        """checksum of the template"""
        self.checksum = None
        self.typeInfo['checksum'] = 'string'
        """the date this template was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """true if the template is managed across all Zones, false otherwise"""
        self.crossZones = None
        self.typeInfo['crossZones'] = 'boolean'
        """additional key/value details tied with template"""
        self.details = None
        self.typeInfo['details'] = 'map'
        """the template display text"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """the name of the domain to which the template belongs"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the ID of the domain to which the template belongs"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the format of the template."""
        self.format = None
        self.typeInfo['format'] = 'imageformat'
        """the ID of the secondary storage host for the template"""
        self.hostid = None
        self.typeInfo['hostid'] = 'string'
        """the name of the secondary storage host for the template"""
        self.hostname = None
        self.typeInfo['hostname'] = 'string'
        """the hypervisor on which the template runs"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """true if template contains XS/VMWare tools inorder to support dynamic scaling of VM cpu/memory"""
        self.isdynamicallyscalable = None
        self.typeInfo['isdynamicallyscalable'] = 'boolean'
        """true if the template is extractable, false otherwise"""
        self.isextractable = None
        self.typeInfo['isextractable'] = 'boolean'
        """true if this template is a featured template, false otherwise"""
        self.isfeatured = None
        self.typeInfo['isfeatured'] = 'boolean'
        """true if this template is a public template, false otherwise"""
        self.ispublic = None
        self.typeInfo['ispublic'] = 'boolean'
        """true if the template is ready to be deployed from, false otherwise."""
        self.isready = None
        self.typeInfo['isready'] = 'boolean'
        """the template name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the ID of the OS type for this template."""
        self.ostypeid = None
        self.typeInfo['ostypeid'] = 'string'
        """the name of the OS type for this template."""
        self.ostypename = None
        self.typeInfo['ostypename'] = 'string'
        """true if the reset password feature is enabled, false otherwise"""
        self.passwordenabled = None
        self.typeInfo['passwordenabled'] = 'boolean'
        """the project name of the template"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the template"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the date this template was removed"""
        self.removed = None
        self.typeInfo['removed'] = 'date'
        """the size of the template"""
        self.size = None
        self.typeInfo['size'] = 'long'
        """the template ID of the parent template if present"""
        self.sourcetemplateid = None
        self.typeInfo['sourcetemplateid'] = 'string'
        """true if template is sshkey enabled, false otherwise"""
        self.sshkeyenabled = None
        self.typeInfo['sshkeyenabled'] = 'boolean'
        """the status of the template"""
        self.status = None
        self.typeInfo['status'] = 'string'
        """the tag of this template"""
        self.templatetag = None
        self.typeInfo['templatetag'] = 'string'
        """the type of the template"""
        self.templatetype = None
        self.typeInfo['templatetype'] = 'string'
        """the ID of the zone for this template"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the name of the zone for this template"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'
        """the list of resource tags associated with tempate"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        self.typeInfo['jobid'] = ''
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = ''

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

