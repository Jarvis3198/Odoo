# -*- coding: utf-8 -*-

{
    'name': 'Teacher App',
    'version': '13.0.1.0',
    'category': 'Teacher',
    'summary': 'My Second App',
    'description': """
    My Second App
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/teacher_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
