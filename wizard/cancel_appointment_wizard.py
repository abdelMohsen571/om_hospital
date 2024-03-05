from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
import datetime


class CancelAppointment(models.TransientModel):
    _name = "cancel.appointment.wizard"

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment',
                                     domain=['|',('state', '=', 'draft'), ('priority', 'in', ('0', '1','')), ])
    reason = fields.Text(string='reason')
    date_cancel = fields.Date(string='Cancellation Date')

    def cancel_appointment(self):
        for rec in self:
            if rec.appointment_id.booking_date == fields.Date.today():
                raise ValidationError(_('sorry, cancellation is not allowed on the same day of booking'))
            return

    @api.model
    def default_get(self, fields_list):
        res = super(CancelAppointment, self).default_get(fields_list)
        res['date_cancel'] = datetime.date.today()
        res['reason'] = 'no reson'

        print('...........', res)
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res
