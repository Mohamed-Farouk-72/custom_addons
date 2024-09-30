# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def action_create_payment(self):
        """ Action Create Payment """
        unique_currencies = []
        for rec in self:
            if rec.contract_id.currency_id.id not in unique_currencies:
                unique_currencies.append(rec.contract_id.currency_id.id)
        unique_currencies = list(set(unique_currencies))
        if len(unique_currencies) > 1:
            raise ValidationError(_("All Payslips must have the same currency."))
        else:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Create Payment',
                'res_model': 'create.payment.wizard',
                'view_type': 'form',
                'view_mode': 'form',
                'view_id': self.env.ref('payroll_customize.create_payment_wizard_form').id,
                'target': 'new',
                'context': {'default_hr_payslip_ids': self.ids,
                            'default_currency_id': unique_currencies[0],
                            'default_previous_currency_id': unique_currencies[0]},

            }
