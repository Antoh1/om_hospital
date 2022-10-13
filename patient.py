# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string='Patient Name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_name'
    _description = 'Patient Record'

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer("Age")
    gender = fields.Selection([('fe_male', 'Female'), ('male', 'Male')], default="male", string="Gender")
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = name = fields.Char(string='Patient Reference', required=True, copy=False, readonly=True,
                                  index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
                vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.code') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
