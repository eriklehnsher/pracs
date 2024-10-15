from odoo import models, fields, api
from odoo.api import depends


class CrmTeam(models.Model):
    _inherit = ["crm.team", "mail.activity.mixin", "mail.thread"]
    _name = 'crm.team'
    favorite_user_ids = fields.Many2many(
        'res.users', 'sale_team_favorite_user_rel', 'team_id', 'user_id', string='Favorite Users')
    # target_id = fields.One2many(
    #     'crm.team.target', 'team_id', string='Mục tiêu nhóm')  # mục tiêu nhóm

    # @api.depends('target_id')
    # def _compute_total_target(self):
    #     for team in self:
    #         team.total_target = sum(
    #             target.target_amount for target in team.target_id)

    # total_target = fields.Float(
    #     string='Tổng mục tiêu', compute='_compute_total_target', store=True)  # tổng mục tiêu

    target_jan = fields.Float(string=' tháng 1', )  # tháng 1
    target_feb = fields.Float(string=' tháng 2', )  # tháng 2
    target_mar = fields.Float(string=' tháng 3', )  # tháng 3
    target_apr = fields.Float(string=' tháng 4', )  # tháng 4
    target_may = fields.Float(string=' tháng 5', )  # tháng 5
    target_jun = fields.Float(string=' tháng 6', )  # tháng 6
    target_jul = fields.Float(string=' tháng 7', )  # tháng 7
    target_aug = fields.Float(string=' tháng 8', )  # tháng 8
    target_sep = fields.Float(string=' tháng 9', )  # tháng 9
    target_oct = fields.Float(string=' tháng 10', )  # tháng 10
    target_nov = fields.Float(string=' tháng 11', )  # tháng 11
    target_dec = fields.Float(string=' tháng 12', )  # tháng 12

    total_target_amount = fields.Monetary(
        string='Tổng mục tiêu', 
        compute='_compute_total_target_amount', 
        store=True, currency_field="currency_id")  # tổng mục tiêu

    @api.depends('target_jan', 'target_feb', 'target_mar', 'target_apr', 'target_may', 'target_jun', 
                 'target_jul', 'target_aug', 'target_sep', 'target_oct', 'target_nov', 'target_dec')
    def _compute_total_target_amount(self):
        for record in self:
            record.total_target_amount = record.target_jan + record.target_feb 
            + record.target_mar + record.target_apr + record.target_may + \
                record.target_jun + record.target_jul + record.target_aug + \
                record.target_sep + record.target_oct + record.target_nov + record.target_dec

    @api.constrains('target_jan', 'target_feb', 'target_mar', 'target_apr', 
                    'target_may', 'target_jun', 'target_jul', 'target_aug', 
                    'target_sep', 'target_oct', 'target_nov', 'target_dec')
    def _check_target(self):

        for record in self:
            targets = [
                record.target_jan,
                record.target_feb,
                record.target_mar,
                record.target_apr,
                record.target_may,
                record.target_jun,
                record.target_jul,
                record.target_aug,
                record.target_sep,
                record.target_oct,
                record.target_nov,
                record.target_dec
            ]
            for target in targets:
                if target is None or target <= 0:
                    raise models.ValidationError(
                        'Mục tiêu không thể nhỏ hơn 0')



    @api.model
    def action_open_export_data(self):
        self.ensure_one()
        return {
            'name': 'Export Data',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.team.target',
            'view_mode': 'tree',
            'target': 'new',
        }
