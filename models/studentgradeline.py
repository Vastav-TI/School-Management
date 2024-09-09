from odoo import models, fields, api
import logging
class StudentGradeLine(models.Model):
    _name = 'school.student.grade.line'
    _description = 'Student Grade Line'

    student_grade_id = fields.Many2one('school.student.grade', string='Student Grades', ondelete='cascade')
    student_id = fields.Many2one('school.student', string='Student')
    s_id = fields.Char(string="Student Id", related='student_id.student_id', store=True)
    name = fields.Char(string='Student Name', related='student_id.name')
    class_id = fields.Many2one('school.studentclass', related='student_id.class_id',string='Class')
    
    # Subjects will be dynamically populated
    subject1_id = fields.Many2one('school.subject', string='Subject 1')
    subject2_id = fields.Many2one('school.subject', string='Subject 2')
    subject3_id = fields.Many2one('school.subject', string='Subject 3')
    subject4_id = fields.Many2one('school.subject', string='Subject 4')
    subject5_id = fields.Many2one('school.subject', string='Subject 5')
    
    # Marks for each subject
    marks_subject1 = fields.Integer(string="Marks Subject 1")
    marks_subject2 = fields.Integer(string="Marks Subject 2")
    marks_subject3 = fields.Integer(string="Marks Subject 3")
    marks_subject4 = fields.Integer(string="Marks Subject 4")
    marks_subject5 = fields.Integer(string="Marks Subject 5")

   