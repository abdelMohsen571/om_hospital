from odoo import models, fields, api
from datetime import date,datetime,timedelta



class HospitalPatiant(models.Model):
    _name = 'hospital.patiant'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Pationt description'

    name = fields.Char(string="name",tracking=True)
    img=fields.Image()
    ref = fields.Text(string='Reference')
    date_of_birth=fields.Date(string='Date Of Birth')
    age = fields.Integer(string="age",compute='_compute_age',store=True)
    gender=fields.Selection([('male','Male'),('female','Female')])
    active=fields.Boolean(string="active",default=True)
    tags_ids=fields.Many2many('patient.tags', string='Patient Tags')


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            currentYear=date.today()
            if rec.date_of_birth:
                rec.age=currentYear.year-rec.date_of_birth.year
            else:
                rec.age=1

