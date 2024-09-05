from odoo import models, fields, api
from datetime import datetime
import logging
from odoo.exceptions import UserError
class TeacherAttendance(models.Model):
    _name = 'teacher.attendance'
    _description = 'Teacher Attendance'

    teacher_id = fields.Many2one('school.teacher', string='Teacher')
    date = fields.Date(string='Date', required=True, default=fields.Date.context_today)
    checkin1 = fields.Selection([
        ('waiting', 'Waiting'),
        ('check_in', 'Check In'),
    ], string='Check In Status', default='waiting')
    checkin2 = fields.Datetime(string='Check In Time', readonly=True, store=True)
    checkout1 = fields.Selection([
        ('waiting', 'Waiting'),
        ('check_out', 'Check Out'),
    ], string='Check Out Status', default='waiting')
    checkout2 = fields.Datetime(string='Check Out Time', readonly=True, store=True)
    total_hours = fields.Float(string='Total Hours', compute='_compute_total_hours', readonly=True)

    @api.depends('checkin2', 'checkout2')
    def _compute_total_hours(self):
        for record in self:
            if record.checkin2 and record.checkout2:
                check_in_time = fields.Datetime.from_string(record.checkin2)
                check_out_time = fields.Datetime.from_string(record.checkout2)
                delta = check_out_time - check_in_time
                record.total_hours = delta.total_seconds() / 3600.0
            else:
                record.total_hours = 0.0

    # @api.onchange('checkin1')
    # def _onchange_checkin1(self):
    #     if self.checkin1 == 'check_in':
    #         self.checkin2 = datetime.now()

    # @api.onchange('checkout1')
    # def _onchange_checkout1(self):
    #     if self.checkout1 == 'check_out':
    #         self.checkout2 = datetime.now()

    # @api.model
    # def create(self, vals):
    #     if vals.get('checkin1') == 'check_in':
    #         vals['checkin2'] = datetime.now()
    #     if vals.get('checkout1') == 'check_out':
    #         vals['checkout2'] = datetime.now()
    #     return super(TeacherAttendance, self).create(vals)

    # def write(self, vals):
    #     if 'checkin1' in vals and vals['checkin1'] == 'check_in':
    #         vals['checkin2'] = datetime.now()
    #     if 'checkout1' in vals and vals['checkout1'] == 'check_out':
    #         vals['checkout2'] = datetime.now()
    #     return super(TeacherAttendance, self).write(vals)
    # def action_check_in(self):
    #     _logger=logging.getLogger(__name__)
    #     _logger.info(f"self = {self}")
    #     self.checkin1 = 'check_in'
    #     self.checkin2 = datetime.now()
    
    def action_check_in(self):
        for record in self:
            # Search for existing records for the same teacher and date
            existing_record = self.search([
                ('teacher_id', '=', record.teacher_id.id),
                ('date', '=', record.date),
                ('checkin1', '=', 'check_in')
            ], limit=1)

            if existing_record:
                raise UserError('You have already checked in for today.')
            
            record.checkin1 = 'check_in'
            record.checkin2 = fields.Datetime.now()
    
    def action_check_out(self):
        for record in self:
            # Search for existing records for the same teacher and date
            existing_record = self.search([
                ('teacher_id', '=', record.teacher_id.id),
                ('date', '=', record.date),
                ('checkout1', '=', 'check_out')
            ], limit=1)

            if existing_record:
                raise UserError('You have already checked out for today.')
            
            record.checkout1 = 'check_out'
            record.checkout2 = fields.Datetime.now()
    # def action_check_out(self):
    #     self.checkout1 = 'check_out'
    #     self.checkout2 = datetime.now()
