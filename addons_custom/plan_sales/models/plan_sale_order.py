from odoo import models, fields, api
from odoo.exceptions import UserError


class PlanSaleOrder(models.Model):
    _name = "plan.sale.order"
    _description = "Sale Plan"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Tiêu đề", required=True)  # tiêu đề của kế hoạch
    approver_ids = fields.Many2many(
        'res.partner', string='Người phê duyệt')  # người phê duyệt
    sale_order_id = fields.Many2one(
        "sale.order", string="Mẫu báo giá", readonly=True
    )  # mẫu báo giá
    plan_sale_order_info = fields.Text(
        string="Thông tin kế hoạch", required=True
    )  # thông tin kế hoạch
    state = fields.Selection(
        [("draft", "Nháp"),
            ('pending', 'Chờ xác nhận'),
            ("approved", "Duyệt "),
            ("rejected", "Từ chối"),
         ],
        string="Trạng thái",
        default="draft",
    )
    approved_by_ids = fields.Many2many(
        'res.partner',
        'plan_sale_approved_by_rel',  # Tên bảng liên kết mới
        'plan_id', 'partner_id', 
         string='Đã duyệt', readonly=True)
    created_at = fields.Datetime(
        string="Ngày tạo", default=fields.Datetime.now)
    updated_at = fields.Datetime(
        string="Ngày cập nhật", default=fields.Datetime.now)
    #creator_id bị trùng
    creater_id = fields.Many2one(
        'res.users', string="Người tạo", readonly=True, default=lambda self: self.env.user.id
    )  # default to current user

    def action_approve(self):
        current_user = self.env.user.partner_id
        if current_user in self.approver_ids and current_user not in self.approved_by_ids:
            self.approved_by_ids = [(4, current_user.id)]
            self.message_post(
                body=f"Người phê duyệt {current_user.name} đã phê duyệt kế hoạch.",
                message_type="notification",
                partner_ids=[current_user.id]
            )
            if len(self.approved_by_ids) == len(self.approver_ids):
                self.state = "approved"
                self.message_post(
                    body="Kế hoạch đã được tất cả người phê duyệt duyệt.",
                    message_type="notification",
                    partner_ids=[self.creater_id.partner_id.id]
                )
        else:
            raise UserError("Người phê duyệt không hợp lệ hoặc đã duyệt.")
        return True

    def action_reject(self):
        current_user = self.env.user.partner_id
        if current_user in self.approver_ids and current_user not in self.approved_by_ids:
            self.state = "rejected"
            self.message_post(
                body=f"Người phê duyệt {current_user.name} đã từ chối kế hoạch.",
                message_type="notification",
                partner_ids=[current_user.id]
            )
            if len(self.approved_by_ids) == len(self.approver_ids):
                self.state = "approved"
                self.message_post(
                    body="Kế hoạch đã được tất cả người phê duyệt duyệt.",
                    message_type="notification",
                    partner_ids=[self.creater_id.partner_id.id]
                )
        else:
            raise UserError("Người phê duyệt không hợp lệ hoặc đã duyệt.")
            
        

    def action_sent_for_approval(self):
        if not self.approver_ids:
            raise UserError("Vui lòng chọn người phê duyệt")
        self.state = "pending"

        for approver in self.approver_ids:
            self.message_post(
                body="Kế hoạch đã được gửi phê duyệt.",
                message_type="notification",
                partner_ids=[approver.id],
            )
        return True
