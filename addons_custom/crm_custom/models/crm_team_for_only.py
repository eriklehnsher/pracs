from odoo import models, fields, api
from datetime import datetime

class CrmTeamForOnly(models.Model):
    _name = 'crm.team.for.only'
    _description = 'CRM Team For Only'

    name = fields.Char(related='team_id.name', string='Name', required=True)
    team_id = fields.Many2one('crm.team', string='Team')
    company_id = fields.Many2one('res.company', related='team_id.company_id', string='Company', store=True,
                                 readonly=True)
    target_jan = fields.Float(related='team_id.target_jan', string=' tháng 1', )  # tháng 1
    target_feb = fields.Float(related='team_id.target_feb', string=' tháng 2', )  # tháng 2
    target_mar = fields.Float(related='team_id.target_mar', string=' tháng 3', )  # tháng 3
    target_apr = fields.Float(related='team_id.target_apr', string=' tháng 4', )  # tháng 4
    target_may = fields.Float(related='team_id.target_may', string=' tháng 5', )  # tháng 5
    target_jun = fields.Float(related='team_id.target_jun', string=' tháng 6', )  # tháng 6
    target_jul = fields.Float(related='team_id.target_jul', string=' tháng 7', )  # tháng 7
    target_aug = fields.Float(related='team_id.target_aug', string=' tháng 8', )  # tháng 8
    target_sep = fields.Float(related='team_id.target_sep', string=' tháng 9', )  # tháng 9
    target_oct = fields.Float(related='team_id.target_oct', string=' tháng 10', )  # tháng 10
    target_nov = fields.Float(related='team_id.target_nov', string=' tháng 11', )  # tháng 11
    target_dec = fields.Float(related='team_id.target_dec', string=' tháng 12', )  # tháng 12

    create_date = fields.Datetime( string='Create Date', readonly=True)
    orders_id = fields.One2many('sale.order', 'team_id', string='Orders')
    sale_amount_totals = fields.Monetary(compute='_compute_sale_amount_totals', string='Sale Amount Totals', store=True,
                                         currency_field='company_currency')
    @api.depends('orders_id.state', 'orders_id.currency_id', 'orders_id.amount_untaxed', 'orders_id.date_order',
                 'orders_id.company_id', 'orders_id.team_id')
    def _compute_sale_amount_totals(self):
        for record in self:
            company_currency = record.company_currency or self.env.company.currency_id
            sale_orders = record.orders_id.filtered_domain(self._get_lead_sale_order_domain())
            record.sale_amount_totals = sum(
                order.currency_id._convert(
                    order.amount_untaxed, company_currency, order.company_id, order.date_order or fields.Date.today()
                )
                for order in sale_orders
            )
