# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management App',
    'version': '13.0.1.0',
    'category': 'Healthcare',
    'summary': 'An app for management of Hospitals',
    'description': """
    An app for mamagement of Hospitals
    """,
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/doctor_wizard_views.xml',
        'wizard/patient_wizard_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/treatment_views.xml',
        'views/invoice_views.xml',
        'views/sale_views.xml',
        'views/doc_inherit.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
