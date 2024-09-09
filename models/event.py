from odoo import models, fields, api
import logging

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
    @api.model
    def create(self, vals):
        # Call the default create method
        _logger=logging.getLogger(__name__)
        _logger.info(f"the create func ")
        _logger.info(f"vals= {vals}")
        if vals['description']==False:
            vals['description']="default desc"
        new_record=super(SchoolEvent, self).create(vals)
        
        for x in new_record:

            _logger.info(f"records={x}")
        
        return new_record
