from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    department_id = fields.Many2one('hr.department', string='Department')
