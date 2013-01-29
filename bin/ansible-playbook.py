# (C) 2012, Michael DeHaan, <michael.dehaan@gmail.com>

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

#######################################################

# This file is a windows-only simple proxy for the 'ansible' script. The windows
# version of the 'mutliprocessing' module can only load scripts with a '.py' extension

import imp
from os import path
_ansibleplayook = imp.load_source('_ansibleplaybook',path.join(path.dirname(path.realpath(__file__)),'ansible-playbook'))
from _ansibleplaybook import *
if __name__ == "__main__":
    outer_main()