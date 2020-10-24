#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib import parse
from base import common_request
from model.model import *


# 获取相似文献
def get_related(search_releated):
    related_url = "https://xueshu.baidu.com/usercenter/paper/search?wd=%s&type=related&rn=10&page_no=1" % search_releated
    related_data = json.loads(common_request(related_url), encoding="utf-8")
    # print(related_data)
    data = related_data["data"]
    data_papers = data["papers"]
    data_list = []
    for data_paper in data_papers:
        meta_di_info = data_paper.get("meta_di_info", '')
        if meta_di_info:
            # 这里获取详细信息
            # pdf链接
            sc_pdf_read = meta_di_info.get("sc_pdf_read", '')
            # 关键词
            sc_research = meta_di_info.get("sc_research", '')
            # 摘要
            sc_abstract = meta_di_info.get("sc_abstract", '')
            # 关键词
            sc_keyword = meta_di_info.get("sc_keyword", '')
            # 年份
            sc_year = meta_di_info.get("sc_year", '')
            # 标题
            sc_title = meta_di_info.get("sc_title", '')
            # 链接
            url = meta_di_info.get("url", '')
            # scholar url
            sc_scholarurl = meta_di_info.get("sc_scholarurl", '')
            # 作者
            sc_author = meta_di_info.get("sc_author", '')
            if sc_author:
                sc_author_list = []
                for i in sc_author:
                    """
                    {
                        'sc_affiliate': ['中国\x01空气\x01动力\x01研究\x01与\x01发展\x01中心\x01'],
                        'sc_affiliate_uri': ['160926617fd31c80'],
                        'sc_author_uri': ['96fa2eb23d1d50d8'],
                        'sc_label': ['1'],
                        'sc_name': ['朱国林', '朱国林']
                    }
                    """
                    try:
                        sc_author_data = {
                            "sc_name": i["sc_name"][0] if isinstance(i["sc_name"], list) else i["sc_name"],
                            'sc_affiliate_uri': i.get("sc_affiliate_uri", ''),
                            'sc_author_uri': i.get("sc_author_uri", ''),
                            'sc_label': i.get("sc_label", ''),
                            "sc_affiliate": i["sc_affiliate"][0].replace("\x01", '') if isinstance(i["sc_affiliate"],
                                                                                                   list) else i[
                                "sc_affiliate"],
                        }
                        sc_author_list.append(sc_author_data)
                    except Exception as e:
                        continue
            else:
                sc_author_list = []
            data_list.append({
                "sc_pdf_read": sc_pdf_read,
                "sc_research": sc_research,
                "sc_abstract": sc_abstract,
                "sc_keyword": sc_keyword,
                "sc_year": sc_year,
                "sc_title": sc_title,
                "url": url,
                "sc_scholarurl": sc_scholarurl,
                "sc_author": sc_author_list,
            })
    # print(data_list)
    return data_list


# 获取参考文献
def get_reference(search_reference):
    """
    result = {
        'msg': '操作成功',
        'status': 0,
        'data': {
            'curr_page_num': 0,
            'page_no': 1,
            'total_page_num': 2,
            'papers': [
                {'meta_di_info': {}},
                {'meta_di_info': {}},
                {'meta_di_info': {}},
            ]
        }
	}
    """
    reference_url = "https://xueshu.baidu.com/usercenter/paper/search?wd=citepaperuri:(%s)&type=reference&rn=10&page_no=1" % search_reference
    reference_data = json.loads(common_request(reference_url), encoding="utf-8")
    # print(reference_data)
    data = reference_data["data"]
    data_papers = data.get("papers", '')
    if data_papers:
        data_list = []
        for data_paper in data_papers:
            meta_di_info = data_paper.get("meta_di_info", '')
            if meta_di_info:
                # 这里获取详细信息
                # pdf链接
                sc_pdf_read = meta_di_info.get("sc_pdf_read", '')
                # 关键词
                sc_research = meta_di_info.get("sc_research", '')
                # 摘要
                sc_abstract = meta_di_info.get("sc_abstract", '')
                # 关键词
                sc_keyword = meta_di_info.get("sc_keyword", '')
                # 年份
                sc_year = meta_di_info.get("sc_year", '')
                # 标题
                sc_title = meta_di_info.get("sc_title", '')
                # 链接
                url = meta_di_info.get("url", '')
                # scholar url
                sc_scholarurl = meta_di_info.get("sc_scholarurl", '')
                # 作者
                sc_author = meta_di_info.get("sc_author", '')

                if sc_author:
                    sc_author_list = []
                    for i in sc_author:
                        """
                        {
                            'sc_affiliate': ['中国\x01空气\x01动力\x01研究\x01与\x01发展\x01中心\x01'],
                            'sc_affiliate_uri': ['160926617fd31c80'],
                            'sc_author_uri': ['96fa2eb23d1d50d8'],
                            'sc_label': ['1'],
                            'sc_name': ['朱国林', '朱国林']
                        }
                        """
                        try:
                            sc_author_data = {
                                "sc_name": i["sc_name"][0] if isinstance(i["sc_name"], list) else i["sc_name"],
                                'sc_affiliate_uri': i.get("sc_affiliate_uri", ''),
                                'sc_author_uri': i.get("sc_author_uri", ''),
                                'sc_label': i.get("sc_label", ''),
                                "sc_affiliate": i["sc_affiliate"][0].replace("\x01", '') if isinstance(
                                    i["sc_affiliate"], list) else i["sc_affiliate"],
                            }
                            sc_author_list.append(sc_author_data)
                        except Exception as e:
                            continue
                else:
                    sc_author_list = []

                data_list.append({
                    "sc_pdf_read": sc_pdf_read,
                    "sc_research": sc_research,
                    "sc_abstract": sc_abstract,
                    "sc_keyword": sc_keyword,
                    "sc_year": sc_year,
                    "sc_title": sc_title,
                    "url": url,
                    "sc_scholarurl": sc_scholarurl,
                    "sc_author": sc_author_list,
                })
        # print(data_list)
        return data_list
    else:
        return []


