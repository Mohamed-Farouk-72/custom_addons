from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    currency_id = fields.Many2one('res.currency', related=False, readonly=False, required=True,
                                  default=lambda self: self.env.user.company_id.currency_id.id)
