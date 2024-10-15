from odoo import http
from odoo.http import request

class CustomPopupController(http.Controller):

   @http.route('/crm/custom_popup', type='json', auth='user', website=True)
   def action_open_custom_popup(self):
       return request.env.ref('crm_custom.custom_popup').render({})