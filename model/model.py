#!/usr/bin/env python
# -*- coding:utf-8 -*-


from peewee import MySQLDatabase, Model
from peewee import PrimaryKeyField, IntegerField, CharField, FloatField, DoubleField, DecimalField
import time
import datetime


def get_str_time(strftime='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.now().strftime(strftime)


def get_now_time():
    return int(time.time())


#
# db = MySQLDatabase("haoyuheng",
#                    user="root",
#                    password="redhat",
#                    host="127.0.0.1",
#                    port=3306)

db = MySQLDatabase("xueshu",
                   user="root",
                   password="xkpt2020",
                   host="39.106.92.143",
                   port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class XueShuPaper(BaseModel):
    id = PrimaryKeyField()
    technology_crawler_keyword = CharField()
    article_paperid = CharField()
    article_title = CharField()
    article_abstract = CharField()
    article_keyword = CharField()
    article_doi = CharField()
    article_sc_cited = CharField()
    article_year = CharField()
    article_journal_title = CharField()
    article_dl_list = CharField()
    article_sc_search = CharField()

    article_createtime = IntegerField(default=get_now_time())
    article_createdatetime = CharField(default=get_str_time())

    class Meta:
        order_by = ('id',)
        db_table = 'xueshu_paper'


class XueShuAuthors(BaseModel):
    id = PrimaryKeyField()
    xueshu_paper_id = IntegerField()
    author_name = CharField()
    author_organization = CharField()
    author_url = CharField()

    author_createtime = IntegerField(default=get_now_time())
    author_createdatetime = CharField(default=get_str_time())

    class Meta:
        order_by = ('id',)
        db_table = 'xueshu_authors'


class XueshuSimilarReferences(BaseModel):
    id = PrimaryKeyField()
    xueshu_paper_id = IntegerField()
    sc_type = IntegerField()
    sc_pdf_read = CharField()
    sc_research = CharField()
    sc_abstract = CharField()
    sc_keyword = CharField()
    sc_year = CharField()
    sc_title = CharField()
    url = CharField()
    sc_scholarurl = CharField()
    sc_author = CharField()

    sc_createtime = IntegerField(default=get_now_time())
    sc_createdatetime = CharField(default=get_str_time())

    class Meta:
        order_by = ('id',)
        db_table = 'xueshu_similar_references'


class ErrorSearch(BaseModel):
    paper_id = CharField()
    search_content = CharField()

    class Meta:
        db_table = 'error_search'


if __name__ == '__main__':
    a = XueShuPaper.get_or_none(XueShuPaper.article_paperid == '1x7q0ta0ab1y08s0f7140e80j2533927')
    print(a)
