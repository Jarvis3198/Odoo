
from odoo import fields, models


class Doctor(models.Model):
    _name = "doctor.doctor"
    _description = 'My Doctor Object'
    _rec_name = 'doctor_name'

    doctor_name = fields.Char(string="Doctor Name")
    doctor_surname = fields.Char(string="Doctor Surname")
    doctor_address = fields.Text(string='Doctor_Address')
    age = fields.Integer(string="Age")
