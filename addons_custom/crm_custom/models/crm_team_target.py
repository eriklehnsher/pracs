from odoo import models, fields, api


class CrmTeamTarget(models.Model):
    _name ="crm.team.target"
    _description = "CRM Team Target"

    member_ids = fields.Many2many('res.partner', string='Thành viên', required=True)  # thành viên
    team_id = fields.Many2one('crm.team', string='Nhóm bán hàng', required=True)  # nhóm
    months = fields.Selection([ ('1', 'Tháng 1'),
                                ('2', 'Tháng 2'),
                                ('3', 'Tháng 3'),
                                ('4', 'Tháng 4'),
                                ('5', 'Tháng 5'),
                                ('6', 'Tháng 6'),
                                ('7', 'Tháng 7'),
                                ('8', 'Tháng 8'),
                                ('9', 'Tháng 9'),
                                ('10', 'Tháng 10'),
                                ('11', 'Tháng 11'),
                                ('12', 'Tháng 12')], string='Tháng', required=True)  # tháng
    target = fields.Float(string='Mục tiêu', required=True)  # mục tiêu



