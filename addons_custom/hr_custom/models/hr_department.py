from odoo import models, fields, api
from odoo.exceptions import ValidationError



class HrDepartment(models.Model):
    _inherit = 'hr.department'

    limit_amount_per_month = fields.Float(string='Limit Amount Per Month', required=True)
    @api.constrains('limit_amount_per_month')
    def _check_limit_amount_per_month(self):
        for record in self:
            if record.limit_amount_per_month < 0:
                raise ValidationError('Limit Amount Per Month must be greater than 0')
            if record.limit_amount_per_month > 1000000:
                raise ValidationError('Limit Amount Per Month must be less than 1000000')
