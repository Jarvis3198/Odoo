
from odoo import fields, models


class Teacher(models.Model):
    _name = "Teacher.Teacher"
    _description = 'My Teacher App'

    teacher_name = fields.Char(string="Teacher Name")
    teacher_salary = fields.Float(string="Teacher Salary")
    sequence = fields.Integer(string='Sequence', default=10)
