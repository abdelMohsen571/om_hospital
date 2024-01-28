from odoo import models, fields, api


class HospitalPatiant(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Pationt Appointments'

    patiant_id = fields.Many2one('hospital.patiant',string="name",tracking=True)
    gender = fields.Selection(related='patiant_id.gender',string="Gender",readonloy=True)
    appointment_time=fields.Datetime(string='Appointment Time',default=fields.Datetime.now())
    booking_date=fields.Date(string='Booking Date',defautl=fields.Date.context_today)

