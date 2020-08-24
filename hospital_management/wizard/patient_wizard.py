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
    w_treatment_ids = fields.Many2many(
        'treatment.treatment', string="Treatment IDS")

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
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': '_blank',
            'domain': '[]',
        }

    def action_process_o2m(self):

        parent_id = self._context.get('active_ids')
        a = self.env['patient.patient'].browse(parent_id[0])
        a.write({'treatment_ids': [(4, self.w_treatment_ids.id, 0)]})

        #obj1 = self.env['patient.patient'].write(0, 0)
        # print(obj1)

        #parent_id = self._context.get('active_ids')
        #patient = self.env['patient.patient'].browse(parent_id)
        #print('patient', patient, self.treatment_id)
        #patient.my_treatment_id = self.treatment_id.id
        #print("aaaaaaaaaaaaaaaaaaaaaa", patient)
