# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 18:39
# @Author  : Mqz
# @FileName: 异步爬虫练习.py
#
# import asyncio
# import time
#
# # 执行函数
# async def to_do_something(i):
#     print('第{}个任务: 任务启动...'.format(i))
#
#     await asyncio.sleep(i)
#     print('第{}个任务: 任务执行...'.format(i))
#
# #定义第2个协程，用于通知任务进行状态
# async def mission_running():
#     print('任务正在执行...')
# start = time.time()
# # 创建一个循环 异步事件获取循环
# loop = asyncio.get_event_loop()
# # 创建一个任务盒子tasks 包含3个需要完成的任务
# # 异步确保将来
# # tasks = [asyncio.ensure_future(to_do_something(i)), asyncio.ensure_future(mission_running()) for i in range(3)]
# tasks = [asyncio.ensure_future(to_do_something(i)) for i in range(3)]
# # print(tasks)
# # for i in tasks:
# #     print(i)


# 参数 https://www.cnblogs.com/wanglan/p/10821140.html#_label1
# 基本的使用
# import asyncio
#
# async def hello(name):
#     print('hello to:', name)
#
# # 获取一个协程对象
# c = hello('bobo')
# # 创建一个异步io\并发，事件循环对象
# loop = asyncio.get_event_loop()
# # 将协程对象注册到事件循环中，然后启动事件循环对象
# loop.run_until_complete(c)

# task使用

"""
import asyncio
async def hello(name):
    print('hello to:', name)

# 获取了一个协程对象
c = hello('bobo')
# 创建一个事件循环对象
loop = asyncio.get_event_loop()
# 协程进行进一步的封装，封装到了task对象中
task = loop.create_task(c)
print(task)
# 循环运行知道完整
loop.run_until_complete(task)
print(task)


# future
# 未来的
import asyncio
async def hello(name):
    print('hello to:', name)

# 获取了一个协程对象
c = hello('bobo')
# # 创建一个事件循环对象
loop = asyncio.get_event_loop()
# 任务       异步io保证将来的
task = asyncio.ensure_future(c)
print(task)
# 循环运行知道完整
loop.run_until_complete(task)
print(task)

# 绑定回调(task)

import asyncio
def callback(task):
    print('I am callback:', task.result())
    

async def hello(name):
    print('hello to:', name)
    return name
    

c = hello('bobo')
# # 创建一个事件循环对象
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 给任务对象绑定一个回调函数
task.add_done_callback(callback)
loop.run_until_complete(task)

"""

# 多任务异步协程
import time
import requests
import asyncio

async def get_page(url):
    print('正在下载:', url)
    #之所以没有实现异步操作，原因是因为requests模块是一个非异步的模块
    response = requests.get(url=url)
    print('响应数据：', response.text)
    print('下载成功：', url)

start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]
tasks = []
loop = asyncio.get_event_loop()
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
print('总耗时：', time.time()-start)