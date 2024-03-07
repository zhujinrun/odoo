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


## 2-7. 创建带有层次结构的模型

### 7.1 模型：图书类别：

library_book_category, 图书类别
* parent_id，父类别，Many2one('library.book.category', string='父类别')
* child_ids，子类别，One2many('library.book.category', 'parent_id', string='子类别')


### 7.2 层级支持和防止循环引用：

```python
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
```

### 7.3 访问权限设置：

| id | name | model_id:id | group_id:id | perm_read | perm_write | perm_create | perm_unlink |
|:--------|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:--------:|
| acl_book_category | library.book_category default | model_library_book_category |  | 1 | 0 | 0 | 0 |
| acl_book_category_librarian | library.book_category librarian | model_library_book_category | group_librarian | 1 | 1 | 1 | 1 |

### 7.4 模型添加字段：

* category_id，类别，Many2one('library.book.category', string='类别')

### 7.5 表单添加字段：

`<field name="category_id"/>`

### 7.6 升级应用：

设置图书的类别，添加类别/父类别


## 2-8. 模型添加数据约束

### 8.1 约束类型：

* 数据库约束：postgreSQL
* 服务端逻辑：python

### 8.2 添加数据库约束：

* 书名：唯一
* 页数：非负数

```python
    _sql_constraints = [
        ('name_uniq', 'unique (name)', '书名不能重复'),
        ('positive_pages', 'check (pages>0)', '页数必须大于0')
    ]
```

### 8.3 添加服务端约束：

* 出版日期：不能大于当前日期

```python
    @api.constrains('date_release')
    def _check_date_release(self):
        for record in self:
            if record.date_release and record.date_release > fields.Date.today():
                raise models.ValidationError('出版日期不能大于当前日期。')
```

### 8.4 升级应用：

验证约束生效结果


## 2-9. 模型添加计算字段

### 9.1 计算字段：

出版天数 = 当前日期 - 出版日期

### 9.2 模型添加字段：

* 字段定义

`release_days = fields.Integer('出版天数', compute='_compute_release_days', store=False, compute_sudo=True, help='出版时间距今天多少天')`

* 方法定义

```python
    @api.depends('date_release')
    def _compute_release_days(self):
        today = fields.Date.today()
        for record in self:
            if record.date_release:
                delta = today - record.date_release
                record.release_days = int(delta.days)
            else:
                record.release_days = 0
```

### 9.3 表单添加字段：

列表和表单添加“出版天数”字段

### 9.4 升级应用：

验证计算字段


## 2-10. 引用关联字段所在模型中的其他字段

### 10.1 关联字段：出版城市

关联字段：出版社 publisher_id
所在模型：res.partner
引用字段：city

### 10.2 模型添加字段：

属性：publisher_city，出版城市，Char(, related='publisher_id.city', readonly=True)

### 10.3 表单添加字段：

列表和表单添加“出版城市”字段

### 10.4 升级应用：

验证引用字段


## 2-11. 类继承：扩展现有模型

### 11.1 Odoo 中的三种继承：

* Class inheritance（extension）：类继承
* Prototype inheritance：原型继承
* Deltegation inheritance：委托继承

### 11.2 扩展模型：

属性：
* 所著书籍（authored_book_ids）
* 著作数量（authored_book_count）

```python

class ExtResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'

    authored_book_ids = fields.Many2many('library.book', string='著作')
    authored_book_count = fields.Integer('著作数量', compute='_compute_authored_book_count', store=False)

    @api.depends('authored_book_ids')
    def _compute_authored_book_count(self):
        for record in self:
            record.authored_book_count = len(record.authored_book_ids)
```

### 11.3 表单添加字段：

```xml
                    <notebook>
                        <page string="作者详情">
                            <field name="author_ids">
                                <tree>
                                    <field name="name"/>
                                    <field name="authored_book_count"/>
                                    <field name="authored_book_ids" widget="many2many_tags"/>
                                </tree>
                            </field>
                        </page>
                    </notebook>
```

### 11.4 升级应用：

验证扩展模型的属性