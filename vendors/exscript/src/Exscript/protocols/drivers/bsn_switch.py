# Copyright (C) 2007-2010 Samuel Abels.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""
A driver for Big Switch SwitchLight. This was borrowed from ios.py.
"""
import re
from Exscript.protocols.drivers.driver import Driver

_user_re = [re.compile(r'user ?name: ?$', re.I)]
_password_re = [re.compile(r'(?:[\r\n]Password: ?|last resort password:)$')]
_tacacs_re = re.compile(r'[\r\n]s\/key[\S ]+\r?%s' % _password_re[0].pattern)

# Original for Cisco
# _prompt_re   = [re.compile(r'[\r\n][\-\w+\.:/]+(?:\([^\)]+\))?[>#] ?$')]

# Expected prompts:
#   CLI:     qa-1-leaf-1>
#
# _prompt_re = [re.compile(r'[\r\n](\w+(-?\w+)?\s?@?)?[\-\w+\.:/]+(?:\([^\)]+\))?(:~)?[>#$] ?$')]

# Special case:
#  Bash:      root@kk-spine01:~#
#            ^ note the extra space
#              See https://bigswitch.atlassian.net/browse/PAN-772

_prompt_re = [re.compile(r'[\r\n]\s?\[?(\w+(-?\w+)?\s?@?)?[\-\w+\.:/]+(?:\([^\)]+\))?(:~)?( ~\])?[>#$] ?$')]


# SwitchLight errors:
#  Error: Invalid argument: Invalid datapath id (64-bit hex value): 11:22:GG:33:44
_error_re = [re.compile(r'%Error'),
             re.compile(r'invalid argument', re.I),
             re.compile(r'invalid input', re.I),
             re.compile(r'(?:incomplete|ambiguous) command', re.I),
             re.compile(r'connection timed out', re.I),
             re.compile(r'[^\r\n]+ not found', re.I)]


class BsnSwitchDriver(Driver):
    def __init__(self):
        Driver.__init__(self, 'bsn_switch')
        self.user_re = _user_re
        self.password_re = _password_re
        self.prompt_re = _prompt_re
        self.error_re = _error_re

        # BSN tweak to specify what platform this device is.
        self._platform = None

    def check_head_for_os(self, string):
        # print("string: %s" % string)
        if 'SwitchLight' in string or 'Switch Light' in string:
            self._platform = 'switchlight'
            return 90
        if _tacacs_re.search(string):
            return 50
        if _user_re[0].search(string):
            return 30
        return 0

    def init_terminal(self, conn):
        pass

    # def auto_authorize(self, conn, account, flush, bailout):
    #    conn.send('enable\r')
    #    conn.app_authorize(account, flush, bailout)

    # BSN tweaks - all methods below
    def platform(self):
        return self._platform
