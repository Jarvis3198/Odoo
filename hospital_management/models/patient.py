
from odoo import fields, models


class Patient(models.Model):
    _name = "patient.patient"
    _description = 'My Patient Module'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_surname = fields.Text(string='Patient_Surname')
    patient_address = fields.Text(string='Patient_Address')
    patient_sex = fields.Selection(
        [('M', 'Male'), ('F', 'Female')], string='Gender Selection')

    patient_nationality = fields.Char(string="Nationality")
    patient_age = fields.Integer(string="Age")
    patient_photo = fields.Image(string="Patient Photo")
    patient_phone = fields.Integer(string="Phone Number", size="10")
    patient_height = fields.Integer(string="Patient height(cm)")
    patient_weight = fields.Integer(string="Phone Weight(kg)")
    patient_DOB = fields.Date(string="Patient Birthdate")
    patient_joindate = fields.Date(string="Patient Joindate")
    treatment_ids = fields.One2many(
        'treatment.treatment', 'patient_id', string="Treatment ID")
    my_treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment Id")
