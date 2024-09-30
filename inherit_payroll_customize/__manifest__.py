
{
    'name': 'Inherit Payroll Customize',
    'summary': '',
    'author': "   ",
    'company': ' ',
    'website': " ",
    'version': '17.0',
    'category': '',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'payroll_customize',
        'account',
        'hr',
        'om_hr_payroll',
    ],
    'data': [
        'wizard/create_payment_wizard_view.xml',
        'views/hr_contract.xml',
    ],
    'demo': [
        # 'demo/',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

