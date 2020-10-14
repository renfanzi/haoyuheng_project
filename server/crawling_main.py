#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from server.get_simple_crticlel import *


# 合成url
def compose_url(search_content, pn, year):
    url_head = "https://xueshu.baidu.com/s?"
    wd = "wd={}".format(search_content)
    pn = "pn={}".format(pn)
    sc_other_year = "tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_year={%s,+}" % year
    url_other = "sc_f_para=sc_tasktype={firstSimpleSearch}&bcp=2&sc_hit=1"
    url = "&".join([url_head, wd, pn, sc_other_year, url_other])
    return url


# 获取html代码里面需要的模块代码
def get_html_code_mode(content):
    soup = BeautifulSoup(content, "html.parser")
    result = soup.findAll(name='div', attrs={"class": "result sc_default_result xpath-log"})
    # 拿到每页的数据，list为每条数据的url
    pn_academic_url_list = []
    for i in result:
        # 这里出问题，也直接pass
        academic_href = get_simple_article_html(i)
        pn_academic_url_list.append(academic_href)
    # print(pn_academic_url_list)
    for son_url in pn_academic_url_list:
        get_simple_content(son_url)


# 请求url的内容
def request_content(search_content, pn, year):
    url = compose_url(search_content, pn, year)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {
        'User-Agent': user_agent,
    }
    content = requests.get(url, headers=headers).text
    # 获取页数代码
    page = get_pn(content)
    if int(pn) > 100:
        if page != '8':
            return False
    # 获取每天数据的html代码
    get_html_code_mode(content)


if __name__ == '__main__':
    request_content("飞行器空气动力学", '0', '2020')
