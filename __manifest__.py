
{
    'name': 'Hospital Management',
    'version': '11.0.1.0.0',
    'summary': 'Module for managing the Hospital',
    'description': '',
    'category': 'Extra Tools',
    'author': 'Tirop',
    'maintainer': 'Tirop',
    'website': 'tirop.com',
    'license': 'AGPL-3',
    'depends': [
                'sale',
                'base_setup',
                'mail',
                ],
    'data': [
              'data/sequence.xml',
              'security/security.xml',
              'security/ir.model.access.csv',
              'views/patient.xml',
              'views/doctor.xml',
              'views/appointment.xml',
              'reports/report.xml',

             ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [],
    }
}