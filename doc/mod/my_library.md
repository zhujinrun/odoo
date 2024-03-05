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
