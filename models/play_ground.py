from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval


class PlayGround(models.Model):
    _name = 'play.ground'
    _description ='Play Ground Description'

