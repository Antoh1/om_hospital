# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctors Records'

    name = fields.Char(string="Doctor's Name", required=False, )
    gender = fields.Selection([('fe_male', 'Female'), ('male', 'Male')], default="male", string="Gender")
    user_id = fields.Many2one('res.users', string='Related User', default=lambda self: self.env.user, required=True)