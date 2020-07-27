# -*- coding: utf-8 -*-

{
    'name': 'Student App',
    'version': '13.0.1.0',
    'category': 'Student',
    'summary': 'My First App',
    'description': """
    My First App
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
