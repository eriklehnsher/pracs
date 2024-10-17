from odoo import models, fields, api

class PurchaseLimitConfig(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'purchase.limit.config'
    _description = 'Purchase Limit Configuration'

    name = fields.Char(string='Name', required=True)
    limit_lines = fields.Many2many('purchase.limit.employee', string='Limit Lines')

