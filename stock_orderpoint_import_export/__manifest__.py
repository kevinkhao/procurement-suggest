# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Orderpoint Import Export',
    'description': """
        Import and export orderpoints according to chosen warehouses""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'https://www.akretion.com',
    'depends': ["stock"
    ],
    'data': [
        'views/stock_warehouse_orderpoint.xml',
    ],
    'demo': [
    ],
}
