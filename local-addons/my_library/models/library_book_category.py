from odoo import api, models,fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = '图书类别'

    # 层级支持
    _parent_stored = True
    _parent_name = 'parent_id' # optional if field is 'parent_id'
    parent_path = fields.Char('父节点路径', index=True)

    # 字段定义
    name = fields.Char('类别', required=True)
    parent_id = fields.Many2one('library.book.category', string='父类别', ondelete='restrict', index=True)
    child_ids = fields.One2many('library.book.category', 'parent_id', string='子类别')

    # 约束：防止循环引用
    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('错误！不允许循环引用')