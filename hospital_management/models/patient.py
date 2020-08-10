
from odoo import fields, models


class Patient(models.Model):
    _name = "patient.patient"
    _description = 'My Patient Module'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_surname = fields.Text(string='Patient_Surname')
    patient_address = fields.Text(string='Patient_Address')
    age = fields.Integer(string="Age")
