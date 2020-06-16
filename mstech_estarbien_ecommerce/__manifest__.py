# -*- coding: utf-8 -*-
{
    'name': 'Proyecto - Ventas MSTECH',
    'description': "Integración pryecto - ventas para el ecommerce de Estarbien",
    'author': "MSTECH",
    'website': "https://www.mstech.pe",
    'summary': "Integración pryecto - ventas para el ecommerce de Estarbien",
    'version': '13.0.1.0.0',
    'depends': [
        'sale_timesheet',
        'basic_hms',
    ],
    'data': [
        'data/project_data.xml',
        'security/estarbien_security.xml',
        'security/ir.model.access.csv',
        #'views/medical_patient_views.xml',
        'views/product_views.xml',
        'views/project_views.xml',
    ],
    'installable': True,
    'sequence': 1,
}