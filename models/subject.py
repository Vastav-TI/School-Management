from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
    teacher_ids = fields.Many2many(
        'school.teacher',
        'school_teacher_subject_rel',  # The name of the relationship table
        'subject_id',  # Field in the relationship table referencing the subject
        'teacher_id',  # Field in the relationship table referencing the teacher
        string='Teachers'
    )
