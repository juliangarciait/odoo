# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    name = fields.Char('Titulo', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Activo?', default=True)
    date_published =fields.Date('Fecha de publicacion')
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='quien lo publica')
    author_ids = fields.Many2many('res.partner', string='autores')
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
