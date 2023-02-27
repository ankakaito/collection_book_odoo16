from odoo import fields, models, api, _

class ListBook(models.Model):
    _name = 'list.book'
    _description = ' List Book '

    name = fields.Char(string="Book Title")
    category_ids = fields.Many2one('category'," Category ")
    launcing_date = fields.Date(string="Launcing Date")
    isbn_code = fields.Char(string="ISBN Code")
    writer_ids = fields.Many2many("master.writer", "list_book_writer_rel", "list_book_id", "writer_id",string=" Writer ")
    image = fields.Binary(string="Book Image")
