#!/usr/bin/env python
# -*- coding:utf-8 -*-

from get_simple_crticlel import *
from base import common_request
from article_details_core import get_simple_content
from model.model import XueShuPaper, ErrorSearch


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
def get_html_code_mode(content, search_content):
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
        paper_id = son_url.split("=")[1].split("&")[0]
        # 这个地方需要增加查重功能, 如果数据库已经存在,则不再进行下面操作
        # if not XueShuPaper.get_or_none(XueShuPaper.article_paperid == paper_id):
        #     get_simple_content(paper_id, search_content)
        try:
            paper_id = son_url.split("=")[1].split("&")[0]
            # 这个地方需要增加查重功能, 如果数据库已经存在,则不再进行下面操作
            if not XueShuPaper.get_or_none(XueShuPaper.article_paperid == paper_id):
                get_simple_content(paper_id, search_content)
        except Exception as e:
            ErrorSearch.insert(**{
                "paper_id": paper_id,
                "search_content": search_content
            }).execute()
            continue


# 请求url的内容
def request_content(search_content, pn):
    url = compose_url(search_content, pn)
    print(url)
    content = common_request(url)
    # print(content)
    # 获取页数代码
    # page = get_pn(content)
    # # print(page)
    # if int(pn) > 100:
    #     if page == '8':
    #         return False
    # 获取每天数据的html代码
    get_html_code_mode(content, search_content)


if __name__ == '__main__':
    a = ['空气动力学', '气动热力学', '航天动力学', '航天器轨道动力学', '航天器姿态动力学', '航天器再入动力学', '火箭动力学',
         '空间环境',
         '太空物理学', '太空化学', '太空气象学', '卫星网络技术', '星间链路技术', '网络体系结构技术', '信息发射传输技术', '信息处理技术', '卫星编队飞行技术', '分布式卫星技术',
         '航天器总体技术',
         '总体设计技术', '总装技术', '综合测试技术', '环境试验技术', '航天器有效载荷技术', '信息获取和处理类有效载荷', '信息存储和传输类有效载荷', '信息基准类有效载荷', '物质和能量传输类',
         '物质存储和处理类有效载荷', '航天器平台技术', '结构与机构技术', '热控制技术', '电源技术', '姿态与轨道控制技术', '推进技术', '测控与数据管理技术', '航天器环境工程技术',
         '空间环境模拟技术及模拟设备技术', '环境获取及环境分析技术', '环境效应机理及其防护技术', '环境试验及评价技术', '航天器运行控制技术', '总体与综合应用技术', '卫星侦察与监视技术',
         '卫星成像侦察技术',
         '卫星电子侦察技术', '卫星预警技术', '卫星通信技术', '卫星星载设备技术', '卫星通信多址与分配技术', '卫星通信信号传输技术', '卫星通信地球站技术', '卫星移动通信技术', '卫星固定通信技术',
         '卫星数据中继技术', '卫星广播和信息分发技术', '卫星激光通信技术', '卫星导航定位技术', '多普勒测速的导航定位技术', '有源测距和无源测距的导航定位技术', '卫星环境探测技术', '空间环境探测技术',
         '海洋环境探测技术', '大气环境探测技术', '卫星测绘技术', '测绘卫星技术', '三维重建技术', '卫星重力场测量技术', '地面跟踪卫星测量技术', '卫星跟踪卫星测量技术', '卫星重力梯度测量技术',
         '卫星搜救与救援技术', '在轨服务技术', '空间交会技术', '停靠与对接技术', '航天员舱外活动技术', '空间机器人技术', '空间遥操作技术', '空间加注技术', '释放与回收技术', '补给航天器技术',
         '可组装航天器技术', '空间可更换单元技术', '载人航天技术', '载人航天器技术', '运载火箭技术', '航天医学工程技术', '着陆场技术', '1航天对抗技术', '航天电子侦察', '航天电子攻击',
         '航天电子防御', '1空间态势感知', '空间情报搜集', '空间目标监视', '空间目标侦察', '空间环境监测', '航天制造技术', '飞行器制造技术', '发动机制造技术', '机载设备制造技术',
         '超精密加工技术',
         '高速加工技术', '数字化制造技术', '航天材料技术', '结构材料', '功能材料', '航天运载器技术', '总体设计技术', '制导和控制技术', '结构设计与制造技术', '可靠性设计技术',
         '计划管理技术',
         '试验技术', '航天发射技术', '测试技术', '加注技术', '瞄准技术', '临射检查及发射技术', '指挥控制技术', '地面勤务与保障技术', '紧急故障与逃逸救生技术', '航天测控技术', '遥测技术',
         '遥控技术', '跟踪测量技术']

    b = ['气动热力学', '航天动力学', '航天器轨道动力学', '航天器姿态动力学']
    for j in b:
        for i in range(0, 70):
            pn = str(i * 10)
            print(pn)
            status = request_content(j, pn)
