from odoo import api,fields, models


class Lunch(models.Model):
    _name = "lunch.lunch"
    _description = 'My lunch object'
    _rec_name = "lunch_name"

    lunch_name = fields.Char(String="Subject name")


    recess_id = fields.Many2one('recess.recess', string="M2O")
    #recess_ids = fields.Many2many('recess.recess', string="M2M")
    recess_ids = fields.One2many('recess.recess', 'lunch_id', string="O2M")



    @api.model
    def create(self, vals):
            res = super(Lunch, self).create(vals)
            return res

    @api.onchange('lunch_name')
    def fun1(self):
        print("API On Change Called")


    @api.constrains('lunch_name')
    def fun2(self):
        print("API Constrains Called")


    @api.depends('lunch_name')
    def fun3(self):
        print("API Depends Called")