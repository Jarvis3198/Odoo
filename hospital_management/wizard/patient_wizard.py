# -*- coding: utf-8 -*-


from odoo import fields, models


class PatientWizard(models.TransientModel):
    _name = "patient.wizard"
    _description = "PatientWizard"

    treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment Id")

    def action_process_patient(self):
        parent_id = self._context.get('active_ids')
        patient = self.env['patient.patient'].browse(parent_id)
        print('patient', patient, self.treatment_id)
        patient.my_treatment_id = self.treatment_id.id
        print("aaaaaaaaaaaaaaaaaaaaaa", patient)
        return True

    # 	self.env['patient.patient'].search([('treatment_ids', '=', self.treatment_id),
        #                               (field,'!=', False),
        #                               (field,'!=', 0.0)]) #
