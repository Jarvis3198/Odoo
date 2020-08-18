# -*- coding: utf-8 -*-


from odoo import fields, models


class PatientWizard(models.TransientModel):
    _name = "patient.wizard"
    _description = "PatientWizard"

    treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment Id")

    def action_process_patient(self):
        return {
            'name': ('Doctor'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'doctor.doctor',
            'view_id': 'doctor_view_order_form',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

        #parent_id = self._context.get('active_ids')
        #patient = self.env['patient.patient'].browse(parent_id)
        #print('patient', patient, self.treatment_id)
        #patient.my_treatment_id = self.treatment_id.id
        #print("aaaaaaaaaaaaaaaaaaaaaa", patient)
