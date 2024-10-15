{
    'name': 'CRM Custom',
    'version': '1.0',
    'depends': ['crm', 'sale', 'sales_team'],
    'data': [
        'security/crm_security_inherit.xml',
        'security/ir.model.access.csv',
        # 'views/crm_team_target_modal_views.xml',
        'views/crm_team_inherit_views.xml',
        'views/crm_lead_inherit_views.xml',
        'wizard/crm_lead_report_views.xml',
    ],
  
}