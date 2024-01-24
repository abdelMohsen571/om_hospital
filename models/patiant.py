from odoo import models, fields, api


class HospitalPatiant(models.Model):
    _name = 'hospital.patiant'
    _description = 'Pationt description'

    name = fields.Char(string="name")
    age = fields.Integer(string="age")
    description = fields.Text()
