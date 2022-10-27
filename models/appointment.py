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

    @api.multi
    def _set_default_code(self):
        return "The odoo sw is the game changer in the business industry"

    # changing state from draft to confirm
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    # changing state from confirm to done
    def action_done(self):
        for rec in self:
            rec.state = 'done'

    # changing state from done to cancel
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    # changing state from cancel to draft
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Patient", required=False, )
    patient_age = fields.Integer(string="Age", related="patient_id.patient_age")
    notes = fields.Text(string="Notes", default=_set_default_code)
    doctor_note = fields.Text(string="Notes")
    appointment_lines = fields.One2many(comodel_name="hospital.appointment.lines",
                                        inverse_name="appointment_id", string="Appointment Lines")
    pharmacy_note = fields.Text(string="Notes")
    appointment_date = fields.Date(string="Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='Status', readonly=True, default='draft')


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'

    product_id = fields.Many2one('product.product', string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')
