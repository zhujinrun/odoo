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

* notes: 备注，Text
* state: 状态，Selection
* description: 内容简介，Html
* cover: 封面，Binary
* out_of_print: 是否绝版，Boolean
* date_updated: 更新时间，Date
* pages: 页数，Integer
* reader_rating: 读者评分，Float

### 2.2 更新视图

form 中添加字段

### 2.3 升级应用

进入 form 页面确认添加的字段


## 2-3. 设置字段的属性

### 3.1 添加属性

* string：字段的显示名称
* required：是否必填
* translate：启用字段值的翻译
* index：是否为字段添加索引
* default：设置字段的默认值
* groups：限制字段只能被给定组用户访问
* states：值对列表的字典映射
* help：用户看到的字段的提示条
* invisible：字段是否可见。默认为False，即可见
* readonly：字段是否只读。默认为False，即可编辑
* store：字段是否存储到数据库，针对计算字段，默认值为False，其它字段默认为True

### 3.2 升级应用

确认属性设置后的效果


## 2-4. 运行时设置浮点数字段的精度

### 4.1 模型添加字段：

* cost_price，采购价格，Float(,digits='Book Price')

### 4.2 表单添加字段

`<field name="cost_price"/>`

### 4.3 升级应用

默认精度：2

### 4.4 运行时设置精度

* 成为超级用户
* 设置 -> 技术 -> 数据库结构 -> 小数准确性（Decimal Accuracy）
* 新建 -> 用途：Book Price -> 数字：0 -> 保存


## 2-5. 添加货币类型字段

### 5.1 模型添加字段：

* currency_id，货币类型，Many2one('res.currency', )
* retail_price，零售价格，Monetary(, currency_field='currency_id')

### 5.2 表单添加字段

```xml
    <field name="retail_price"/>
    <field name="currency_id"/>
```

### 5.3 升级应用

支持多货币设置


## 2-6. 添加关联字段

### 6.1 关联字段的种类：

* One2many：一对多
* Many2one：多对一
* Many2many：多对多

### 6.2 模型添加字段：

* publisher_id，出版社，Many2one('res.partner', string='出版社')

### 6.3 表单添加字段

出版社

### 6.4 升级应用

下拉列表选择出版社
