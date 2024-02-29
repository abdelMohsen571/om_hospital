from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'inherit sale order'

    confirmed_user_id = fields.Many2one('res.users',string='Confirmed User')

    def action_confirm(self):
        print('inherited funcation success')
        super(SaleOrder,self).action_confirm()
        self.confirmed_user_id=self.env.user.id