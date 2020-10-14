#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup


# 获取搜索首页文章的链接
def get_simple_article_html(soup):
    result = soup.find(name='h3', attrs={"class": "t c_font"})
    # -----<学术链接>----- #
    academic_href = result.find(name='a', attrs={"data-click": "{'button_tp':'title'}"}).get("href")
    academic_href = "https:" + academic_href
    return academic_href


# 获取搜索首页的底栏的页数
def get_pn(content):
    soup = BeautifulSoup(content, "html.parser")
    """<span class="pc">8</span>"""
    result = soup.findAll(name='span', attrs={"class": "pc"})
    page = result[-1].text.strip()
    return page


# 获取单个详情页的数据
def get_simple_content(url):
    print(url)
    # 如果这里出问题，则直接pass
