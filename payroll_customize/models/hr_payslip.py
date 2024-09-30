# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def action_create_payment(self):
        """ Action Create Payment """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Create Payment',
            'res_model': 'create.payment.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': self.env.ref('payroll_customize.create_payment_wizard_form').id,
            'target': 'new',
            'context': {'default_hr_payslip_ids': self.ids},

        }
