from odoo import api, models,fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}
    _description = '会员'

    partner_id = fields.Many2one('res.partner', string='联系人', ondelete='cascade', required=True)
    date_start = fields.Date('加入时间', required=True)
    date_end = fields.Date('到期时间')
    member_number = fields.Char('会员编号', required=True, index=True)
    date_of_birth = fields.Date('出生日期')