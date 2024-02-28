from odoo import api, fields, models
class CreateAppointment(models.TransientModel):
    _name = "create.appointment.wizard"

    name=fields.Char(string='Name')
    patiant_id = fields.Many2one('hospital.patiant', string="name", tracking=True)

    def create_appointment(self):
        print('appointment ceratedd')
