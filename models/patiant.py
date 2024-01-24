from odoo import models, fields, api


class HospitalPatiant(models.Model):
    _name = 'hospital.patiant'
    _description = 'Pationt description'

    name = fields.Char(string="name")
    description = fields.Text()
