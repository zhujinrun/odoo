from odoo import api, models,fields

class ExtResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'

    authored_book_ids = fields.Many2many('library.book', string='著作')
    authored_book_count = fields.Integer('著作数量', compute='_compute_authored_book_count', store=False)

    @api.depends('authored_book_ids')
    def _compute_authored_book_count(self):
        for record in self:
            record.authored_book_count = len(record.authored_book_ids)