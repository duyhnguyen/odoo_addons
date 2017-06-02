# -*- coding: utf-8 -*-
{
    'name': "sale_extended_fields",

    'summary': """
        Thêm field cho form tạo order mới""",

    'description': """
        Thêm field cho form tạo order mới
        - thông tin người cho mẫu
    """,

    'author': "Tí Rắn",
    'website': "http://www.idna.com.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}