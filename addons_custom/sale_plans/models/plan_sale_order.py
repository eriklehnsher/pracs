from odoo import models, fields, api


class PlanSaleOrder(models.Model):
    _name = "plan.sale.order"
    _description = "Sale Plan"

    name = fields.Char(string="Tiêu đề", required=True)  # tiêu đề của kế hoạch
    approver_ids = fields.Many2many('res.partner', string='Người phê duyệt')  # người phê duyệt
    quotation_template_ids = fields.Many2one(
        "sale.order", string="Mẫu báo giá", readonly=True
    )  # mẫu báo giá
    plan_sale_order_info = fields.Text(
        string="Thông tin kế hoạch", required=True
    )  # thông tin kế hoạch
    state = fields.Selection(
        [ 
            ("draft", "Nháp"),
            ("confirmed", "Xác nhận"),
            ("cancel", "Hủy"),
        ],
        string="Trạng thái",
        default="draft",
    )

    def action_confirm(self):
        for rec in self:
            rec.state = "confirmed"
        return True

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"
        return True

    def save_action(self):
        for rec in self:
            rec.write({"state": "confirmed"})
        return True
