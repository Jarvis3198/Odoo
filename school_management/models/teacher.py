
from odoo import fields, models, api


class Teacher(models.Model):
    _name = "teacher.teacher"
    _description = 'My Teacher Module'
    _rec_name = 'teacher_name'

    teacher_name = fields.Char(string="Teacher Name", required=True)
    teacher_surname = fields.Text(string='Teacher_Surname')
    teacher_address = fields.Text(string='Teacher_Address')
    age = fields.Integer(string="Age")
    teacher_salary = fields.Float(string="Teacher Salary")
    in_service = fields.Boolean(string="Currently in service?")
    join_date = fields.Date(string="Join Date")
    t_photo = fields.Image(string='Teacher Photo')
    signed_on = fields.Datetime(string='Signed On', help="Date of the signature.",copy=False)
    t_selection = fields.Selection([ ('tsel1', 'Primary'),('tsel2', 'Secondary'),('tsel3', 'Higher Secondary')], string='Teaching teaching level')
    state = fields.Selection([
        ('draft', 'Not Working'),
        ('done', 'Hired'),
    ], string='Selection Status', readonly=True, copy=False, store=True, default='draft')
    sequence = fields.Integer(string='Teacher', default=10)
    govt_certified = fields.Boolean(string="Govt approved?")
    phd = fields.Boolean(string="PhD passout?")
    blood_group = fields.Selection([ ('o+', 'O Positive'),('a+', 'A Positive'),('b+', 'B Positive'),('AB+', 'AB Positive')], string='Blood Group')
    
    student_ids = fields.One2many('student.student', 'teacher_id', string="Student")
    students_ids = fields.Many2many('student.student', string="Student")

    def action_go_forward(self):
        self.write({'state': 'done'})
        self.write({'in_service': True})


    def action_go_backward(self):
        self.write({'state': 'draft'})
        self.write({'in_service': False})

   
