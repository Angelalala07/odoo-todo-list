from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'
    _order = 'priority desc, name asc'

    name = fields.Char(string='Title', required=True)
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
    ], string='Priority', default='0', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete'),
    ], string='Status', default='draft')
    item_ids = fields.One2many('todo.item', 'todo_id', string='Todo Items')
    attendee_ids = fields.One2many('todo.attendee', 'todo_id', string='Attendees')
    all_items_complete = fields.Boolean(
        compute='_compute_all_items_complete',
        store=True
    )

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                if rec.end_date <= rec.start_date:
                    raise ValidationError('End Date must be later than Start Date.')

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date:
            if self.end_date <= self.start_date:
                self.end_date = False
                return {
                    'warning': {
                        'title': 'Invalid Date',
                        'message': 'End Date cleared because it was earlier than Start Date.',
                        'type': 'notification',
                    }
                }
    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.start_date and self.end_date:
            if self.end_date <= self.start_date:
                self.end_date = False
                return {
                    'warning': {
                        'title': 'Invalid End Date',
                        'message': 'End Date must be later than Start Date.',
                        'type': 'notification',
                    }
                }
    def action_start(self):
        self.state = 'in_progress'

    def action_complete(self):
        self.state = 'complete'

    @api.depends('item_ids.is_complete', 'item_ids')
    def _compute_all_items_complete(self):
        for rec in self:
            if rec.item_ids:
                rec.all_items_complete = all(rec.item_ids.mapped('is_complete'))
            else:
                rec.all_items_complete = False


class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color')


class TodoAttendee(models.Model):
    _name = 'todo.attendee'
    _description = 'Todo Attendee'

    todo_id = fields.Many2one('todo.list', string='Todo List')
    user_id = fields.Many2one('res.users', string='User Name')