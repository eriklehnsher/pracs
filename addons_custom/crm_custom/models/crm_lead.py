import csv
import base64
from io import StringIO as stringIO
from odoo import models, fields, api
from odoo.exceptions import UserError
import calendar
from datetime import datetime

import logging


class CrmLead(models.Model):
    _inherit = "crm.lead"
    min_revenue = fields.Float(string='Doanh thu tối thiểu(trước VAT)', default="", readonly=False, required=True)
    create_month = fields.Selection(
        selection=lambda self: [(str(i), datetime.strptime(str(i), '%m').strftime('%B')) for i in range(1, 13)],
        string='Tháng tạo',
        required=True,
        default=lambda self: str(datetime.now().month),
    )

    @api.model
    def create(self, vals):
        if 'create_date' in vals:
            create_date = fields.Datetime.from_string(vals['create_date'])
            vals['create_month'] = str(create_date.month)  # Thiết lập tháng tạo từ create_date
        else:
            vals['create_month'] = str(datetime.now().month)  # Tháng hiện tại nếu không có create_date
        return super(CrmLead, self).create(vals)

    def update_create_month_for_existing_leads(self):
        leads = self.search([('create_month', '=', False)])  # Tìm kiếm các cơ hội chưa có giá trị create_month
        for lead in leads:
            lead.create_month = str(lead.create_date.month)  # Cập nhật create_month dựa trên create_date

    @api.constrains('min_revenue')
    def _check_min_revenue(self):
        if self.min_revenue <= 0:
            raise UserError("Doanh thu tối thiểu phải lớn hơn 0")
    @api.depends('quotation_count')
    def write(self, vals):
        if self.quotation_count > 0 and 'min_revenue' in vals:
            raise UserError("Không thể thay đổi doanh thu tối thiểu khi đã có báo giá")
        return super(CrmLead, self).write(vals)
    @api.model
    def action_open_crm_lead_popup(self):
        self.ensure_one()
        return {
            'name': 'Popup',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'tree',
            'target': 'new',
        }
    def action_report_lead_specific_fields(self):
        team_id = self.team_id.id
        create_month = self.create_month
        leads = self.search([('team_id', '=', team_id), ('create_month', '=', create_month)])
        if not leads:
            raise UserError("Không tìm thấy dữ liệu để xuất.")
        return self.env.ref('crm_custom.action_report_lead_specific_fields').report_action(leads)
