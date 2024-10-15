from odoo import models, fields, api

from odoo.exceptions import UserError

class CrmLead(models.Model):
    _inherit =[ "crm.lead", "mail.activity.mixin", "mail.thread"]
    _name = 'crm.lead'
    
    min_revenue = fields.Float(string='Doanh thu tối thiểu(trước VAT)',default="", readonly=False, required=True)
    create_month = fields.Selection([
        ('1', 'Tháng 1'),
        ('2', 'Tháng 2'),
        ('3', 'Tháng 3'),
        ('4', 'Tháng 4'),
        ('5', 'Tháng 5'),
        ('6', 'Tháng 6'),
        ('7', 'Tháng 7'),
        ('8', 'Tháng 8'),
        ('9', 'Tháng 9'),
        ('10', 'Tháng 10'),
        ('11', 'Tháng 11'),
        ('12', 'Tháng 12'),
    ], string='Tháng tạo',compute='_compute_create_month', default= lambda self: fields.datetime.now().month)
    
    @api.depends('create_date')
    def _compute_create_month(self):
        for lead in self:
            if lead.create_date:
               lead.create_month = lead.create_date.strftime('%m') 
            else:
                lead.create_month = fields.datetime.now().month
    
    @api.constrains('min_revenue')
    def _check_min_revenue(self):
            if self.min_revenue <= 0:
                raise UserError("Doanh thu tối thiểu phải lớn hơn 0")
            
    
    @api.depends('quotation_count')
    def write(self, vals):
        if self.quotation_count > 0 and 'min_revenue' in vals:
            raise UserError("Không thể thay đổi doanh thu tối thiểu khi đã có báo giá")
        return super(CrmLead, self).write(vals)
    
    
    # def action_set_lost(self, **additional_values):
    #     if self.priority != ' high' or not  self.env.user.has_group('sales_team.group_sale_manager'):
    #         raise UserError('Bạn không thể thực hiện hành động này')
    #     res = super(CrmLead, self).action_archive()
    #     if additional_values:
    #         self.write(additional_values)
    #     return res
    