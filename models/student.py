from odoo import models, fields,api
from datetime import date
import logging
class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    student_id = fields.Char(string='Student ID', required=True, copy=False, default=lambda self: ('New'),compute='_compute_student_id', store=True)
    admission_date =fields.Date(string="Admission Date",required=True,default = lambda self: date.today())
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number')
    address = fields.Text(string='Address',required=True)
    guardian_name = fields.Char(string='Guardian Name')
    guardian_phone = fields.Char(string='Guardian Phone Number')
    # blood_group = fields.Selection([('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], string='Blood Group')
    class_id=fields.Many2one('school.studentclass',string="Class")
    photo = fields.Binary(string='Photo')
    

    # adding age using compute
    age = fields.Integer(string='Age', compute='_compute_age',store=True,readonly=True)

    # adding logic for age cal
    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()  # Get the current date
                birth_date = record.birth_date  # Extract birth date
                # Calculate preliminary age
                age = today.year - birth_date.year
                # Adjust if birthday has not occurred yet this year
                if (today.month, today.day) < (birth_date.month, birth_date.day):
                    age -= 1
                record.age = age  # Set the computed age
            else:
                record.age = 0  # Set age to 0 if birth_date is not set
    
    # @api.depends('name')
    # def _compute_student_id(self):
    #     for record in self:
    #         if record.student_id == 'New':
    #             _logger=logging.getLogger(__name__)
    #             # Get the latest student record
    #             last_student = self.env['school.student'].search([], order='id desc', limit=1)

    #             _logger.info(f"last student = {last_student}")
    #             student_model = self.env['school.student']
    #             students = student_model.browse(last_student[0])
    #             if last_student:
    #                 last_id = last_student.student_id
    #                 _logger.info(f"last id  = {last_id}")

    #                 last_num = int(last_id[3:]) if last_id else 0  # Extract numeric part from 'STU999'
    #             else:
    #                 last_num = 0

    #             # Increment the number
    #             new_num = last_num + 1

    #             # Generate the new ID with dynamic length
    #             record.student_id = f'STU{new_num:03d}' if new_num < 1000 else f'STU{new_num}'
    #         else:
    #             record.student_id = record.student_id
    def create_id(self):
        _logger=logging.getLogger(__name__)
        _logger.info(f"inside func ")
        record=self.env['school.student'].search([],order="student_id desc",limit=1)
        last_id=record.student_id
        last_id=last_id[3:]
        new_num=int(last_id)+1
        last_id=f"STU{new_num:03d}"
        
        _logger.info(f"newid={last_id}")
        return last_id
            # if record.student_id != "STU00"+str(i):
            #     return "STU00"+str(i)
                    

    @api.model
    def create(self,vals):

        new_id=self.create_id()
        vals['student_id']=new_id
        new_record=super(Student,self).create(vals)
        return new_record
    
    def create_dummy_student(self):
    # Dummy data to be used for the student creation
        dummy_vals = {
            'name': 'Dummy Student',
            'age': 20,
            'email': 'dummy@student.com',
            'address':"dwarka"
        }
        _logger=logging.getLogger(__name__)
        # Create a student record using the custom create method
        new_student = self.create(dummy_vals)
        _logger.info(f"dummy record created {new_student}")

        return new_student

    
