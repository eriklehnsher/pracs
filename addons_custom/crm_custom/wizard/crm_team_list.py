from odoo import models, fields, api


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
        start_date = datetime( selected_month, 1)

        teams = self.env['crm.team.for.only'].search([
            ('create_date')



        return {
            'name': 'Lead List',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'tree',
            'views': [(self.env.ref('crm_custom.crm_lead_team_list_views').id, 'tree')],

            'target': 'current',
        }