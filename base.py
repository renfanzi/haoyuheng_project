# ! -*- encoding:utf-8 -*-

import requests
import time


def common_request(url):
    # 要访问的目标页面
    # 代理服务器
    # 经典版
    # proxyHost = "http-cla.abuyun.com"
    # proxyPort = "9030"
    # 动态版
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    # 经典版
    # proxyUser = "H69C8B57A4B223RC"
    # proxyPass = "77373898A78DDA5B"
    # 动态版
    proxyUser = "H8854Q8YXR374GDD"
    proxyPass = "418F4696DB6B83B6"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }
    # print(proxyMeta)
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

    headers = {
        # 经典版
        # "Proxy-Authorization": "Basic SDY5QzhCNTdBNEIyMjNSQyUzQTc3MzczODk4QTc4RERBNUI=",
        # 动态版
        "Proxy-Authorization": "Basic SDg4NTRROFlYUjM3NEdERCUzQTQxOEY0Njk2REI2QjgzQjY=",
        'User-Agent': user_agent,
    }
    content = requests.get(url, proxies=proxies, headers=headers).text

    time.sleep(2)
    return content


if __name__ == '__main__':
    data = common_request("https://xueshu.baidu.com/s?&wd=飞行器空气动力学&pn=580&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&&sc_hit=1")
    print(data)
