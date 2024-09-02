from odoo import models, fields,api

class Studentclass(models.Model):
    _name = 'school.studentclass'
    _description = 'Students in Class'

    name = fields.Char(string='Class Name', required=True)
    strength = fields.Integer(string='Class Strength',readonly=True,compute="_compute_class_strength")
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')
    student_ids=fields.One2many('school.student','class_id',string="Students in Class",readonly=True)

    @api.depends('student_ids')
    def _compute_class_strength(self):
        for record in self:
            record.strength = len(record.student_ids)