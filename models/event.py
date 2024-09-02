from odoo import models, fields, api

class SchoolEvent(models.Model):
    _name = 'school.event'
    _description = 'School Event'

    name = fields.Char(string="Event Name", required=True)
    event_type = fields.Selection([
        ('holiday', 'Holiday'),
        ('school_event', 'School Event')
    ], string="Event Type", required=True)
    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
