{
    'name': "om_hospital",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'sequence': -100,
    'author': "",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu_view.xml',
        'views/patiant_view.xml',
        'views/female_patiant_view.xml',
        'views/appointment_view.xml',
        'views/users.xml',
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
