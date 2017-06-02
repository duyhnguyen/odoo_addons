# -*- coding: utf-8 -*-
from odoo import http

# class PartnerExtendedFields(http.Controller):
#     @http.route('/partner_extended_fields/partner_extended_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_extended_fields/partner_extended_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_extended_fields.listing', {
#             'root': '/partner_extended_fields/partner_extended_fields',
#             'objects': http.request.env['partner_extended_fields.partner_extended_fields'].search([]),
#         })

#     @http.route('/partner_extended_fields/partner_extended_fields/objects/<model("partner_extended_fields.partner_extended_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_extended_fields.object', {
#             'object': obj
#         })