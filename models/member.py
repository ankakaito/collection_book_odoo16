from odoo import fields, models, api, _

class Member(models.Model):
    _name = 'member'
    _description = ' Member '

    def func_to_approve(self):
        if self.state == 'draft':
                self.state = 'aproved'

    name = fields.Char(string="Member Name")
    no_id = fields.Char(string="Number ID")
    card_type = fields.Selection([
        ('KTP', 'KTP'),
        ('SIM', 'SIM'),
        ('passport', 'Passport'),
        ], 'KTP', default='KTP')    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('aproved', 'Aproved'),
        ], 'State', default='draft')    
