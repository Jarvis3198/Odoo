# -*- coding: utf-8 -*-

{
    'name': 'School Management App',
    'version': '13.0.1.0',
    'category': 'Education',
    'summary': 'An app for mamagement of students and teachers',
    'description': """
    An app for mamagement of students and teachers
    """,
    'depends': ['base', 'sale','account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/student_wizard_views.xml',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/subject_views.xml',
        'views/lunch_views.xml',
        'views/recess_views.xml',
        'views/sale_views.xml',
        'views/invoice_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
