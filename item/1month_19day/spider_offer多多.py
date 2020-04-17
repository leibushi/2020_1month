# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 17:37
# @Author  : Mqz
# @FileName: spider_offer多多.py

import requests
import json

def requests_data():

    headers = {
        # 'authority': 'api.1point3acres.com',
        # 'pragma': 'no-cache',
        # 'cache-control': 'no-cache',
        # 'authorization': 'undefined',
        # 'device-id': '2a2510f45231dadb6f042f1dbcaeabec',
        # 'Origin': 'https://offer.1point3acres.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        # 'Content-Type': 'application/json',
        # 'Accept': '*/*',
        # 'sec-fetch-site': 'same-site',
        # 'sec-fetch-mode': 'cors',
        # 'Referer': 'https://offer.1point3acres.com/',
        # 'accept-encoding': 'XMLHttpRequest',
        # 'Connection': 'gzip, deflate, br',
        # 'accept-language': 'zh-CN,zh;q=0.9'
    }

    # data = "{\"filters\": {}}"
    # {filters: {}}
    # filters: {}
    # headers = {
    #     'Accept-Encoding': 'gzip, deflate, sdch',
    #     'Accept-Language': 'en-US,en;q=0.8',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Referer': 'http://www.wikipedia.org/',
    #     'Connection': 'keep-alive',
    # }
    # s = requests.session()
    # res = s.post('https://api.1point3acres.com/offer/results?ps=15&pg=1', headers=headers, data=data)
    # url = 'https://api.1point3acres.com/offer/results?ps=15&pg=1'
    # res = requests.post(url=url, headers=headers, data=data)
    #
    # print(res.text)
    import requests

    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }
    url = 'https://api.map.baidu.com/?qt=cen&b=12581481.11%2C2585014.49%3B12668265.17%2C2647990.58&l=11&ie=utf-8&oue=1&fromproduct=jsapi&callback=BMap._rd._cbk17407'
    url = 'https://api.map.baidu.com/?qt=s&c=257&wd=%E6%B1%89%E5%A0%A1%E7%8E%8B&rn=5&pn=3&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk93388&ak=l1efF5xp00r6mHIeesGh5amG'
    response = requests.get(url=url, headers=headers)
    print(response.text)
    # res = json.loads(response.text)
    # print(type(response.text))
    # print(res)

requests_data()