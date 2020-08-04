
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    my_cust = fields.Char(string="Sale Order inherit")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    my_field2 = fields.Char(string="Sale Order ihn 2")


class InvoiceOrder(models.Model):
    _inherit = "account.move"

    abcd = fields.Char(string="Inherited field 1")
    efgh = fields.Char(string="Inherited field 2")
