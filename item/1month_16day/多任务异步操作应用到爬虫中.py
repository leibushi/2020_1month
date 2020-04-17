# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 13:39
# @Author  : Mqz
# @FileName: 多任务异步操作应用到爬虫中.py
import time

import aiohttp
import asyncio

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            page_text = await response.text()
            print(page_text)


start = time.time()

urls = [
    'http://www.baidu.com',
    'https://www.cnblogs.com/wanglan/p/10821140.html#_label1',
    # 'http://127.0.0.1:5000/bobo',
    # 'http://127.0.0.1:5000/jay',
    # 'http://127.0.0.1:5000/tom',
    # 'http://127.0.0.1:5000/bobo',
    # 'http://127.0.0.1:5000/jay',
    # 'http://127.0.0.1:5000/tom'
]

tasks = []
loop = asyncio.get_event_loop()
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时:', time.time() - start)