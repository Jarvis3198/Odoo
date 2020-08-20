
from odoo import fields, models, api


class Patient(models.Model):
    _name = "patient.patient"
    _description = 'My Patient Module'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_surname = fields.Text(string='Patient_Surname')
    patient_address = fields.Text(string='Patient_Address')
    patient_sex = fields.Selection(
        [('M', 'Male'), ('F', 'Female')], string='Gender Selection')

    patient_nationality = fields.Char(string="Nationality")
    patient_age = fields.Integer(string="Age")
    patient_photo = fields.Image(string="Patient Photo")
    patient_phone = fields.Integer(string="Phone Number", size="10")
    patient_height = fields.Integer(string="Patient height(cm)")
    patient_weight = fields.Integer(string="Phone Weight(kg)")
    patient_DOB = fields.Date(string="Patient Birthdate")
    patient_joindate = fields.Date(string="Patient Joindate")
    treatment_ids = fields.One2many(
        'treatment.treatment', 'patient_id', string="Treatment ID")
    my_treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment Id")

    def smartbutton(self):

        parent_id = self._context.get('active_ids')
        print(parent_id)
        #treatment = self.env['treatment.treatment'].browse(parent_id)
        # print(treatment)

        return {
            'name': ('Treatment'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'treatment.treatment',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def smartbutton1(self):
        return {
            'name': ('Doctor'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'doctor.doctor',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }
