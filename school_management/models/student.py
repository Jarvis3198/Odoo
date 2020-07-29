
from odoo import fields, models


class Student(models.Model):
    _name = "student.student"
    _description = 'My Student Module'

    student_name = fields.Char(string="Student Name")
    student_address = fields.Text(string='student_address')
    student_marks = fields.Float(string="Student Marks")
    currently_studying = fields.Boolean(string="Currently studying?")
    join_date = fields.Date(string="Join Date")
    s_photo = fields.Image(string='Student Photo')
    signed_on = fields.Datetime(string='Signed On', help="Date of the signature.",copy=False)
    s_selection = fields.Selection([ ('sel1', 'Semester 1'),('sel2', 'Semester 2'),('sel3', 'Semester 3'),('sel4', 'Semester 4')], string='Semester Selection')
    sequence = fields.Integer(string='Sequence', default=10)