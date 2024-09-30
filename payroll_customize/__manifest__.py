
{
    'name': 'Payroll Customize',
    'summary': 'Payroll Customize ',
    'author': "Ahmed Holiel",
    'company': '',
    'version': '17.0.0.1.0',
    'category': '',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'account',
        'hr',
        'om_hr_payroll',
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'report/',
        'wizard/create_payment_wizard_view.xml',
        'views/hr_payslip.xml',
        'views/hr_employee_view.xml',
        'views/employee_check_list_view.xml',
        # 'data/',
    ],
    'demo': [
        # 'demo/',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

