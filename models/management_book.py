from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class BookManagement(models.Model):
    _name = 'book.management'
    _description = 'Book Management'

    name = fields.Char(string="Serial Number")
    rack_code = fields.Char(string="Rack Code")
    book_id = fields.Many2one("list.book","Book Title")
    book_qty = fields.Integer(string="Qty")
    amount_borrowed = fields.Integer('Amount Borrowed')
    #trans_ids = fields.One2many('book.transaction.line','transaction_id','Transaction Number')
    #borrowing_count = fields.Integer(sring='Borrowing Count', compute='_computer_borrowing_count')

    @api.constrains('name')
    def check_serial(self):
        for rec in self:
            check = self.env['book.management'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if check:
                raise ValidationError(_("Cannot Duplicate %s As Serial Number" % rec.name))

    @api.constrains('book_qty')
    def check_qty(self):
        for rec in self:
            if rec.book_qty < 0:
                raise ValidationError('Qty Input must more then  0')


