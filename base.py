#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import time


def common_request(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    headers = {
        'User-Agent': user_agent,
    }
    content = requests.get(url, headers=headers).text
    # time.sleep(10)
    return content