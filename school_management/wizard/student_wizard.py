# -*- coding: utf-8 -*-


from odoo import fields, models


class StudentWizard(models.TransientModel):
    _name = "student.wizard"
    _description = "StudentWizard"

    my_wizard_field_name = fields.Char(string="My Wizard Name")

    def action_process(self):
        print("aaaaaaaaaaaaaaaaaaaaaaaA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
