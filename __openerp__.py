{
    'name' : 'OpenERP Pet Store',
    'version': '1.0',
    'summary': 'Sell pet toys',
    'category': 'Tools',
    'description':
        """
OpenERP Pet Store
=================

A wonderful application to sell pet toys.
        """,
    'data': [
        "petstore.xml",
        "oepetstore.message_of_the_day.csv",
        "security/ir.model.access.csv",
    ],
    'depends' : ['sale_stock'],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}
