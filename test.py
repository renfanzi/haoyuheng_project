#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import time
import random


def common_request(url):
    ip_list = [
        "111.75.126.252:19914"
    ]

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {
        'User-Agent': user_agent,
    }
    ip = random.choice(ip_list)
    content = requests.get(url, headers=headers, proxies={'https': ip}).text
    # time.sleep(10)
    return content

if __name__ == '__main__':
    common_request("https://xueshu.baidu.com/s?&wd=飞行器空气动力学&pn=580&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&&sc_hit=1")