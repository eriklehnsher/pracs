from odoo import models, fields, api


class CrmLeadNew(models.Model):
    _name = 'crm.lead.new'
    _description = 'CRM Lead New'

    lead_id = fields.Many2one('crm.lead', string='Lead')
    team_id = fields.Many2one('crm.team', string='Team')

    sale_amount_total = fields.Monetary(related='lead_id.sale_amount_total', string='Sale Amount Total', readonly=True)
    currency_id = fields.Many2one(related='lead_id.company_currency', string='Currency', readonly=True)
    target = fields.Float(string='Chỉ tiêu doanh thu')


