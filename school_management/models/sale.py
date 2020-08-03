
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    my_cust = fields.Char(string="ssssssssssssssssssssssss")
