from odoo import fields, models, api, _

class Member(models.Model):
    _name = 'member'
    _description = ' Member '

    name = fields.Char(string="Member Name")
    no_id = fields.Char(string="Number ID")
    card_type = fields.Selection([
        ('KTP', 'KTP'),
        ('SIM', 'SIM'),
        ('passport', 'Passport'),
        ], 'KTP', default='Draft')    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('aproved', 'Aproved'),
        ], 'State', default='Draft')    
