{
    'name': 'Kế Hoạch Kinh Doanh',
    'version': '1.0',
    'category': 'Sales',
    'description': """
        KH kinh doanh
    """,
    'author': 'Erik.',
    'depends': ['sale'],
    'data': [
        'views/plan_sale_order.xml',
        'views/sale_order_inherit.xml',
        'security/ir.model.access.csv'
    ],
}