# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 18:24
# @Author  : Mqz
# @FileName: 异步爬虫测试1.py
import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())