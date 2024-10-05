# -*- coding: utf-8 -*-
from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    bank_name = fields.Char()
    account_number = fields.Char()
    iban = fields.Char(
        string="IBAN"
    )
