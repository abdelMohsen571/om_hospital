from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
from dateutil import relativedelta
from odoo.exceptions import ValidationError


class HospitalPatiant(models.Model):
    _name = 'hospital.patiant'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Pationt description'

    name = fields.Char(string="name", tracking=True, default='user name')
    img = fields.Image()
    ref = fields.Text(string='Reference', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth', tracking=True)
    age = fields.Integer(string="age", compute='_compute_age', inverse="_inverse_compute_age", search='_search_age',
                         tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True)
    active = fields.Boolean(string="active", default=True, tracking=True)
    tags_ids = fields.Many2many('patient.tags', string='Patient Tags', tracking=True)
    old_name1 = fields.Char(string='old name', default='old')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            currentYear = date.today()
            if rec.date_of_birth:
                rec.age = currentYear.year - rec.date_of_birth.year
            else:
                rec.age = 1

    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

    @api.model
    def create(self, vals_list):
        vals_list['ref'] = self.env['ir.sequence'].next_by_code('hospital.patiant')
        return super(HospitalPatiant, self).create(vals_list)

    @api.constrains('date_of_birth')
    def check_dat_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_('this data no acceptable'))


    your_field = fields.Char(string='Your Field')
    previous_value = fields.Char(string='Previous Value')

    @api.model
    def create(self, values):
        record = super(HospitalPatiant, self).create(values)
        print("Field value before editing:", record.your_field)
        return record

    def _search_age(self,operator,value):
        date_of_birth=date.today()-relativedelta.relativedelta(years=value)
        start_date=date_of_birth.replace(day=1,month=1)
        end_date=date_of_birth.replace(day=31,month=12)
        print(start_date,end_date)
        return [('date_of_birth','>=',start_date),('date_of_birth','<=',end_date),]
