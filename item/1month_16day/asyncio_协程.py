# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 13:36
# @Author  : Mqz
# @FileName: asyncio_协程.py
import asyncio
import time


async def request(url):
    print('正在下载：', url)
    #     sleep(2) #非异步模块的代码：在此处如果存在非异步操作代码，则会彻底让asyncio失去异步的效果
    await asyncio.sleep(2)
    print('下载成功：', url)


urls = [
    'www.baidu.com',
    'www.taobao.com',
    'www.sogou.com'
]
start = time.time()
loop = asyncio.get_event_loop()
tasks = []  # 任务列表，放置多个任务对象
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

# 将多个任务对象对应的列表注册到事件循环中
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时：', time.time() - start)