# -*- coding: utf-8 -*-


from odoo import fields, models


class LunchWizard(models.TransientModel):
    _name = "lunch.wizard"
    _description = "LunchWizard"

    lun_type = fields.Char(string="Set New Lunch Type")
    lunch_id = fields.Many2one('lunch.lunch', string="Lunch Id")

    def action_process_lunch(self):
        self.lunch_id.lunch_type = self.lun_type
        #self.write( { self.lunch_id.lunch_type : self.lun_type } )