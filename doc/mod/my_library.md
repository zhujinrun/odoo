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
* library_book——res_partner_rel
