
{'name': 'Company Management',
 'description': 'Company',
 'depends': ['base', 'hr'],
 'data': [
     'security/company_security.xml',
     'security/ir.model.access.csv',
     'views/company_menu.xml',
     'views/employee_building_assignment.xml',
     'views/fm_building_views.xml'

 ],
 'application': False,
 'installable': True,
 }