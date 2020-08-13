# -*- coding: utf-8 -*-


from odoo import fields, models


class PatientWizard(models.TransientModel):
    _name = "patient.wizard"
    _description = "PatientWizard"

    treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment Id")

    def action_process_patient(self):
        res = self.env['patient.patient'].search('treatment_ids', '=', treatment_id)
        print(res)
        return res
