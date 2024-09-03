from odoo import models, fields, api

class StudentGradeLine(models.Model):
    _name = 'school.student.grade.line'
    _description = 'Student Grade Line'

    student_grade_id = fields.Many2one('school.student.grade', string='Student Grades', ondelete='cascade')
    student_id = fields.Many2one('school.student', string='Student')
    s_id=fields.Char(string="Student Id",related='student_id.student_id',store=True)
    name = fields.Char(string='Student Name', related='student_id.name')
    grade = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('not_assigned', 'Not Assigned'),
    ], string='Grade')

    # def write(self,vals):
    #     res=super(StudentGradeLine,self).write(vals)
    #     if self.
    # def create(self,vals):
    #     res=super(StudentGradeLine,self).create(vals)
    #     if res.status:
    #         res.student_id.


