from odoo import models, fields, api, _, exceptions


class CreatePaymentWizard(models.TransientModel):
    _name = 'create.payment.wizard'

    journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Journal",
        domain="[('type','in',['cash','bank'])]"
    )
    payment_method_line_id = fields.Many2one(
        'account.payment.method.line',
        # compute='_compute_payment_method_line_id',
        string='Payment Method',
    )
    payment_date = fields.Date(string="Payment Date", required=True,
                               default=fields.Date.today(),
                               )
    amount = fields.Monetary(currency_field='currency_id', store=True,
                             readonly=False,
                             compute='_compute_amount'
                             )

    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index = 1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, store=True)
    hr_payslip_ids = fields.Many2many(
        'hr.payslip'
    )

    @api.depends('hr_payslip_ids')
    def _compute_amount(self):
        for rec in self.hr_payslip_ids:
            if rec.line_ids:
                all_net = rec.line_ids.filtered(lambda p: p.code == 'NET').mapped('amount')
                for net in all_net:
                    if net:
                        self.amount += net
                    else:
                        self.amount = 0
            else:
                self.amount = 0

    # @api.depends('journal_id')
    # def _compute_currency_id(self):
    #     for wizard in self:
    #         wizard.currency_id = wizard.journal_id.currency_id


    def create_payment(self):
        if self.hr_payslip_ids:
            for rec in self.hr_payslip_ids:
                #amount = rec.line_ids.filtered(lambda p: p.code == 'NET').mapped('amount')
                debit_account = self.env['hr.salary.rule'].sudo().search([('code', '=', 'NET')], limit=1)
                crdit_account = self.journal_id.default_account_id
                if self.journal_id:
                        payment_value = {
                            'payment_type': 'outbound',
                            'journal_id': self.journal_id.id,
                            'payment_method_line_id': self.payment_method_line_id.id,
                            'partner_id': rec.employee_id.partner_id.id,
                            'currency_id': self.currency_id.id,
                            'amount':self.amount,
                            'date': self.payment_date,
                            'ref': rec.number,
                        }
                        payment = self.env['account.payment'].sudo().create(payment_value)
                        payment.action_post()

                        payment.move_id.line_ids.filtered(lambda p: p.credit > 0).write({
                                                    'account_id':crdit_account.id
                                                })
                        payment.move_id.line_ids.filtered(lambda p: p.debit > 0).write({
                                                    'account_id': debit_account.account_credit.id
                                                })

