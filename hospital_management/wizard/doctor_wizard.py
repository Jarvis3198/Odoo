# -*- coding: utf-8 -*-


from odoo import fields, models


class DoctorWizard(models.TransientModel):
    _name = "doctor.wizard"
    _description = "DoctorWizard"

    doctor_wizard = fields.Char(string="Doctor_Wizard")

    def action_process(self):
        print("")
