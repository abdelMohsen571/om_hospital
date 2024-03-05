from   odoo import models,fields,api,_
from datetime import date,datetime,timedelta
from odoo.exceptions import ValidationError
class PatientTags(models.Model):
    _name='patient.tags'


    name=fields.Char(string='Name',requried=1)
    active=fields.Boolean(string='Active')
    color = fields.Integer(string='Color')
    color_2 = fields.Char(string='Color2')
    sequence=fields.Integer(string='Sequence')

    _sql_constraints = [
        ('unique_tag_name', 'unique(name,active)','name must be unique if active true'),
        ('valid_seq', 'check(sequence>0)','sequence must be greater than 0')

    ]

