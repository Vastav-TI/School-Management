from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age',required=True)
    salary = fields.Float(string='Salary',required=True)
    active = fields.Boolean(string='Active', default=True)
    subject_ids = fields.Many2many(
        'school.subject',
        'school_teacher_subject_rel',  # The name of the relationship table
        'teacher_id',  # Field in the relationship table referencing the teacher
        'subject_id',  # Field in the relationship table referencing the subject
        string='Subjects'
    )
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    class_id=fields.Many2one('school.studentclass',string="Class")
    photo = fields.Binary(string='Photo')
