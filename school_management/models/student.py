
from odoo import fields, models


class Student(models.Model):
    _name = "student.student"
    _description = 'My Student Module'

    student_name = fields.Char(string="Student Name")
    student_surname = fields.Char(string="Student Surname")
    age = fields.Integer(string='Age')
    scholarship = fields.Boolean(string="Scholarship?")
    student_address = fields.Text(string='student_address')
    student_marks = fields.Float(string="Student Percentage")
    student_Physics_marks = fields.Float(string="Student Physics marks")
    student_Chemistry_marks = fields.Float(string="Student Chemistry Marks")
    student_Math_marks = fields.Float(string="Student Math Marks")
    currently_studying = fields.Boolean(string="Currently studying?")
    medical_problems = fields.Text(string='Medical problems if any')
    blood_group = fields.Selection([ ('o+', 'O Positive'),('a+', 'A Positive'),('b+', 'B Positive'),('AB+', 'AB Positive')], string='Blood Group')
    join_date = fields.Date(string="Join Date")
    s_photo = fields.Image(string="Student Photo")
    signed_on = fields.Datetime(string="Signed On", help="Date of the signature.",copy=False)
    s_selection = fields.Selection([ ('sel1', 'Semester 1'),('sel2', 'Semester 2'),('sel3', 'Semester 3'),('sel4', 'Semester 4')], string='Semester Selection')
    sequence = fields.Integer(string='Sequence', default=10)

    state = fields.Selection([
        ('studying', 'Still Studying'),
        ('done', 'Graduated'),
    ], string='Selection Status', readonly=True, copy=False, store=True, default='studying')


    def action_state_graduate(self):
    	self.write({'state': 'done'})
    	self.write({'currently_studying': False})

    def action_state_enroll(self):
    	self.write({'state': 'studying'})
    	self.write({'currently_studying': True})