# 获取单个详情页的数据
def get_simple_content(article_id, search_content):
    # 7e5d6765e44e4aba2bcb2b87dc0830bb
    simple_html_url = "https://xueshu.baidu.com/usercenter/paper/show?paperid=%s&site=xueshu_se" % article_id
    # print(simple_html_url)
    simple_html = common_request(simple_html_url)
    # print(simple_html)
    soup = BeautifulSoup(simple_html, "html.parser")
    # title : 标题（汽车空气动力学数值仿真研究进展）
    try:
        article_title = soup.find(name='a',
                                  attrs={"data-click": "{'act_block':'main','button_tp':'title'}"}).text.strip()
    except Exception as e:
        try:
            article_title_div = soup.find(name='div', attrs={"class": "main-info"})
            article_title_h3 = article_title_div.find(name="h3")
            article_title = article_title_h3.find("a").text.strip()
        except Exception as e:
            article_title_div = soup.find(name='div', attrs={"class": "main-info"})
            article_title_h3 = article_title_div.find(name="h3")
            article_title = article_title_h3.find("span").text.strip()

    # print("标题：", article_title)
    # authors: 作者
    try:
        authors_soup_p = soup.find(name='p', attrs={"class": "author_text"})
        authors_a = authors_soup_p.find_all(name='a')
        # 获取作者链接
        # 获取作者名字
        authors_list = []
        for author_simple in authors_a:
            # 作者链接
            author_url = author_simple.get("href")
            # 作者姓名
            author_name = author_simple.text
            query = urlparse(author_url)[4]
            wd = parse.unquote(query)  # 解码字符串
            author_organization = wd.split("&")[0].split("=")[1]

            # 两种情况
            # 1. author:(张扬军) 清华大学&
            # 2. author:(张晋平) &
            if len(author_organization.split(' ')) > 1:
                author_organization = author_organization.split(' ')[1]
            else:
                author_organization = ''
            author_sub_data = {
                "author_name": author_name,
                "author_organization": author_organization,
                "author_url": author_url,
            }
            if author_sub_data not in authors_list:
                authors_list.append(author_sub_data)
    except Exception as e:
        authors_list = ''
    # print("作者：", authors_list)
    # 摘要
    try:
        article_abstract = soup.find(name='p', attrs={"class": "abstract"}).text.strip()
    except Exception as e:
        article_abstract = ''
    # print("摘要：", article_abstract)
    # 关键字
    try:
        keyword_soup_p = soup.find(name='p', attrs={"data-click": "{'button_tp':'keyword'}"})
        keyword_a = keyword_soup_p.find_all(name='a')
        keyword = [i.text.strip() for i in keyword_a]
    except Exception as e:
        keyword = ''
    # print("关键字：", keyword)
    # DOI
    try:
        DOI = soup.find(name='p', attrs={"data-click": "{'button_tp':'doi'}"}).text.strip()
    except Exception as e:
        DOI = ''
    # print("DOI:", DOI)
    # 被引用量
    # {'button_tp':'sc_cited'}
    try:
        sc_cited = soup.find(name='a', attrs={"data-click": "{'button_tp':'sc_cited'}"}).text.strip()
    except Exception as e:
        sc_cited = 0
    # print("被引用量：", sc_cited)
    # 年份
    try:
        year = soup.find(name='p', attrs={"data-click": "{'button_tp':'year'}"}).text.strip()
    except Exception as e:
        year = 0
    # print("年份：", year)
    # 来源期刊
    try:
        journal_title = soup.find(name='a', attrs={"data-click": "{'button_tp':'journal_title'}"}).text.strip()
    except Exception as e:
        journal_title = 0
    # print("来源期刊：", journal_title)
    # 全部来源
    try:
        dl_item_span = soup.find_all(name='span', attrs={"class": "dl_item_span"})
        dl_list = []
        # 获取链接
        for i in dl_item_span:
            try:
                dl_item_href = i.find(name="a", attrs={"class": "dl_item"}).get("href")
                dl_item_title = i.find(name="span", attrs={"class": "dl_source"}).get("title")
                son_dl = {
                    "dl_item_title": dl_item_title,
                    "dl_item_href": dl_item_href
                }
                if son_dl not in dl_list:
                    dl_list.append(son_dl)
            except Exception as e:
                continue
    except Exception as e:
        dl_list = []
    # print("全部来源:", dl_list)

    # 研究点分析
    try:
        sc_search_soup = soup.find_all(name='a', attrs={"data-click": "{'button_tp':'sc_search'}"})
        sc_search = [i.get("title") for i in sc_search_soup]
    except Exception as e:
        sc_search = ''
    # print("研究点分析：", sc_search)

    # 相似文献
    try:
        related_data = get_related(article_title)
    except Exception as e:
        related_data = ''
    # print("相似文献：", related_data)

    # 参考文献
    try:
        reference_data = get_reference(article_id)
    except Exception as e:
        reference_data = ''
    # print("参考文献：", reference_data)

    # 数据库数据
    xueshupaper_data = {
        "technology_crawler_keyword": search_content,
        "article_paperid": article_id,
        "article_title": article_title,
        "article_abstract": article_abstract,
        "article_keyword": json.dumps(keyword, ensure_ascii=False),
        "article_doi": DOI,
        "article_sc_cited": sc_cited,
        "article_year": year,
        "article_journal_title": journal_title,
        "article_dl_list": json.dumps(dl_list, ensure_ascii=False),
        "article_sc_search": json.dumps(sc_search, ensure_ascii=False),
    }
    XueShuPaperID = XueShuPaper.insert(**xueshupaper_data).execute()

    xueshuauthors_data = []
    for i in authors_list:
        i["xueshu_paper_id"] = XueShuPaperID
        xueshuauthors_data.append(i)
    XueShuAuthors.insert(xueshuauthors_data).execute()

    # 1是相似文献
    xueshusimilar_related_data_data = []
    for i in related_data:
        for k, v in i.items():
            i[k] = json.dumps(v, ensure_ascii=False)
        i["xueshu_paper_id"] = XueShuPaperID
        i["sc_type"] = 1
        xueshusimilar_related_data_data.append(i)
    XueshuSimilarReferences.insert(xueshusimilar_related_data_data).execute()

    # 2是参考文献
    xueshusimilar_references_data = []
    for i in reference_data:
        for k, v in i.items():
            i[k] = json.dumps(v, ensure_ascii=False)
        i["xueshu_paper_id"] = XueShuPaperID
        i["sc_type"] = 2
        xueshusimilar_references_data.append(i)
    XueshuSimilarReferences.insert(xueshusimilar_references_data).execute()

    # 索引数据
    all_data = {
        "article_id": article_id,
        "article_name": article_title,
        "article_title": article_title,
        "authors_list": json.dumps(authors_list, ensure_ascii=False),
        "article_abstract": article_abstract,
        "article_keyword": json.dumps(keyword, ensure_ascii=False),
        "article_doi": DOI,
        "article_sc_cited": sc_cited,
        "article_year": year,
        "article_journal_title": journal_title,
        "article_dl_list": json.dumps(dl_list, ensure_ascii=False),
        "article_sc_search": json.dumps(sc_search, ensure_ascii=False),
        "related_data": json.dumps(related_data, ensure_ascii=False),
        "reference_data": json.dumps(reference_data, ensure_ascii=False),
    }
    print(all_data)
    # return all_data


if __name__ == '__main__':
    # get_related("汽车空气动力学数值仿真研究进展")
    # get_reference("1g6v0j70wq4p0mw0f47n0xf06n347113")
    get_simple_content("1v1b0r807x0d06c07m2t0x1034174532", "气动热力学")
