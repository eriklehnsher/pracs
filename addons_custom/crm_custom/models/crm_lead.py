from odoo import models, fields, api

from odoo.exceptions import UserError

class CrmLead(models.Model):
    _inherit =[ "crm.lead", "mail.activity.mixin", "mail.thread"]
    _name = 'crm.lead'
    
    min_revenue = fields.Float(string='Doanh thu tối thiểu(trước VAT)', readonly=False, required=True)
    
    @api.constrains('min_revenue')
    def _check_min_revenue(self):
            if self.min_revenue <= 0:
                raise UserError("Doanh thu tối thiểu phải lớn hơn 0")
            
    
    @api.depends('quotation_count')
    def write(self, vals):
        if self.quotation_count > 0 and 'min_revenue' in vals:
            raise UserError("Không thể thay đổi doanh thu tối thiểu khi đã có báo giá")
        return super(CrmLead, self).write(vals)