# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner_extended_fields(models.Model):
    _inherit = "res.partner"

    birthdate = fields.Date("Ngày sinh")
    gender = fields.Selection([('male', 'Nam'),
                               ('female', 'Nữ')], string='Giới tính')
    nationality = fields.Many2one('res.country', string='Quốc tịch', default=lambda self: self.env['res.country'].search([('name','=','Vietnam')]))
    password = fields.Char("Mật khẩu")
    report_receive_via = fields.Selection([('self-collect', 'Tự đến lấy'),
                                           ('EMS', 'EMS'),
                                           ('Phone', 'Phone'),
                                           ('Email', 'Email')], string='Nhận kết quả')


