from odoo import api, fields, models


class Lunch(models.Model):
    _name = "lunch.lunch"
    _description = 'My lunch object'
    _rec_name = "lunch_name"

    lunch_name = fields.Char(String="Subject name")
    lunch_type = fields.Char(String="Lunch Type")


    recess_id = fields.Many2one('recess.recess', string="Recess Time")
    #recess_ids = fields.Many2many('recess.recess' , string="M2M")
    recess_ids = fields.One2many('recess.recess', 'lunch_id', string="Recesses Time")

    def smartbutton(self):
        print("Im a smart button")

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

    def read(self,fields=None):
        print("Read called")
        res = super(Lunch,self).read(fields)
        print(res)
        return res

    def field_get(self,fields=None,attributes=None):
        print("Field_get called")
        res = super(Lunch,self).field_get(fields,attributes)
        print(res)
        return res

    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        print("Read_group called")
        res = super(Lunch,self).read_group(domain, fields, groupby, offset, limit, orderby, lazy)
        print(res)
        return res

    def search(self, args, offset=0, limit=None, order=None, count=False):
        print("Search Called")
        res = super(Lunch, self).search( args, offset, limit, order, count)
        print(res)
        return res

    
  #  def copy(self, default=None):
        


 #   def search:
    
   # def read(self, fields=None, load='_classic_read'):
      #  print("Search was called")
#    def search_read: