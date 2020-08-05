
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    my_cust = fields.Char(string="Sale Order inherit")
    my_field2 = fields.Char(string="Sale Order ihn 2")

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    my_field2 = fields.Char(string="Sale Order ihn 3")


