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
{
    'name': 'NV-D3 Line Chart',
    'version': '0.0.1',
    'sequence': 101,
    'category': 'Charts',
    'description': """
        Used d3 chart module from http://anybox.fr as a starting point. This module draws only line charts
    """,
    'author': 'Sandeep',
    'website': 'www.nuchange.com',
    'depends': [
        'base',
        'web',
        'web_graph',
    ],
    'data': [
    ],
    'js': [
        'static/lib/canvg/rgbcolor.js',
        'static/lib/canvg/StackBlur.js',
        'static/lib/canvg/canvg.js',
        'static/lib/d3.min.js',
        'static/lib/d3_chart.js',
        'static/src/js/view_d3.js',
    ],
    'qweb': [
        'static/src/xml/view_d3.xml',
    ],
    'css': [
        'static/lib/d3_chart.css',
        'static/src/css/view_d3.css',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
