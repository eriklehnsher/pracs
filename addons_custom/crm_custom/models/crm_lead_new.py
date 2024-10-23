from odoo import models, fields, api


class CrmLeadNew(models.Model):
    _name = 'crm.lead.new'
    _description = 'CRM Lead New'

    lead_id = fields.Many2one('crm.lead', string='Lead')
    team_id = fields.Many2one('crm.team', string='Team')
    create_date = fields.Datetime(related='lead_id.create_date', string='Create Date')
    sale_amount_total = fields.Float(related='lead_id.sale_amount_total', string='Sale Amount Total')

    @api.model
    def create_new_record(self, lead_id, team_id):
        return self.create({
            'lead_id': lead_id,
            'team_id': team_id,
        })
    def action_open_crm_lead_new_popup(self):
        self.ensure_one()
        return {
            'name': 'Popup',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead.new',
            'view_mode': 'tree',
            'target': 'new',
        }