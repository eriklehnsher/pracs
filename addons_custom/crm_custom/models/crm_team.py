from odoo import models, fields, api
from odoo.api import depends


class CrmTeam(models.Model):
    _inherit = ["crm.team", "mail.activity.mixin", "mail.thread"]


    target_ids = fields.One2many('crm.team.target', 'team_id', string='Mục tiêu nhóm')  # mục tiêu nhóm

    @api.depends('target_ids')
    def _compute_total_target(self):
        for team in self:
            team.total_target = sum(target.target_amount for target in team.target_ids)

    total_target = fields.Float(string='Tổng mục tiêu', compute='_compute_total_target', store=True)  # tổng mục tiêu