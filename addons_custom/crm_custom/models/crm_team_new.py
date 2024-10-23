from odoo import models, fields, api



class CrmTeamNew(models.Model):
    _name = 'crm.team.new'
    _description = 'CRM Teams'

    team_id = fields.Many2many('crm.team',  string='Teams')
    name = fields.Char(related='team_id.name',string='Name', required=True)
    create_date = fields.Datetime(String='Create Date', required=True)
    target_jan = fields.Float(related='team_id.target_jan',string='January Target', required=True)
    target_feb = fields.Float(related='team_id.target_feb',string='February Target', required=True)
    target_mar = fields.Float(related='team_id.target_mar',string='March Target', required=True)
    target_apr = fields.Float(related='team_id.target_apr',string='April Target', required=True)
    target_may = fields.Float(related='team_id.target_may',string='May Target', required=True)
    target_jun = fields.Float(related='team_id.target_jun',string='June Target', required=True)
    target_jul = fields.Float(related='team_id.target_jul',string='July Target', required=True)
    target_aug = fields.Float(related='team_id.target_aug',string='August Target', required=True)
    target_sep = fields.Float(related='team_id.target_sep',string='September Target', required=True)
    target_oct = fields.Float(related='team_id.target_oct',string='October Target', required=True)
    target_nov = fields.Float(related='team_id.target_nov',string='November Target', required=True)
    target_dec = fields.Float(related='team_id.target_dec',string='December Target', required=True)

    @api.model
    def create_new_crm_team(self):
        new_crm_team_new = self.env['crm.team.new'].create({
            'team_id': self.team_id.ids,
            'name': self.name,
            'create_date': self.create_date,
            'target_jan': self.target_jan,
            'target_feb': self.target_feb,
            'target_mar': self.target_mar,
            'target_apr': self.target_apr,
            'target_may': self.target_may,
            'target_jun': self.target_jun,
            'target_jul': self.target_jul,
            'target_aug': self.target_aug,
            'target_sep': self.target_sep,
            'target_oct': self.target_oct,
            'target_nov': self.target_nov,
            'target_dec': self.target_dec,
        })
        return new_crm_team_new


