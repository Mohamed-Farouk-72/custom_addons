from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    partner_id = fields.Many2one('res.partner')
    exit_checklist = fields.Many2many('employee.checklist', 'exit_obj', 'exit_hr_rel', 'hr_exit_rel',
                                      string='Out',readonly=False,
                                      compute='_documents_entry_vals',
                                      domain="[('document_type', '=', 'exit')]")

    entry_checklist = fields.Many2many('employee.checklist', 'entry_obj', 'check_hr_rel', 'hr_check_rel',
                                       string='IN',
                                       compute='_documents_entry_vals',readonly=False,
                                       domain="[('document_type', '=', 'entry')]")

    def _documents_entry_vals(self):
        for rec in self:
            checklist = self.env['employee.checklist'].search([])
            for c in checklist:
                if c.document_type == 'entry':
                    self.write({'entry_checklist': [(4, c.name)]})
                if c.document_type == 'exit':
                    self.write({'exit_checklist': [(4, c.name)]})