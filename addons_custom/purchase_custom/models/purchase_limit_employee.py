from odoo import models, fields, api


class PurchaseLimitEmployee(models.Model):
    _name = 'purchase.limit.employee'
    _description = 'Purchase Limit Employee'

    employees_id = fields.Many2one('res.users', string='Nhân Viên', required=True)
    limit_amount = fields.Float(string='Limit Amount', required=True)

    @api.constrains('limit_amount')
    def _check_limit_amount(self):
        for record in self:
            if record.limit_amount <= 0:
                raise ValueError('Limit Amount must be greater than 0')
