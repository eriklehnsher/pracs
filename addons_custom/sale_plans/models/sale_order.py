from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    plan_sale_order_id = fields.Many2one('plan.sale.order', string='Kế hoạch bán hàng')    # kế hoạch bán hàng
    
    def action_create_plan_sale_order(self):
        self.ensure_one()
        plan_sale_order = self.env['plan.sale.order'].create({
            'name': self.name,
            'quotation_template_ids': self.id,
            'plan_sale_order_info': self.note,
        })
        self.plan_sale_order_id = plan_sale_order.id
        return {
            'name': 'Kế hoạch bán hàng',
            'type': 'ir.actions.act_window',
            'res_model': 'plan.sale.order',
            'res_id': plan_sale_order.id,
            'view_mode': 'form',
            'target': 'current',
        }
            
