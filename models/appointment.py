from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Pationt Appointments'

    patiant_id = fields.Many2one('hospital.patiant', string="name", tracking=True)
    ref = fields.Text(string='Refrence')
    gender = fields.Selection(related='patiant_id.gender', string="Gender", readonloy=True)
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now())
    booking_date = fields.Date(string='Booking Date', defautl=fields.Date.context_today)


    @api.onchange('patiant_id')
    def onchange_patiant_id(self):
      self.ref = self.patiant_id.ref
