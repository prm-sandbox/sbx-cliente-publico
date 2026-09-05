from odoo import fields, models


class Cosa(models.Model):
    _name = 'prm.ensayo.cosa'
    _description = 'Cosa de ensayo'

    name = fields.Char()
