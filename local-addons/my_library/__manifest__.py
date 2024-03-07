# -*- coding: utf-8 -*-
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
    'application': True,
    'data':[
        'security/library_book_security.xml',
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_member_views.xml'
     ],
    # 'demo':['demo.xml'],
}