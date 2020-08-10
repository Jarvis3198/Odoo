
from odoo import fields, models


class Treatment(models.Model):
    _name = "treatment.treatment"
    _description = 'My Treatment Object'
    _rec_name = 'treatment_name'

    treatment_name = fields.Char(string="Treatment Name")
    treatment_date = fields.Date(string="Treatment Date")
    doctor_id = fields.Many2one('doctor.doctor', string="Doctor_Id")
    patient_id = fields.Many2one('patient.patient', string="Patient_Id")
