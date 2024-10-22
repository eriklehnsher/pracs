from odoo import models, fields, api



class CrmTeams(models.Model):
    _name = 'crm.teams'
    _description = 'CRM Teams'

    teams_id = fields.Many2one('crm.team',  string='Teams')
    name = fields.Char(related='teams_id.name',string='Name', required=True)
    create_date = fields.Datetime(String='Create Date', required=True)
    target_jan = fields.Float(related='teams_id.target_jan',string='January Target', required=True)
    target_feb = fields.Float(related='teams_id.target_feb',string='February Target', required=True)
    target_mar = fields.Float(related='teams_id.target_mar',string='March Target', required=True)
    target_apr = fields.Float(related='teams_id.target_apr',string='April Target', required=True)
    target_may = fields.Float(related='teams_id.target_may',string='May Target', required=True)
    target_jun = fields.Float(related='teams_id.target_jun',string='June Target', required=True)
    target_jul = fields.Float(related='teams_id.target_jul',string='July Target', required=True)
    target_aug = fields.Float(related='teams_id.target_aug',string='August Target', required=True)
    target_sep = fields.Float(related='teams_id.target_sep',string='September Target', required=True)
    target_oct = fields.Float(related='teams_id.target_oct',string='October Target', required=True)
    target_nov = fields.Float(related='teams_id.target_nov',string='November Target', required=True)
    target_dec = fields.Float(related='teams_id.target_dec',string='December Target', required=True)



