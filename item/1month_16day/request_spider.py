# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 17:17
# @Author  : Mqz
# @FileName: request_spider.py
import time

import requests
from common import ip_proxy_1_1

proxies = ip_proxy_1_1.get_proxy()
def requests_datas():

    urls = [
        'https://www.cnblogs.com/wanglan/p/10821140.html#_label1',
        'http://baidu.com',
        'http://taobao.cn',
        # 'http://jindong.com',
        # 'https://www.runoob.com/java/java-basic-syntax.html',
        'https://www.w3cschool.cn/java/java-basic-syntax.html',
        'https://blog.csdn.net/yrg5101?t=1',
        'https://www.processon.com/diagrams',
        'https://dev.tencent.com/u/YangXiaoShuai/p/zyl_x_sign_service_monitor/git'
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    for url in urls:
        res = requests.get(url=url, headers=headers, proxies=proxies)
        # print(res.text)

start = time.time()
requests_datas()
print('共有时间:', time.time() - start)