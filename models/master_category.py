
from odoo import fields, models, api, _

class MasterCategory(models.Model):
    _name = 'category'
    _description = ' Book Category '

    name = fields.Char(string="Category")
    desc = fields.Char(string="Description")
