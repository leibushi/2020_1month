# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 18:38
# @Author  : Mqz
# @FileName: 异步爬虫.py
import asyncio
import time

#定义第1个协程，协程就是将要具体完成的任务，该任务耗时3秒，完成后显示任务完成
async def to_do_something(i):
    print('第{}个任务：任务启动...'.format(i))
    #遇到耗时的操作，await就会使任务挂起，继续去完成下一个任务
    await asyncio.sleep(i)
    print('第{}个任务：任务完成！'.format(i))
#定义第2个协程，用于通知任务进行状态
async def mission_running():
    print('任务正在执行...')


start = time.time()
#创建一个循环
loop = asyncio.get_event_loop()
#创建一个任务盒子tasks，包含了3个需要完成的任务
tasks = [asyncio.ensure_future(to_do_something(1)),
         asyncio.ensure_future(to_do_something(2)),
         asyncio.ensure_future(mission_running())]
#tasks接入loop中开始运行
print(tasks)
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(end-start)