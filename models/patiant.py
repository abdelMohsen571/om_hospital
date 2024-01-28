from odoo import models, fields, api


class HospitalPatiant(models.Model):
    _name = 'hospital.patiant'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Pationt description'

    name = fields.Char(string="name",tracking=True)
    age = fields.Integer(string="age")
    description = fields.Text()
    gender=fields.Selection([('male','Male'),('female','Female')])
    active=fields.Boolean(string="active",default=True)

