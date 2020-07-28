
from odoo import fields, models


class Student(models.Model):
    _name = "student.student"
    _description = 'My Student Module'

    student_name = fields.Char(string="Student Name")
    student_marks = fields.Float(string="Student Marks")
    sequence = fields.Integer(string='Sequence', default=10)
    s_photo = fields.Image(string='Student Photo')
    join_date = fields.Date(string="Join Date")
    s_selection = fields.Selection([ ('sel1', 'Semester 1'),('sel2', 'Semester 2'),('sel3', 'Semester 3'),('sel4', 'Semester 4')], string='Semester Selection')
