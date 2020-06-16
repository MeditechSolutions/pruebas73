# -*- coding: utf-8 -*-

{
    'name' : 'S2U Online Appointment Extension',
    'version' : '1.0.0',
    'author' : 'MSTECH',
    'category' : 'Technical Configuration',
    'summary': 'S2U Online Appointment Extension',
    'description' : """
S2U Online Appointment Extension
    """,
    'website': 'http://www.mstech.pe',
    'depends' : [
        's2u_online_appointment',
        'basic_hms',
        'sinerkia_jitsi_meet'
    ],
    'data': [
        'data/calendar_data.xml',
        'views/appointment_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 1,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
