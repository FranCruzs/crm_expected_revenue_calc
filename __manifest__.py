{
    'name': 'CRM Sale Subtotal Sync',
    'version': '1.0',
    'summary': 'Synchronize sale order subtotal to CRM lead expected revenue',
    'description': """
        This module synchronizes the subtotal of related sale orders to the expected revenue field in CRM leads.
    """,
    'author': 'Fran Cruz',
    'website': 'https://www.linkedin.com/in/francisco-cruz-1b918b27b/',
    'category': 'CRM',
    'depends': ['crm', 'sale'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
 

}
