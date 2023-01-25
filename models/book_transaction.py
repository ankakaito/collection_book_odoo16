from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class BookTransactionLine(models.Model):
    _name = 'book.transaction.line'
    _description = 'Book Transaction Line'

    management_id = fields.Many2one('book.management','Serial Number')
    transaction_id = fields.Many2one('book.transaction', 'Transaction ID')
    book_title = fields.Char('Book Title')
    qty = fields.Integer(string='Qty')

    @api.constrains('qty')
    def check_val_qty(self):
        for rec in self:
            if rec.qty < 0:
                raise ValidationError('Qty Input must more or less then 0')

    @api.constrains('qty')
    def check_qty(self):
        for rec in self:
            check = self.env['book.management'].search([('book_qty', '<', rec.qty)])
            if check:
                raise ValidationError(_("Qty Borrowed cannot more than Amount Stok The Book"))

    @api.onchange('management_id')
    def onchange_management_id(self):
        for rec in self:
            if rec.management_id:
                #rec.qty = rec.management_id.amount_borrowed
                rec.book_title = rec.management_id.book_id.name



class BookTransaction(models.Model):
    _name = 'book.transaction'
    _description = 'Book Transaction'

    name = fields.Char(string="Transaction Number", default='New')
    member_id = fields.Many2one('member',"Member Name")
    borrowing_date = fields.Date(string="Borrowing Date", default=fields.Date.today())
    returning_date= fields.Datetime(string="Returning Date")
    transaction_ids = fields.One2many('book.transaction.line','transaction_id',"List Book Management")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'seq.book.transaction') or 'New'
        result = super(BookTransaction, self).create(vals)
        return result

