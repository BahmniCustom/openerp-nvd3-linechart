##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class ChartD3Color(osv.AbstractModel):
    _name = 'chart_d3.color'
    _description = 'Chart d3 color'

    _columns = {
        'color': fields.char(
            u"Couleur", size=64,
            help=u"Toutes couleur valid css, exemple blue ou #f57900"),
    }

    def chart_d3_get_color(self, cr, uid, ids, model, fields_get, context=None):
        colors = self.read(cr, uid, ids, ['color'], context=context)
        colors = [(x['id'], x['color']) for x in colors if x['color']]
        return dict(colors)
