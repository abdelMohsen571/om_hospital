from   odoo import models,fields,api,_
from datetime import date,datetime,timedelta
from odoo.exceptions import ValidationError
class PatientTags(models.Model):
    _name='patient.tags'


    name=fields.Char(string='Name',requried=1)
    active=fields.Boolean(string='Active')
    color = fields.Integer(string='Color')


