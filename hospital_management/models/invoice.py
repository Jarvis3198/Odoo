
from odoo import fields, models


class Invoice(models.Model):
    _name = "invoice.invoice"
    _description = 'My Invoice Object'
    _rec_name = 'invoice_name'

    invoice_name = fields.Char(string="Invoice Name")
    invoice_date = fields.Date(string="Invoice Date")
    invoice_cost = fields.Float(string="Invoice Cost(₹)")
    doctor_id = fields.Many2one('doctor.doctor', string="Doctor_Id")
    patient_id = fields.Many2one('patient.patient', string="Patient_Id")
