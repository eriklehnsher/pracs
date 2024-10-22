from datetime import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class   CrmTeamList(models.TransientModel):
    _name = 'crm.team.list'
    _description = 'CRM Team List'

    team_id = fields.Many2one('crm.team', string='Team')
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

    def action_open_custom_lead_tree(self):
        selected_team = self.team_id.id if self.team_id else False
        selected_month = self.create_month
        current_year = datetime.now().year
        start_date = datetime(current_year, selected_month, 1)
        end_date = start_date + relativedelta(months=1, days=-1)
        domains = [('create_date', '>=', start_date), ('create_date', '<=', end_date)]
        if selected_team:
            domains.append(('team_id', '=', selected_team))
        leads = self.env['crm.team.for.only'].search(domains)

        return {
            'name': 'Lead List',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'tree',
            'views': [(self.env.ref('crm_custom.crm_lead_team_list_views').id, 'tree')],
            'domain': [('id', 'in', leads.ids)],
            'target': 'current',
        }