from odoo import models, fields
from datetime import date

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    student_id = fields.Char(string='Student ID', required=True, copy=False, default=lambda self: ('New'))
    admission_date =fields.Date(string="Admission Date",required=True,default = lambda self: date.today())
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number',required=True)
    address = fields.Text(string='Address',required=True)
    guardian_name = fields.Char(string='Guardian Name',required=True)
    guardian_phone = fields.Char(string='Guardian Phone Number',required=True)
    # blood_group = fields.Selection([('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], string='Blood Group')
    class_id=fields.Many2one('school.studentclass',string="Class")
