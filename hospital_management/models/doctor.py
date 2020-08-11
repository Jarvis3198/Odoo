
from odoo import fields, models


class Doctor(models.Model):
    _name = "doctor.doctor"
    _description = 'My Doctor Object'
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string="Doctor Name")
    doctor_surname = fields.Char(string="Doctor Surname")
    doctor_address = fields.Text(string='Doctor_Address')
    doctor_age = fields.Integer(string="Age")
    doctor_sex = fields.Selection(
        [('M', 'Male'), ('F', 'Female')], string='Gender Selection')
    doctor_nationality = fields.Char(string="Nationality")
    doctor_photo = fields.Image(string="Doctor Photo")
    doctor_phone = fields.Integer(string="Phone Number", size="10")
    doctor_height = fields.Integer(string="Doctor height(cm)")
    doctor_weight = fields.Integer(string="Doctor Weight(kg)")
    doctor_DOB = fields.Date(string="Doctor Birthdate")
    doctor_joindate = fields.Date(string="Doctor Joindate")
    treatment_ids = fields.One2many(
        'treatment.treatment', 'patient_id', string="treatment_id")
