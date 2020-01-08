# -*- coding: utf-8 -*-
{ 
    'name': 'Library Management', 
    'description': 'Manage library book catalogue and lending.', 
    'author': 'Daniel Reis', 
    'depends': ['base'], 
    "installable": True,
    'application': True, 
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',

    ],
}
