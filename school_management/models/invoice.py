
from odoo import fields, models



class InvoiceOrder(models.Model):
    _inherit = "account.move"

    abcd = fields.Char(string="Inherited field 1")
    efgh = fields.Char(string="Inherited field 2")

class InvoiceOrderLine(models.Model):
    _inherit = "account.move.line"

    ijkl = fields.Char(string="Inherited field 1")
    mnop = fields.Char(string="Inherited field 2")