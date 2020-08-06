
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "student.student"
    _description = 'My Student Module'
    _rec_name = 'student_name'

    student_name = fields.Char(string="Student Name")
    student_surname = fields.Char(string="Student Surname")
    age = fields.Integer(string='Age')
    scholarship = fields.Boolean(string="Scholarship?")
    student_address = fields.Text(string='student_address')
    student_marks = fields.Float(string="Student Percentage")
    student_Physics_marks = fields.Float(string="Student Physics marks")
    student_Chemistry_marks = fields.Float(string="Student Chemistry Marks")
    student_Math_marks = fields.Float(string="Student Math Marks")
    currently_studying = fields.Boolean(string="Currently studying?", compute="ffunc3", store=True)
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

    teacher_id = fields.Many2one('teacher.teacher', string="Teacher")

    def action_state_graduate(self):
        self.write({'state': 'done'})
        self.write({'currently_studying': False})
        return {}

    def action_state_enroll(self):
        self.write({'state': 'studying'})
        self.write({'currently_studying': True})

    @api.model
    def create(self, vals):
        print("Create Method Called")
        res = super(Student, self).create(vals)
        res.age = 25
        return res

    def write(self, vals):
        vals["student_Physics_marks"] = "74"
        res = super(Student, self).write(vals)
        return res

    def unlink(self):
        if self.age < 25: 
            raise ValidationError("Younger than 25 cant self delete")
        res = super(Student, self).unlink()
        print("Unlink method called")
        return res

    def copy(self, default=None):
        if self.age > 75:
            raise ValidationError("Older than 75 cant self copy")
        res = super(Student, self).copy(default)
        return res

    def copy_data(self, default=None):
        if self.teacher_id.teacher_name == False:
            raise ValidationError("Teacher needed to duplicate")
        res =  super().copy_data(default)
        return res

    def name_get(self):
        return [(student.id, student.student_name or _('No name')) for student in self]

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        res = super(Student, self)._name_search(name, args, operator, limit, name_get_uid)
        print("=======================",res)
        return res

    @api.onchange('student_name')
    def ffunc1(self):
        self.age = 50

    @api.constrains('student_surname')
    def ffunc2(self):
        if self.student_name == self.student_surname:
            raise ValidationError("Name and Surname can't be the same")

    @api.depends('student_marks')
    def ffunc3(self):
        if self.student_marks != 0.0 and not self.currently_studying:
            raise ValidationError(_("How can you have marks without studying"))


    def search(self, args, offset=0, limit=None, order=None, count=False):
        
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa search reduce")
        res = super(Student, self).search( args, offset, limit, order, count)
        print("=======================", res)
        return res
