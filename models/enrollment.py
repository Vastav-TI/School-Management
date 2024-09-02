from odoo import models, fields

class Enrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'Student Enrollment'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    class_id = fields.Many2one('school.classes',string ="Class",required=True)
    enrollment_date = fields.Date(string='Enrollment Date', required=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')
