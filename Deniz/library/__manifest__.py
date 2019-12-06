# -*- coding: utf-8 -*-

{
    'name' : 'Library Management',
    'depends' : ['base'],
    'description': 'Books,members and borrowed books.',
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],

    'installable': True,
    'application': True,
}
