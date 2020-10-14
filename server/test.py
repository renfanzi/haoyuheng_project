#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

def compose_url():
    url_head = "https://xueshu.baidu.com/s?"
    wd = "wd={}".format("空气动力学")
    pn = "pn={}".format("0")
    sc_other_year = "tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&filter=sc_year={%s,+}" % "2020"
    url_other = "sc_f_para=sc_tasktype={firstSimpleSearch}&bcp=2&sc_hit=1"
    url = "&".join([url_head, wd, pn, sc_other_year, url_other])
    print(url)
    # print(requests.get(url, verify=False).text)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    print(requests.get(url,headers=headers).text)

if __name__ == '__main__':
    compose_url()
