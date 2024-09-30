
{
    'name': ' Sale Order Customize ',
    'description': 'Edit In Sale Order',
    'author': "Ahmed Holiel",
    'company': '',
    'website': "",
    'version': '17.0.0.1.0',
    'category': '',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'sale',
        'account',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'report/',
        # 'wizard/',
        'views/sale_order.xml',
        'views/account_move.xml',
        # 'data/',
    ],
    'demo': [
        # 'demo/',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

