from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class CrmLeadOpporFilter(models.TransientModel):
    _name = 'crm.lead.oppor.filter'
    _description = 'Filter Opportunities from Leads'
    year = fields.Selection([
        (str(i), f"Năm {i}") for i in range(2020, 2031)
    ], string="Năm", required=True)

    month = fields.Selection([
        (str(i), f"tháng {i}") for i in range(1, 13)
    ], string="Tháng", required=True)

    def action_filter_oppor(self):
        selected_month = int(self.month)
        selected_year = int(self.year)
        start_date = datetime(selected_year, selected_month, 1)
        end_date = start_date + relativedelta(months=1, days=-1)
        oppors = self.env['crm.lead'].search([
            ('create_date', '>=', start_date),
            ('create_date', '<=', end_date),

        ])

        return {
            'name': 'Opportunities from Leads',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'tree',

            'views': [(self.env.ref('crm_custom.crm_lead_oppor_custom_views').id, 'tree')],
            'domain': [('id', 'in', oppors.ids)],
        }
