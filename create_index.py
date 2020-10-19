#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pymysql, os, configparser
from whoosh.index import create_in
from jieba.analyse import ChineseAnalyzer
from decimal import Decimal
from whoosh.fields import Schema, TEXT, ID
from hyh.add_index import incremental_index

analyzer = ChineseAnalyzer()

"""
    创建索引文件系统
"""


def CreateIndexFilesPattern(indexname, schema, indexdir, columnName, uniqueValue):
    """
        注意， 如果更新数据，在创建和添加的时候， 某个字段必须唯一， 才OK， 同是在更新的时候， 也要有那个唯一字段
        :param columnName: 是给Schema用的， 数据是数据库的字段， 只是列的字段名
        :param indexname: 这里的indexname  ==》 当分类搜索的时候就是根据这个indexname来的, 通常用库名， 但不能有下划线等字符
        :param schema: # 初始空字符， 然后进来拼接
        :param indexdir: 索引目录
        :return:
        """
    # keys = {"ID": "abc", "content": "撸啊撸啊德玛西亚"}  # 表示从数据库得到的模拟数据

    """
        # ID(stored=True, unique=True)
        unique:  的作用表示唯一值， 由于update的原因， 所以这里某个值要求唯一，否则将会出现两条数据 
    """
    s = "Schema("
    for key in columnName:
        if key == uniqueValue:
            s += key.replace('\n', '').replace('/r', '').replace('\t', '').replace(' ',
                                                                                   '') + '=ID(stored=True, unique=True), '
        else:
            s += key.replace('\n', '').replace('/r', '').replace('\t', '').replace(' ',
                                                                                   '') + '=TEXT(stored=True, analyzer=analyzer), '
            # TEXT(stored=True, analyzer=analyzer) 其实就是结合分词了

    s = s.rstrip(", ")
    s += ")"
    # print(s) # Schema(ID=TEXT(stored=True, analyzer=analyzer), content=TEXT(stored=True, analyzer=analyzer))
    schema = eval(s)
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)

    create_in(indexdir, schema=schema, indexname=indexname)  # from whoosh.index import create_in 创建索引文件


def escape(s, obj="’"):
    ret = ''
    for x in s:
        if x == obj:
            ret += '\\'
        ret += x
    return ret


def app():
    """
        获取一个表的每个字段

    """
    indexDirectory = ''
    dbname = ''
    uniqueValue = ['']
    # 字段名
    columnName = []

    if not os.path.exists(indexDirectory):
        os.makedirs(indexDirectory)

    # 创建索引
    CreateIndexFilesPattern(indexname=dbname, schema="", indexdir=indexDirectory, columnName=columnName,
                            uniqueValue=uniqueValue)
    # 写入数据
    data = []
    for rowData in data:
        incremental_index(indexdir=indexDirectory, indexname=dbname, rowData=rowData)


if __name__ == '__main__':
    app()
