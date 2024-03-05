from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval


class PlayGround(models.Model):
    _name = 'play.ground'
    _description ='Play Ground Description'

    DEFAULT_ENV_VARIABLES=""" #JFSDKFJASDJF;KSDF"""
    model_id=fields.Many2one('ir.model', string='Model')
    code=fields.Text(string='Code' , default=DEFAULT_ENV_VARIABLES)
    result=fields.Text(string='Result')

    def action_excute(self):
        try:
            if self.model_id:
                model=self.env[self.model_id.model]
            else:
                model=self
            self.result=safe_eval(self.code.strip(),{'self':   model})
        except Exception  as e :
            self.result=str(e)