#!/usr/bin/env python
# -*- coding:utf-8 -*-

from get_simple_crticlel import *
from base import common_request
from article_details_core import get_simple_content


# 合成url
def compose_url(search_content, pn):
    url_head = "https://xueshu.baidu.com/s?"
    wd = "wd={}".format(search_content)
    pn = "pn={}".format(pn)
    sc_other_year = "tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&"
    url_other = "sc_hit=1"
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
        # print(son_url)
        try:
            paper_id = son_url.split("=")[1].split("&")[0]
            # 这个地方需要增加查重功能, 如果数据库已经存在,则不再进行下面操作
            get_simple_content(paper_id)
        except Exception as e:
            continue
        pass


# 请求url的内容
def request_content(search_content, pn):
    url = compose_url(search_content, pn)
    print(url)
    content = common_request(url)
    # 获取页数代码
    page = get_pn(content)
    # print(page)
    if int(pn) > 100:
        if page == '8':
            return False
    # 获取每天数据的html代码
    get_html_code_mode(content)


if __name__ == '__main__':
    for i in range(0, 100):
        pn = str(i * 10)
        print(pn)
        status = request_content("飞行器空气动力学", pn)

