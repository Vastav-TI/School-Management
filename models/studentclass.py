from odoo import models, fields,api
import logging
class Studentclass(models.Model):
    _name = 'school.studentclass'
    _description = 'Students in Class'

    name = fields.Char(string='Class Name', required=True)
    email=fields.Char(string="School Email",readonly=True)
    strength = fields.Integer(string='Class Strength',readonly=True,compute="_compute_class_strength")
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')
    student_ids=fields.One2many('school.student','class_id',string="Students in Class",readonly=True)
    # Adding Many2many relation with school.subject
    subject_ids = fields.Many2many(
        'school.subject',
        'school_studentclass_subject_rel',  # The name of the relationship table
        'class_id',  # The field referencing the student class
        'subject_id',  # The field referencing the subject
        string="Subjects"
    )
    
    @api.onchange('name')
    def compute_email(self):
        _logger=logging.getLogger(__name__)
        _logger.info(f"self {self}")
        _logger.info(f"name-------- {self.name}")
        if self.name:
            self.email=self.name+"@gmail.com"
        _logger.info(f"self.id {type(self.id)}")
        record_id_str = f"{self.id}"  # e.g., 'NewId_6'

        # Extract the numeric part (assuming it's the last part after an underscore)
        record_id = int(record_id_str.split('_')[-1])
        _logger.info(f"id-------- {record_id}")
        if record_id:
            record=self.env['school.studentclass'].browse(record_id)
            record.email=self.email
    @api.depends('student_ids')
    def _compute_class_strength(self):
        for record in self:
            record.strength = len(record.student_ids)