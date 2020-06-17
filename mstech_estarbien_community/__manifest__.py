# -*- coding: utf-8 -*-

{
    'name' : 'Clínica Estarbien - Odoo',
    'version' : '1.0.0',
    'author' : 'MSTECH',
    'category' : 'Technical Configuration',
    'summary': 'Clínica Estarbien - Odoo.',
    'description' : """
Módulo de personalización de la Clínica Estarbien en Odoo
    """,
    'website': 'http://www.mstech.pe',
    'depends' : ['base','basic_hms'],
    'data': [
        'security/ir.model.access.csv',
        'views/medicina_cita_views.xml',
        'views/medicina_cita_medicina_views.xml',
        'views/medicina_cita_dermatologia_views.xml',
        'views/medicina_cita_grandes_alturas_views.xml',
        'views/medicina_cita_altura_views.xml',
        'views/medicina_cita_confinados_views.xml',
        'views/medicina_cita_electrocardiograma_views.xml',
        'views/medicina_cita_oftalmologia_views.xml',
        'views/medicina_cita_audiometria_views.xml',
        'views/medicina_cita_psicologia_views.xml',
        'views/medicina_cita_odontograma_views.xml',
        'views/medicina_cita_musculo_esqueletico_views.xml',
        'views/medicina_cita_radiologia_views.xml',
        #'views/medicina_cita_espirometria_views.xml',
        'views/medicina_cita_tsr_views.xml',
        'views/medicina_cita_laboratorio_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    "sequence": 1,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
