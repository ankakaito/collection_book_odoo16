from odoo import fields, models, api, _

class Writer(models.Model):
    _name = 'master.writer'
    _description = ' Master Writer '

    name = fields.Char(string="Writer Name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    city = fields.Char(string="City")
    country = fields.Char(string="Country")
   # book_writed = fields.Many2one("list.book", "Book Writed")
    book_count = fields.Integer(string='Book Count', compute='_compute_book_count')
   #book_writed = fields.Integer(string="Book Writed", compute='book_writed')

    def _compute_book_count(self):
        for rec in self:
            book_count = self.env['list.book'].search_count([('writer_ids', '=',rec.id)])
            rec.book_count = book_count

    def book_count_button_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'List Book',
            'res_model': 'list.book',
            'domain': [('writer_ids','=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
