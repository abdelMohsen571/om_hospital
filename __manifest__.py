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
    'depends': ['base','mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu_view.xml',
        'views/patiant_view.xml',
        'views/female_patiant_view.xml',
        'views/appointment_view.xml',
        'views/patient_tags_view.xml',
        'views/users.xml',
        'wizard/create_appointment_wizard_view.xml',
        'wizard/cancel_appointment_wizard_view.xml',
        'data/patient_tags_data.xml',
        'data/patient_sequence_data.xml',
        'views/play_ground_view.xml',
        'data/appointment_sequence_data.xml'
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
