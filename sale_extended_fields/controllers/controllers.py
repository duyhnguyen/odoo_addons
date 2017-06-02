# -*- coding: utf-8 -*-
from odoo import http

# class Partnerfield(http.Controller):
#     @http.route('/partnerfield/partnerfield/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partnerfield/partnerfield/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partnerfield.listing', {
#             'root': '/partnerfield/partnerfield',
#             'objects': http.request.env['partnerfield.partnerfield'].search([]),
#         })

#     @http.route('/partnerfield/partnerfield/objects/<model("partnerfield.partnerfield"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partnerfield.object', {
#             'object': obj
#         })