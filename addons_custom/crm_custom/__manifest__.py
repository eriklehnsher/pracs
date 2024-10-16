{
    'name': 'CRM Custom',
    'version': '1.0',
    'depends': ['crm', 'sale', 'sales_team'],
    'data': [
        'security/crm_security_inherit.xml',
        'security/ir.model.access.csv',
        'wizard/crm_lead_popup_views.xml',
        'views/crm_team_inherit_views.xml',
        'views/crm_lead_inherit_views.xml', 
        'views/assets.xml',
    ],
  
}