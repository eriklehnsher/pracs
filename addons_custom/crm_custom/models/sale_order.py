from Demos.win32cred_demo import domain

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    crm_team_for_only_id = fields.Many2one('crm.team.for.only', string='Sale Team Custom', domain="[('type','=','sale team custom'), '|', ('team_id', '=', team_id), ('team_id', '=', False)]")

