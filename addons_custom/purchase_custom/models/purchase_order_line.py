from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    suplier_recomend = fields.Char(string='Suplier Recomend')