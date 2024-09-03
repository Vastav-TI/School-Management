import logging
from odoo import models, fields, api

class StudentGrade(models.Model):
    _name = 'school.student.grade'
    _description = 'Student Grades'

    name = fields.Char(string='Name')  # Optional field for the record name
    class_id = fields.Many2one('school.studentclass', string='Class', required=True)
    student_grade_line_ids = fields.One2many('school.student.grade.line', 'student_grade_id', string='Student Grades')

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            #initialize the logger 
            _logger=logging.getLogger(__name__)
            _logger.info(f"self = {self}")
            students = self.env['school.student'].search([('class_id', '=', self.class_id.id)])
            
            #using logger to print the stud info
            _logger.info(f"students found for class {self.class_id.name}:{students}")
            
            s = self.env['school.student'].browse([1, 2])
            for i in s:
                _logger.info(f"student row i = {i}")
                _logger.info(f"student name = {i.student_id}")

            student_grades = []
            for student in students:
                student_grades.append((0, 0, {
                    'student_id': student.id,
                    'name': student.name
                }))
            _logger.info(f"student_grades = {student_grades}")
            self.student_grade_line_ids = student_grades


