from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class CrmTeamFilter(models.Model):
    _name = 'crm.team.filter'
    _description = 'CRM Team Filter'
    team_id = fields.Many2one('crm.team',  string='Teams')
    month = fields.Selection([
        (str(i), f"Tháng{i}") for i in range(1, 13)
    ], string='thán', required=True)
    def action_apply_filter(self):
        selected_month = int(self.month) if self.month else False
        current_year = datetime.now().year
        if selected_month:
            start_date = datetime(current_year, selected_month, 1)
            end_date = start_date + relativedelta(months=1)
        else:
            start_date, end_date = None, None
        domain = []
        if start_date:
            domain.append(('create_date', '>=', start_date))
        if end_date:
            domain.append(('create_date', '<=', end_date))
        if self.team_id:
            domain.append(('team_id', '=', self.team_id.id))
        teams = self.env['crm.teams'].search(domain)

        return {
            'name': 'CRM Teams',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'crm.teams',
            'views': [(self.env.ref('crm_custom.crm_team_view_tree').id, 'tree')],
            'domain': [('id', 'in', teams.ids)],
            'context': {'default_team_id': self.team_id.id, 'selected_month': selected_month},
        }
