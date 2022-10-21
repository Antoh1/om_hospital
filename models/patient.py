# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string='Patient Name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_name'
    _description = 'Patient Record'

    patient_name = fields.Char(string='Name', required=True)
    doctor_id = fields.Many2one(comodel_name="hospital.doctor", string="Doctor", required=False, )
    patient_age = fields.Integer(string="Age", track_visibility="always")  # track field changes on chatter
    contact = fields.Char(string="Contact Number")
    gender = fields.Selection([('fe_male', 'Female'), ('male', 'Male')], default="male", string="Gender")
    notes = fields.Text(string="Registration Notes")
    image = fields.Binary(string="Image")
    age_group = fields.Selection(string="Age Group", selection=[('minor', 'Minor'), ('adult', 'Adult')],
                                 compute='set_age_group')
    name = name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                                  index=True, default=lambda self: _('New'))
    appointment_count = fields.Integer(string="Appointments", compute="get_appointment_count")
    active = fields.Boolean('Active', default=True)

    # function to assign number of appointments to a field
    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    # returning a form and tree views for individual patient appointments
    @api.multi
    def open_patient_appointments(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }

    # validating field input for the HP model
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 6:
                raise ValidationError('The age is too low refer them to children hospital')

    # computing value for age_group field
    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'adult'

    # generating sequence for HospitalPatient model
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.code') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
