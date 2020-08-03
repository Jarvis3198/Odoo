from odoo import api,fields, models


class Recess(models.Model):
    _name = "recess.recess"
    _description = 'My recess Object'
    _rec_name = 'recess_name'

    recess_name = fields.Char(String="Subject name", copy=False)
    lunch_id = fields.Many2one('lunch.lunch', string="Lunch")
    
    
    @api.model
    def create(self, vals):
            res = super(Recess, self).create(vals)
            return res