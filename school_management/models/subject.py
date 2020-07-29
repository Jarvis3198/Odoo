from odoo import fields, models


class Subject(models.Model):
    _name = "subject.subject"
    _description = 'My Subject Object'


    subject_name = fields.Char(String="Subject name")
    subject_code = fields.Integer(string='Subject code')
    start_date = fields.Date(string="Subject Start Date")