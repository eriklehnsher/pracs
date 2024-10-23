from odoo import models, fields, api


class CrmLeadNew(models.Model):
    _name = 'crm.team.new'
    _description = 'CRM Teams'

    team_id = fields.Many2many('crm.team', string='Teams')
    name = fields.Char(related='team_id.name', string='Name', required=True)
    create_date = fields.Datetime(String='Create Date', required=True)
    target_jan = fields.Float(related='team_id.target_jan', string='January Target', required=True)
    target_feb = fields.Float(related='team_id.target_feb', string='February Target', required=True)
    target_mar = fields.Float(related='team_id.target_mar', string='March Target', required=True)
    target_apr = fields.Float(related='team_id.target_apr', string='April Target', required=True)
    target_may = fields.Float(related='team_id.target_may', string='May Target', required=True)
    target_jun = fields.Float(related='team_id.target_jun', string='June Target', required=True)
    target_jul = fields.Float(related='team_id.target_jul', string='July Target', required=True)
    target_aug = fields.Float(related='team_id.target_aug', string='August Target', required=True)
    target_sep = fields.Float(related='team_id.target_sep', string='September Target', required=True)
    target_oct = fields.Float(related='team_id.target_oct', string='October Target', required=True)
    target_nov = fields.Float(related='team_id.target_nov', string='November Target', required=True)
    target_dec = fields.Float(related='team_id.target_dec', string='December Target', required=True)
    min_revenue = fields.Float(related='team_id.', string='Minimum Revenue', readonly=True)

    @api.model
    def create(self, vals):
        team_id = vals.get('team_id')
        if team_id:
            team_id = self.env['crm.team'].browse(team_id)
            vals.update({
                'name': team_id.name,
                'create_date': fields.Datetime.now(),
                'target_jan': team_id.target_jan,
                'target_feb': team_id.target_feb,
                'target_mar': team_id.target_mar,
                'target_apr': team_id.target_apr,
                'target_may': team_id.target_may,
                'target_jun': team_id.target_jun,
                'target_jul': team_id.target_jul,
                'target_aug': team_id.target_aug,
                'target_sep': team_id.target_sep,
                'target_oct': team_id.target_oct,
                'target_nov': team_id.target_nov,
                'target_dec': team_id.target_dec,
                'min_revenue': team_id.sale_team_id.min_revenue if team_id.sale_team_id else 0,
            })
        return super(CrmTeamNew, self).create(vals)
