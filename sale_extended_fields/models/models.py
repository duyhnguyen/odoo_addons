# -*- coding: utf-8 -*-

from odoo import models, fields


class sale_extended_fields(models.Model):
    _inherit = "sale.order"

    donor1_name = fields.Char(string='Họ và tên')
    donor1_sex = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], string='Giới tính')
    donor1_dob = fields.Date(string='Ngày sinh')
    donor1_nationality = fields.Many2one('res.country', string='Quốc tịch', default=lambda self: self.env['res.country'].search([('name', '=', 'Vietnam')]))
    donor1_relationship = fields.Char(string='Quan hệ')
    donor1_sample_type = fields.Char(string='Loại mẫu')
    donor1_sample_date = fields.Date(string='Ngày thu')
    donor1_sample_collector = fields.Many2one('res.users', string='Người thu mẫu', track_visibility='onchange', default=lambda self: self.env.user)
    donor1_id_type = fields.Selection([('passport', 'Hộ chiếu'), ('cmnd', 'CMND'), ('birth_cert', 'Giấy khai sinh')], string='Loại giấy tờ')
    donor1_id_issue = fields.Date(string='Ngày cấp')
    donor1_id_no = fields.Char(string='Số')
    donor1_id_exp = fields.Date(string='Ngày hết hạn')
    donor1_id_issue_place = fields.Char(string='Nơi cấp')
    donor1_guardian = fields.Char(string='Người giám hộ')
    donor1_guardian_rel = fields.Char(string='Quan hệ')

    donor2_name = fields.Char(string='Họ và tên')
    donor2_sex = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], string='Giới tính')
    donor2_dob = fields.Date(string='Ngày sinh')
    donor2_nationality = fields.Many2one('res.country', string='Quốc tịch',
                                         default=lambda self: self.env['res.country'].search(
                                             [('name', '=', 'Vietnam')]))
    donor2_relationship = fields.Char(string='Quan hệ')
    donor2_sample_type = fields.Char(string='Loại mẫu')
    donor2_sample_date = fields.Date(string='Ngày thu')
    donor2_sample_collector = fields.Many2one('res.users', string='Người thu mẫu', track_visibility='onchange', default=lambda self: self.env.user)
    donor2_id_type = fields.Selection([('passport', 'Hộ chiếu'), ('cmnd', 'CMND'), ('birth_cert', 'Giấy khai sinh')], string='Loại giấy tờ')
    donor2_id_issue = fields.Date(string='Ngày cấp')
    donor2_id_no = fields.Char(string='Số')
    donor2_id_exp = fields.Date(string='Ngày hết hạn')
    donor2_id_issue_place = fields.Char(string='Nơi cấp')
    donor2_guardian = fields.Char(string='Người giám hộ')
    donor2_guardian_rel = fields.Char(string='Quan hệ')

    donor3_name = fields.Char(string='Họ và tên')
    donor3_sex = fields.Selection([('male', 'Nam'), ('female', 'Nữ')], string='Giới tính')
    donor3_dob = fields.Date(string='Ngày sinh')
    donor3_nationality = fields.Many2one('res.country', string='Quốc tịch',
                                         default=lambda self: self.env['res.country'].search(
                                             [('name', '=', 'Vietnam')]))
    donor3_relationship = fields.Char(string='Quan hệ')
    donor3_sample_type = fields.Char(string='Loại mẫu')
    donor3_sample_date = fields.Date(string='Ngày thu')
    donor3_sample_collector = fields.Many2one('res.users', string='Người thu mẫu', track_visibility='onchange', default=lambda self: self.env.user)
    donor3_id_type = fields.Selection([('passport', 'Hộ chiếu'), ('cmnd', 'CMND'), ('birth_cert', 'Giấy khai sinh')], string='Loại giấy tờ')
    donor3_id_issue = fields.Date(string='Ngày cấp')
    donor3_id_no = fields.Char(string='Số')
    donor3_id_exp = fields.Date(string='Ngày hết hạn')
    donor3_id_issue_place = fields.Char(string='Nơi cấp')
    donor3_guardian = fields.Char(string='Người giám hộ')
    donor3_guardian_rel = fields.Char(string='Quan hệ')

