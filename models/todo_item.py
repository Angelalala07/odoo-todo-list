from odoo import models, fields

class TodoItem(models.Model):
    _name = 'todo.item'
    _description = 'Todo Item'

    todo_id = fields.Many2one('todo.list', string='Todo List')
    name = fields.Char(string='Item Name', required=True)
    description = fields.Char(string='Description')
    is_complete = fields.Boolean(string='Is Complete')
    todo_state = fields.Selection(
        related='todo_id.state',
        string='Todo State',
        store=False
    )