from odoo import api, fields, models
class CreateAppointment(models.TransientModel):
    _name = "cancel.appointment.wizard"

    appointment_id=fields.Many2one('hospital.appointment',string='Appointment')
    reason=fields.Text(string='reason')

    def cancel_appointment(self):
        print('appointment canceld')