# -*- encoding: utf-8 -*-
########################################################################
#
#   OOOP, OpenObject On Python
#   Copyright (C) 2010 Impulzia S.L. All Rights Reserved.
#   Gamaliel Toro <argami@impulzia.com>
#   $Id$
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
from __future__ import nested_scopes
import new

from osv import osv, fields
from ooop import OOOP

class impulzia_ooop(osv.osv_memory):
    """ OOOP."""
    _name = "impulzia.ooop"
    _description = "ooop wrapper to bypass the orm"
    
    def get(self, *args):
        return OOOP(parent=args[0], cr=args[1], uid=args[2])
    

impulzia_ooop()


def add_ooop(cls):
    def ooop(self, cr, uid):
        if not self.__dict__.has_key('_ooop'):
            self._ooop = OOOP(parent=self, cr=cr, uid=uid)
        return self._ooop
            
    ooop.__doc__ = "set ooop funtion to call self.ooop(cr, cursor)" 
    ooop.__name__ = "ooop"
    setattr(cls,ooop.__name__,ooop)




add_ooop(osv.osv_base)