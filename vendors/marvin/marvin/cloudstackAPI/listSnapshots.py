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


"""Lists all available snapshots for the account."""
from baseCmd import *
from baseResponse import *
class listSnapshotsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """lists snapshot by snapshot ID"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """valid values are HOURLY, DAILY, WEEKLY, and MONTHLY."""
        self.intervaltype = None
        self.typeInfo['intervaltype'] = 'string'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """lists snapshot by snapshot name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """valid values are MANUAL or RECURRING."""
        self.snapshottype = None
        self.typeInfo['snapshottype'] = 'string'
        """List resources by tags (key/value pairs)"""
        self.tags = []
        self.typeInfo['tags'] = 'map'
        """the ID of the disk volume"""
        self.volumeid = None
        self.typeInfo['volumeid'] = 'uuid'
        """list snapshots by zone id"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = []

class listSnapshotsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """ID of the snapshot"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account associated with the snapshot"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the date the snapshot was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the domain name of the snapshot's account"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the snapshot's account"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """valid types are hourly, daily, weekly, monthy, template, and none."""
        self.intervaltype = None
        self.typeInfo['intervaltype'] = 'string'
        """name of the snapshot"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the project name of the snapshot"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the snapshot"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """indicates whether the underlying storage supports reverting the volume to this snapshot"""
        self.revertable = None
        self.typeInfo['revertable'] = 'boolean'
        """the type of the snapshot"""
        self.snapshottype = None
        self.typeInfo['snapshottype'] = 'string'
        """the state of the snapshot. BackedUp means that snapshot is ready to be used; Creating - the snapshot is being allocated on the primary storage; BackingUp - the snapshot is being backed up on secondary storage"""
        self.state = None
        self.typeInfo['state'] = 'state'
        """ID of the disk volume"""
        self.volumeid = None
        self.typeInfo['volumeid'] = 'string'
        """name of the disk volume"""
        self.volumename = None
        self.typeInfo['volumename'] = 'string'
        """type of the disk volume"""
        self.volumetype = None
        self.typeInfo['volumetype'] = 'string'
        """id of the availability zone"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the list of resource tags associated with snapshot"""
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

