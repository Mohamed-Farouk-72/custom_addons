from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_sales_order = fields.Char()


    def _prepare_invoice(self):
        result = super(SaleOrder, self)._prepare_invoice()
        result['customer_sales_order'] = self.customer_sales_order

        return result
                                                                                                             