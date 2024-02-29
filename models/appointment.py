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
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sale_price = fields.Boolean(string="Hide Sale Price")

    @api.onchange('patiant_id')
    def onchange_patiant_id(self):
        self.ref = self.patiant_id.ref

    def action_test(self):
        print('button clicked!!!!!!!!!!!11')
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click sucess',
                'type': 'rainbow_man'
            }
        }

    def action_cancel(self):
        action = self.env.ref('om_hospital.cancel_appointment_wizard_action').read()[0]
        return action


    def action_waiting(self):
        for rec in self:
           rec.state = 'waiting'


    def action_done(self):
        for rec in self:
            rec.state = 'done'


    def action_draft(self):
        for rec in self:
            rec.state = 'draft'


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product', requried=True)
    price_unit = fields.Float(string='Price', related='product_id.list_price')
    qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
