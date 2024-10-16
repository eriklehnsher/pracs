import csv
import base64
from io import StringIO as stringIO
from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    min_revenue = fields.Float(string='Doanh thu tối thiểu(trước VAT)', default="", readonly=False, required=True)
    create_month = fields.Selection([
        ('01', 'Tháng 1'),
        ('02', 'Tháng 2'),
        ('03', 'Tháng 3'),
        ('04', 'Tháng 4'),
        ('05', 'Tháng 5'),
        ('06', 'Tháng 6'),
        ('07', 'Tháng 7'),
        ('08', 'Tháng 8'),
        ('09', 'Tháng 9'),
        ('10', 'Tháng 10'),
        ('11', 'Tháng 11'),
        ('12', 'Tháng 12'),
    ], string='Tháng tạo', compute='_compute_create_month',
        default=lambda self: str(fields.Date.context_today(self).month).zfill(2))

    @api.depends('create_date')
    def _compute_create_month(self):
        for lead in self:
            if lead.create_date:
                lead.create_month = str(lead.create_date.month).zfill(2)  # Đảm bảo định dạng hai chữ số
            else:
                lead.create_month = str(fields.Date.context_today(self).month).zfill(2)  # Tháng hiện tại

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

    def action_export_crm_lead_data(self):
        output = stringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
        field_names = ['name', 'min_revenue', 'create_month', 'team_id', 'user_id']
        writer.writerow(field_names)

        for lead in self:
            writer.writerow([getattr(lead, field_name) for field_name in field_names])

        csv_data = base64.b64encode(output.getvalue().encode())
        output.close()

        attachment = self.env['ir.attachment'].create({
            'name': 'crm_lead.csv',
            'type': 'binary',
            'datas': csv_data,
            'datas_fname': 'crm_lead.csv',
            'res_model': 'crm.lead',
            'res_id': self.id,
            'mime_type': 'text/csv'  # Đúng là mime_type, không phải mine_type
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self'
        }
