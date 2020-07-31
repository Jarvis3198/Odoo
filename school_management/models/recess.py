from odoo import fields, models


class Recess(models.Model):
    _name = "recess.recess"
    _description = 'My recess Object'
    _rec_name = 'recess_name'

    recess_name = fields.Char(String="Subject name")
    #lunch_id = fields.Many2one('lunch.lunch', string="Lunch")
