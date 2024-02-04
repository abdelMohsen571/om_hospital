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
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string="Priority", )
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'), ('done', 'Done'), ('canceled', 'Canceled ')],
                             default='draft', string="Status Bar")

    @api.onchange('patiant_id')
    def onchange_patiant_id(self):
        self.ref = self.patiant_id.ref

    def action_test(self):
        print('button clicked!!!!!!!!!!!11')
        return {
            'effect':{
                'fadeout':'slow',
                'message':'Click sucess',
                'type':'rainbow_man'
            }
        }
