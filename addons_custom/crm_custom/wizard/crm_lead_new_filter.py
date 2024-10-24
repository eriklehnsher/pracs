from email.policy import default

from odoo import models, fields
from datetime import datetime
from odoo.osv import expression
from dateutil.relativedelta import relativedelta


class CrmLeadNewFilter(models.Model):
    _name = "crm.lead.new.filter"
    _description = "CRM Team Filter"

    team_ids = fields.Many2many("crm.team", string="Chọn Nhóm")
    month = fields.Selection(
        [(str(i), f"Tháng{i}") for i in range(1, 13)],
        string="Chọn Tháng",
        required=True,
        default=str(datetime.now().month),
    )

    def action_apply_filter(self):
        selected_month = int(self.month)
        selected_year = datetime.today().year
        start_date = datetime(selected_year, selected_month, 1)
        end_date = start_date + relativedelta(months=1, days=-1)
        ids = []
        opp_domain = [('create_date', '>=', start_date), ('create_date', '<=', end_date), ('type', '=', 'opportunity')]
        if self.team_ids:
            opp_domain.append(('team_id', 'in', self.team_ids.ids))
            lead_ids = self.env['crm.lead'].search(opp_domain)
        else:
            lead_ids = self.env['crm.lead'].search(opp_domain)
        data = {}  # key: team_id, value: total_amount
        for lead in lead_ids:
            amount = 0
            # find related sale order
            order_domain = [('opportunity_id', '=', lead.id), ('state', '=', 'sale')]
            orders = self.env['sale.order'].search(order_domain)
            print(orders, 'orders')
            if orders:
                amount = sum(order.amount_total for order in orders)
            if lead.team_id not in data:
                data[lead.team_id] = amount
            else:
                data[lead.team_id] += amount
            target = 0
            if self.month == '1':
                target = lead.team_id.target_jan
            elif self.month == '2':
                target = lead.team_id.target_feb
            elif self.month == '3':
                target = lead.team_id.target_mar
            elif self.month == '4':
                target = lead.team_id.target_apr
            elif self.month == '5':
                target = lead.team_id.target_may
            elif self.month == '6':
                target = lead.team_id.target_jun
            elif self.month == '7':
                target = lead.team_id.target_jul
            elif self.month == '8':
                target = lead.team_id.target_aug
            elif self.month == '9':
                target = lead.team_id.target_sep
            elif self.month == '10':
                target = lead.team_id.target_oct
            elif self.month == '11':
                target = lead.team_id.target_nov
            elif self.month == '12':
                target = lead.team_id.target_dec

        print(data, 'data')
        if len(data) > 0:
            for k in data:
                res_id = self.env['crm.lead.new'].create({
                    'team_id': k.id,
                    'sale_amount_total': data[k],
                    'target': target,
                })
                ids.append(res_id.id)
        return {
            "name": "CRM Teams",
            "type": "ir.actions.act_window",
            "view_mode": "tree",
            "res_model": "crm.lead.new",
            "views": [(self.env.ref("crm_custom.view_crm_lead_new_to_tree").id, "tree")],
            "domain": [("id", "in", ids)],

        }
