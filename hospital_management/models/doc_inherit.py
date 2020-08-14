
from odoo import fields, models


class Doctor(models.Model):
    _inherit = "doctor.doctor"

    inh_field1 = fields.Char(string="Doc inherit1")
    inh_field2 = fields.Char(string="Doc inherit2")
    inh_field3 = fields.Char(string="Doc inherit3")
