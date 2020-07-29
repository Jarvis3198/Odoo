
from odoo import fields, models


class Teacher(models.Model):
    _name = "teacher.teacher"
    _description = 'My Teacher Module'

    teacher_name = fields.Char(string="Teacher Name", required=True)
    teacher_surname = fields.Text(string='Teacher_Surname')
    teacher_salary = fields.Float(string="Teacher Salary")
    in_service = fields.Boolean(string="Currently in service?")
    join_date = fields.Date(string="Join Date")
    t_photo = fields.Image(string='Teacher Photo')
    signed_on = fields.Datetime(string='Signed On', help="Date of the signature.",copy=False)
    t_selection = fields.Selection([ ('tsel1', 'Primary'),('tsel2', 'Secondary'),('tsel3', 'Higher Secondary')], string='Teaching teaching level')
    sequence = fields.Integer(string='Teacher', default=10)