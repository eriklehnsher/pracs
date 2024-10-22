{
    'name': 'CRM Custom',
    'version': '1.0',
    'depends': ['crm', 'sale', 'sales_team', 'sale_crm'],
    'data': [
        'security/crm_security_inherit.xml',
        'security/ir.model.access.csv',
        # 'views/crm_lead_popup.xml',
        'views/crm_lead_oppor_custom_views.xml',
        'wizard/crm_lead_oppor_filter_views.xml',
        'wizard/crm_team_list_views.xml',
        'views/crm_team_inherit_views.xml',
        'views/crm_lead_inherit_views.xml',
        'views/assets.xml',
    ],
}
