# -*- coding: utf-8 -*-
{
    'name': "Módulo Inventario",

    'summary': """
        Sistema de inventario Restaurante PABAKA""",

    'description': """
         Módulo que permite la administración del inventario del Restaurante PABAKA
    """,

    'author': "picrack",
    'website': "https://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'insurance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
         'views/view_insumos.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
