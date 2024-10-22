import csv
import base64
from io import StringIO as stringIO

from pkg_resources import require

from odoo import models, fields, api
from odoo.exceptions import UserError
import calendar
from datetime import datetime
from io import StringIO
import logging


class CrmLead(models.Model):
    _inherit = "crm.lead"
    min_revenue = fields.Float(string='Doanh thu tối thiểu(trước VAT)', default="", readonly=False, required=True)

    create_month = fields.Selection([
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    ], string="Create Month")

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



    def _compute_create_month(self):
        for record in self:
            if record.create_date:
                record.create_month = str(record.create_date.month)
            else:
                record.create_month = False

    def action_open_custom_lead_tree(self):
        selected_team = self.team_id.id if self.team_id else False
        selected_month = self.create_month

        domain = []

        if selected_team:
            domain.append(('team_id', '=', selected_team))
        if selected_month:
            domain.append(('create_month', '=', selected_month))

        return {
            'name': 'Custom Lead Tree',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'tree',
            'view_id': self.env.ref('custom_crm_lead_tree_view').id,
            'domain': domain,
            'target': 'current',
        }

    @api.constrains('min_revenue')
    def _check_min_revenue(self):
        if self.min_revenue <= 0:
            raise UserError("Doanh thu tối thiểu phải lớn hơn 0")

    @api.depends('quotation_count')
    def write(self, vals):
        if self.quotation_count > 0 and 'min_revenue' in vals:
            raise UserError("Không thể thay đổi doanh thu tối thiểu khi đã có báo giá")
        return super(CrmLead, self).write(vals)
