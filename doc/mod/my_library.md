## 2.创建一个新的 Odoo 模块（图书管理）

### 2.1 配置 addons 路径
```
mkdir local-addons 
```
### 2.2 生成模块文件

模块目录：

```
mkdir local-addons/my_library
```

模块文件：

* `__init__.py`：Python 模块，内容：空
* `__manifest__.py`：Odoo模块说明，内容：`{'name':'图书管理'}`

### 2.3 激活模块

启动 Odoo16：

```
python odoo-bin --addons-path=local-addons,addons,odoo/addons -d odoo16 -r odoo16 -w odoo16
```

### 2.4 安装模块

应用 -> 更新应用列表 -> 搜索 模块：`图书管理` -> 激活


## 3.完善模块说明文件：__manifest__.py

### 3.1 文件内容

```
{
    'name':'图书管理',
    'version':'0.1',
    'summary':'这是图书管理模块概要说明',
    'sequence': 1,
    'description': """
图书管理，这是模块详细说明。
===================================================   
    """,
    'author':'Zhujr',
    'category':'Uncategorized',
    'website':'https://space.bilibili.com/333462738',
    'depends':['base'],
    # 'data':['views/views.xml'],
    # 'demo':['demo.xml'],
}
```

### 3.2 应用图标

`static/description/icon.png`

### 3.3 升级模块

重启 Odoo16 -> 应用 -> 搜索 已安装 模块：`图书管理` -> 升级

### 3.4 激活开发者模式

设置 -> 一般设置 -> Developer Tools -> 激活开发者模式

查看模块详细说明


## 4.完善模块文件目录结构

### 4.1 目录结构

```
my_library
    __init__.py
    __manifest__.py
    controllers
        __init__.py
    models
        __init__.py
    views
    security
    static
    data
    demo
```


### 4.2 导入 python 模块

`__init__.py`：
```
from . import controllers
from . import models
```


## 5.创建一个模型（model）

### 5.1 LibraryBook（图书信息）

字段：
* name (书名)
* data_release (出版日期)
* author_ids (作者)

```
from odoo import models,fields

class library_book(models.Model):
    _name = 'library.book'
    _description = '图书信息'

    name = fields.Char('书名', required=True)
    date_release = fields.Date('出版日期')
    author_ids = fields.Many2many('res.partner', string='作者')
```

### 5.2 导入 python 模块

`models/__init__.py`：

```
from . import library_book
```

`my_library/__init__.py`：

```
from . import models
```

### 5.3 升级模块

重启 Odoo16 -> 应用 -> 搜索 已安装 模块：`图书管理` -> 升级

### 5.4 确认数据库表

* library_book
* library_book_res_partner_rel


## 6.添加菜单和视图（页面）

### 6.1 创建视图文件

文件：
`views/library_book_views.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Data records go here -->
</odoo>
```
添加到 manifest 文件：

```     
'application': True,
'data':['views/library_book_views.xml'],
```

### 6.2 创建动作（action）

```xml
    <record id="library_book_action" model="ir.actions.act_window">
        <field name="name">图书列表</field>
        <field name="res_model">library.book</field>
        <field name="view_mode">tree,form</field>
    </record>
```

### 6.3 创建菜单（menu）

```xml
    <menuitem id="library_base_menu" name="图书管理" />
    <menuitem id="library_book_menu" name="图书" parent="library_base_menu" action="library_book_action" />
```

### 6.4 升级应用

重启 Odoo16 -> 应用 -> 搜索 应用 已安装：`图书管理` -> 升级

菜单不显示，原因：尚未配置权限

### 6.5 超级用户身份运行

调试按钮 -> 成为超级用户

可查看菜单、进入操作页面，进行增、删、改、查操作。


## 7.自定义视图（页面）

### 7.1 列表视图

图书列表页面：
```
书名  |  出版日期
```
### 7.2 表单视图

图书详情/编辑页面：
```
书名  |  作者  |  出版日期
```

### 7.3 搜索视图

搜索栏：
* 查询：按书名或作者，进行模糊查询
* 筛选：只查看未设置作者的书籍


### 7.4 升级应用

重启 Odoo16 -> 应用 -> 搜索 应用 已安装：`图书管理` -> 升级

切换超级用户身份，确认页面效果。


## 8.访问控制（表级）

### 8.1 权限概述

* 表级：用户组
* 记录级：规则-domain
* 字段级：字段定义参数-groups

### 8.2 创建用户组（图书管理员）

* 普通用户组：user1, 只能查看书籍信息

* 图书管理员组：user2，可以查看和维护书籍信息

文件：`security/library_book_security.xml`:

```xml
    <record id="group_librarian" model="res.groups">
        <field name="name">图书管理员</field>
        <field name="comment">拥有图书查看和维护的权限。</field>
        <!-- 
            将管理员用户（admin）和 超级用户（root）添加到该用户组：
            base.user_root：odoo中的超级用户，在系统中具有最高级别的权限。通常用于系统的初始化和特殊的管理任务，具有对系统中所有对象和功能的完全访问权限，而不受用户组的权限限制。
            base.user_admin：odoo中的管理员用户，具有系统管理权限，例如安装/卸载模块、配置用户权限、管理数据库等。但这个用户受用户组的权限限制。
        -->
        <field name="users" eval="[(4, ref('base.user_root')), (4, ref('base.user_admin'))]"/>
    </record>
```


### 8.3 添加访问控制

文件：`security/ir.model.access.csv`:

### 8.4 更新 manifest 文件

将 `library_book_security.xml` 和 `ir.model.access.csv` 添加到 `data` 属性中。注意：如果您不遵守安全文件的顺序，则必须在`__manifest__.py`中将与安全相关的`.xml`文件放在`·.csv`文件之前

### 8.5 升级应用

重启 Odoo16 -> 应用 -> 搜索 应用 已安装：`图书管理` -> 升级

* 创建2个用户：user1,user2
* 将 user2 设置为图书管理员组成员

确认：
* user1 只能查看书籍信息
* user2 和 admin 可以查看和维护书籍信息