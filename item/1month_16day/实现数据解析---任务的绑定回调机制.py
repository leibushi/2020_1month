# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 13:54
# @Author  : Mqz
# @FileName: 实现数据解析---任务的绑定回调机制.py
import time

import aiohttp
import asyncio
from common import ip_proxy_1_1

proxies = ip_proxy_1_1.get_proxy()
# print(proxies)

# 回调函数：解析响应数据
def callback(task):
    print('this is callback()')
    # 获取响应数据
    page_text = task.result()
    # print('在回调函数中，实现数据解析', page_text)
    print('在回调函数中，实现数据解析')


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        }
        # 加入代理但是不能以proxies开头
        async with await session.get(url=url, headers=headers, data=proxies) as response:
            page_text = await response.text()  # read()  json()
            #             print(page_text)
            print(url)
            return page_text


start = time.time()
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
tasks = []
loop = asyncio.get_event_loop()
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    # 给任务对象绑定回调函数用于解析响应数据
    task.add_done_callback(callback)
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时：', time.time() - start)