from odoo import models, fields, api
from odoo.exceptions import ValidationError



class HrDepartment(models.Model):
    _inherit = 'hr.department'
    limit_amount_per_month = fields.Float(string='Hạn Mức chi tiêu/tháng', required=True)
