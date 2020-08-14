
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    inh_field1 = fields.Char(string="Sale inherit1")
    inh_field2 = fields.Char(string="Sale inherit2")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    inh_field3 = fields.Char(string="SaleOrderLine inherit3")
