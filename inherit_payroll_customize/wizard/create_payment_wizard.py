from odoo import models, fields, api, _, exceptions


class CreatePaymentWizard(models.TransientModel):
    _inherit = 'create.payment.wizard'

    previous_currency_id = fields.Many2one('res.currency', 'Currency',
                                           default=lambda self: self.env.user.company_id.currency_id.id, store=True)
    ignore_first_onchange = fields.Boolean(default=True)

    @api.onchange('currency_id')
    def onchange_currency_id(self):
        for wizard in self:
            if wizard.ignore_first_onchange:
                wizard.ignore_first_onchange = False
                return
            elif wizard.currency_id and not wizard.ignore_first_onchange:
                if wizard.currency_id.id != self.env.user.company_id.currency_id.id:
                    if wizard.previous_currency_id.id != self.env.user.company_id.currency_id.id and wizard.currency_id.id != self.env.user.company_id.currency_id.id:
                        default_currency_rate = \
                            wizard.previous_currency_id.rate_ids.sorted(key=lambda r: r.name, reverse=True)[
                                0].inverse_company_rate
                        wizard.amount = wizard.amount / default_currency_rate
                    wizard.amount = wizard.amount * wizard.currency_id.rate
                else:
                    wizard.amount = wizard.amount / wizard.previous_currency_id.rate
                wizard.previous_currency_id = wizard.currency_id.id