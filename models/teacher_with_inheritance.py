from odoo import models, fields

class Teacher2(models.Model):
    _inherit="school.teacher"
    date_of_birth=fields.Date(string='Date of Birth')
    address=fields.Char(string="Address")
    salary=fields.Float(default=1000)
