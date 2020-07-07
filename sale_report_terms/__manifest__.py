{
    'name': 'Informe sales terminos',
    'version': '13.0.1',
    'summary': 'Agrega un apartado en compania para definir terminos del sales order',
    'description': 'Agrega un apartado en compania para definir terminos del sales order',
    'author': 'Xmarts',
    'website': 'www.xmarts.com',
    'depends': ['base','sale','product'],
    'data': [
        'views/res_company.xml',
        'views/product_template.xml',
        'reports/sale_report.xml',
    ],
    'installable': True,
}
