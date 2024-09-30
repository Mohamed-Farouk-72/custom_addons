# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    customer_sales_order = fields.Char()
                                                                                                             