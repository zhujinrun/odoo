## 2-1. 定义模型的全局属性

```python
from odoo import models,fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = '图书信息'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'

    name = fields.Char('书名', required=True)
    date_release = fields.Date('出版日期')
    author_ids = fields.Many2many('res.partner', string='作者')

    short_name = fields.Char('书名简称', required=False)
```

### 1.1 模型名称：_name

### 1.2 显示名称：_description

### 1.3 默认排序字段：_order

### 1.4 记录的代表/标题字段：_rec_name

用于：
* 面包屑菜单的标题
* 关联表引用，选择关联记录时下拉列表的显示

### 1.5 升级应用

* 查看显示名称：
    设置 -> 技术 -> 数据库结构 -> 模型

* 列表页面确认排序


## 2-2. 在模型中添加字段

```python
    notes = fields.Text('备注')
    state = fields.Selection([('draft', '不可用'), ('available', '可用'), ('lost', '遗失') ], string='状态')
    description = fields.Html('内容简介')
    cover = fields.Binary('封面')
    out_of_print = fields.Boolean('是否绝版')
    date_updated = fields.Datetime('更新时间')
    pages = fields.Integer('页数')
    reader_rating = fields.Float('读者评分',digits=(14,4))
```

### 2.1 字段与类型

notes: 备注，Text
state: 状态，Selection
description: 内容简介，Html
cover: 封面，Binary
out_of_print: 是否绝版，Boolean
date_updated: 更新时间，Date
pages: 页数，Integer
reader_rating: 读者评分，Float

### 2.2 更新视图

form 中添加字段

### 2.3 升级应用

进入 form 页面确认添加的字段