from email.policy import default

from odoo import models, fields
from datetime import datetime
from odoo.osv import expression



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
        ids = []
        if self.team_ids:
            lead_ids = self.env['crm.lead'].search([('team_id', 'in',  self.team_ids.ids)]).filtered(lambda l: l.create_date.month == int(self.month))
        else:
            lead_ids = self.env['crm.lead'].search([]).filtered(
                lambda l: l.create_date.month == int(self.month))

        for lead in lead_ids:
            domain = expression.AND([[('opportunity_id', '=', lead.id)], lead._get_lead_sale_order_domain()])
            order_ids = self.env['sale.order'].search(domain)

            target = 0
            if self.month == '10':
                target = lead.team_id.target_oct
            elif self.month == '11':
                target = lead.team_id.target_nov

            res_id = self.env['crm.lead.new'].create({
                'lead_id': lead.id,
                'team_id': lead.team_id.id,
                'sale_amount_total': sum(order.amount_total for order in order_ids),
                'target': target,
            })
            ids.append(res_id.id)

        print(ids)

        return {
            "name": "CRM Teams",
            "type": "ir.actions.act_window",
            "view_mode": "tree",
            "res_model": "crm.lead.new",
            "views": [(self.env.ref("crm_custom.view_crm_lead_new_to_tree").id, "tree")],
            "domain": [("id", "in", ids)],
            # "context": {"selected_month": selected_month},
        }


        # selected_month = int(self.month) if self.month else False
        # current_year = datetime.now().year
        # if selected_month:
        #     start_date = datetime(current_year, selected_month, 1)
        #     end_date = start_date + relativedelta(months=1)
        # else:
        #     start_date, end_date = None, None
        # domain = []
        # if start_date:
        #     domain.append(("create_date", ">=", start_date))
        # if end_date:
        #     domain.append(("create_date", "<=", end_date))
        # if self.team_id:
        #     domain.append(("team_id", "in", self.team_id.ids))
        # leads = self.env["crm.lead"].search(domain)
        # if not leads:
        #    raise UserError('No leads found for the selected criteria.')
        #

