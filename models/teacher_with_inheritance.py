from odoo import models, fields,api

class Teacher2(models.Model):
    _inherit="school.teacher"
    date_of_birth=fields.Date(string='Date of Birth')
    address=fields.Char(string="Address")
    salary=fields.Float(default=1000)
    
    email=fields.Char(string="Email",readonly=True)
    phone = fields.Char(string='Phone Number')
    years_of_experience = fields.Integer(string='Years of Experience')




    @api.onchange('name')
    def compute_email(self):
        if self.name:
            self.email=self.name+"@gmail.com"
        




