{
    'name': 'Sale Customer Accepted',
    'version': '1.0',
    'summary': 'Adds a Customer Accepted state between Quotation Sent and Sales Order',
    'description': """
        This module adds a new 'Customer Accepted' stage to sale orders,
        sitting between the quotation sent and sales order confirmation.
    """,
    'author': 'Ahex',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/custom_sale.xml',
        'data/external.xml',
        'views/template.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
