import logging
from odoo import models, fields, api


class StudentGradeLineSubject(models.Model):
    _name = 'school.student.grade.line.subject'
    _description = 'Student Grade Line Subject'

    student_grade_line_id = fields.Many2one('school.student.grade.line', string='Student Grade Line', ondelete='cascade')
    subject_id = fields.Many2one('school.subject', string='Subject')
    subject_name = fields.Char(string='Subject Name', related='subject_id.name', store=True)
    marks = fields.Integer(string='Marks')