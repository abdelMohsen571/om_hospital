from odoo import api, fields, models
from datetime import date,datetime,timedelta
import datetime
class CancelAppointment(models.TransientModel):
    _name = "cancel.appointment.wizard"

    appointment_id=fields.Many2one('hospital.appointment',string='Appointment')
    reason=fields.Text(string='reason')
    date_cancel=fields.Date(string='Cancellation Date')

    def cancel_appointment(self):
        print('appointment canceld')
    @api.model
    def default_get(self, fields_list):
        res=super(CancelAppointment,self).default_get(fields_list)
        res['date_cancel']=datetime.date.today()
        res['reason']='no reson'

        print('...........',res)
        if self.env.context.get('active_id'):
            res['appointment_id']=self.env.context.get('active_id')
        return res