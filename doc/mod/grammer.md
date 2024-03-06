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