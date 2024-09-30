
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class EmployeeEntryDocuments(models.Model):
    _name = 'employee.checklist'
    _inherit = 'mail.thread'
    _description = "Employee Documents"



    name = fields.Char(string='Document Name', copy=False, required=1)
    document_type = fields.Selection([('entry', 'In'),
                                      ('exit', 'Out')], string='Checklist Type', required=1)