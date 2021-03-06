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
import openerp.addons.web.http as openerpweb
from openerp.pooler import RegistryManager
import simplejson
import base64
import urllib2
from cStringIO import StringIO
import csv


class ChartD3(openerpweb.Controller):

    _cp_path = '/web/chartd3'

    @openerpweb.jsonrequest
    def autocomplete_data(self, request, model=None, searchText=None):
        obj = request.session.model(model)
        context = request.context
        registry = RegistryManager.get(request.session._db)
        if hasattr(registry.get(model), 'autocomplete_data'):
            return obj.autocomplete_data(
                model, searchText, context=context)

        view = request.session.model('ir.ui.view.chart.d3')
        return view.autocomplete_data(
            model, searchText, context=context)

    @openerpweb.jsonrequest
    def get_data(self, request, model=None, xaxis=None, yaxis=None, domain=None,
                 group_by=None, options=None,product=None,start_date=None,end_date=None):
        if domain is None:
            domain = []

        if group_by is None:
            group_by = []

        if options is None:
            options = {}

        obj = request.session.model(model)
        context = request.context
        registry = RegistryManager.get(request.session._db)
        if hasattr(registry.get(model), 'chart_d3_get_data'):
            return obj.chart_d3_get_data(
                xaxis, yaxis, domain, group_by, options,product,start_date,end_date,context=context)

        view = request.session.model('ir.ui.view.chart.d3')
        return view.get_data(
            model, xaxis, yaxis, domain, group_by, options, product,start_date,end_date,context=context)

    def content_disposition(self,request,filename):
        filename = filename.encode('utf8')
        escaped = urllib2.quote(filename)
        browser = request.httprequest.user_agent.browser
        version = int((request.httprequest.user_agent.version or '0').split('.')[0])
        if browser == 'msie' and version < 9:
            return "attachment; filename=%s" % escaped
        elif browser == 'safari':
            return "attachment; filename=%s" % filename
        else:
            return "attachment; filename*=UTF-8''%s" % escaped

    def from_data(self, fields, rows):
        fp = StringIO()
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)

        writer.writerow([name.encode('utf-8') for name in fields])

        for data in rows:
            row = []
            for d in data:
                if isinstance(d, basestring):
                    d = d.replace('\n',' ').replace('\t',' ')
                    try:
                        d = d.encode('utf-8')
                    except UnicodeError:
                        pass
                if d is False: d = None
                row.append(d)
            writer.writerow(row)

        fp.seek(0)
        data = fp.read()
        fp.close()
        return data

    @openerpweb.httprequest
    def export(self, request, data, token):
        kwargs = simplejson.loads(data)
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        model = kwargs.get('model')
        obj = request.session.model(model)
        registry = RegistryManager.get(request.session._db)
        if hasattr(registry.get(model), 'export_data'):
            data = obj.export_data(
                start_date,end_date)
            header = obj.export_header(
                start_date,end_date)
            return request.make_response(self.from_data(header, data),
                headers=[('Content-Disposition',
                            self.content_disposition(request,"ChartData.csv")),
                        ('Content-Type', 'text/csv;charset=utf8')],
                cookies={'fileToken': token})
        raise osv.except_osv(('Error'), ('Functionality not enabled'))
        # return request.make_response(self.from_data(header, data),
        #     headers=[('Content-Disposition',
        #                 self.content_disposition(self.filename(model))),
        #             ('Content-Type', self.content_type)],
        #     cookies={'fileToken': token})
