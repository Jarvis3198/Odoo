# -*- coding: utf-8 -*-


from odoo import fields, models


class PatientWizard(models.TransientModel):
    _name = "patient.wizard"
    _description = "PatientWizard"

    treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment ID")
    doctor_id = fields.Many2one(
        'doctor.doctor', string="Doctor ID")

    w_doctor_address = fields.Text(string='Doctor_Address')
    w_doctor_age = fields.Integer(string="Age")
    w_doctor_sex = fields.Selection(
        [('M', 'Male'), ('F', 'Female')], string='Gender Selection')

    def action_process_patient(self):

        object1 = self.env['doctor.doctor'].search(
            [['doctor_name', '=', self.doctor_id.doctor_name]])
        object1.doctor_address = self.w_doctor_address
        object1.doctor_age = self.w_doctor_age
        object1.doctor_sex = self.w_doctor_sex

        return {
            'name': ('Doctor'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'doctor.doctor',
            'res_id': object1.id,
            # 'view_id': self.env.ref('hospital_management.doctor_view_order_form').id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': '_blank',
            'domain': '[]',
        }

        #parent_id = self._context.get('active_ids')
        #patient = self.env['patient.patient'].browse(parent_id)
        #print('patient', patient, self.treatment_id)
        #patient.my_treatment_id = self.treatment_id.id
        #print("aaaaaaaaaaaaaaaaaaaaaa", patient)
