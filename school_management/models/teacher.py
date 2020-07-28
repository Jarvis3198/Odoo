
from odoo import fields, models


class Teacher(models.Model):
    _name = "teacher.teacher"
    _description = 'My Teacher App'

    teacher_name = fields.Text(string='Teacher_name', required=True)
    teacher_salary = fields.Float(string="Teacher Salary")
    in_service = fields.Boolean()
    join_date = fields.Date(string="Join Date")
    sequence = fields.Integer(string='Teacher', default=10)
    signed_on = fields.Datetime(string='Signed On', help="Date of the signature.",copy=False)
