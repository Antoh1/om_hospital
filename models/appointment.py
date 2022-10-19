# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Appointment'
    _order = 'id desc'


    @api.model
    def create(self, vals):        # generating sequence for HospitalAppointment model
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.code') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def _set_default_code(self):
        return "The odoo sw is the game changer in the business industry"

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Patient", required=False, )
    patient_age = fields.Integer(string="Age", related="patient_id.patient_age")
    notes = fields.Text(string="Notes", default=_set_default_code)
    appointment_date = fields.Date(string="Date")


