{
    'name': 'Todo List',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Manage your Todo Lists',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'data/todo_tags.xml',
        'views/todo_list_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'todo_list/static/src/css/todo_list.css',
        ],
    },
    'installable': True,
    'application': True,
}