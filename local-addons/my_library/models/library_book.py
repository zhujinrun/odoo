from odoo import models,fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = '图书信息'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'

    name = fields.Char('书名', required=True)
    date_release = fields.Date('出版日期')
    author_ids = fields.Many2many('res.partner', string='作者')

    short_name = fields.Char('书名简称', required=True, 
                             translate=True, index=True)

    notes = fields.Text('备注')
    state = fields.Selection([('draft', '不可用'), ('available', '可用'), ('lost', '遗失') ], string='状态', 
                             default='draft')
    description = fields.Html('内容简介')
    cover = fields.Binary('封面')
    out_of_print = fields.Boolean('是否绝版')
    date_updated = fields.Datetime('更新时间')
    pages = fields.Integer('页数', 
                           groups='base.group_user',
                           states={'lost':[('readonly',True)]},
                           help='图书总页数')
    reader_rating = fields.Float('读者评分',digits=(14,4))
    cost_price = fields.Float('采购价格', digits='Book Price')

    currency_id = fields.Many2one('res.currency', string='货币类型')
    retail_price = fields.Monetary('零售价格', currency_field='currency_id')

    publisher_id = fields.Many2one('res.partner', string='出版社',
                                   # optional=True,
                                   ondelete='set null', # 'restrict', 'cascade'
                                   context={},
                                   domain=[])