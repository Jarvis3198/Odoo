# -*- coding: utf-8 -*-


from odoo import fields, models


class PatientWizard(models.TransientModel):
    _name = "patient.wizard"
    _description = "PatientWizard"

    treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment ID")
    doctor_id = fields.Many2one(
        'doctor.doctor', string="Doctor ID")

    def action_process_patient(self):

        object1 = self.env['doctor.doctor'].search(
            [['doctor_name', '=', self.doctor_id.doctor_name]])

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
