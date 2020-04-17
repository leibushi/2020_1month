# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 10:09
# @Author  : Mqz
# @FileName: lagou_spider.py
import requests
# from

def get_lagou_info():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python/p-city_213?&cl=false&fromSearch=true&labelWords=&suginput='
    }

    # url = 'POST https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
    url2 = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
    s = requests.session()
    # 更新headers信息，cookies会变
    s.headers.update(headers)
    url1 = 'https://www.lagou.com/jobs/list_python/p-city_213?&cl=false&fromSearch=true&labelWords=&suginput= HTTP/1.1'
    s.get(url1, headers=headers)
    # res = s.post(url, headers=headers)
    # print(res.text)
    from_data = {
        'first': '广州',
        'pn': '1',
        'kd': 'python',
        # 'sid': 'ab833245de8a4f949cf10eabb8b4180f'
    }
    res = s.post(url2, headers=headers, data=from_data)
    print(res.text)

get_lagou_info()
