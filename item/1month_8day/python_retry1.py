# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 16:42
# @Author  : Mqz
# @FileName: python_retry1.py
from retrying import retry

def retry_if_io_error(exception):
    print("---------------------------")
    return isinstance(exception, FileNotFoundError)

# @retry(retry_on_exception=retry_if_io_error)
# def this_maybe_has_error():
#     try:
#         print("test")
#         with open("aa.txt", 'r') as f:
#             f.readlines()
#     except FileNotFoundError as e:
#         raise FileNotFoundError
# this_maybe_has_error()
@retry
def test_retry():
    try:
        1/0
    except Exception as e:
        print('异常', e)
        raise e
# test_retry()
# 2、使用stop_max_attempt_number最大运行次数

@retry(stop_max_attempt_number=3)
def test_stop_max_attempt_number():
    try:
        1/0
    except Exception as e:
        print(e)
        raise e
# test_stop_max_attempt_number()


# 3、stop_max_delay 设置失败重试的最大时间, 单位毫秒，超出时间，则停止重试
@retry(stop_max_delay=1000)
def test_stop_max_delay():
    try:
        # sleep(2)
        print("test")
        1/0
        # print("test")
    except Exception as e:
        print(e)
        raise e

# test_stop_max_delay()


# 4、wait_fixed 设置失败重试的间隔时间
@retry(wait_fixed=1000)
def test_wait_fixed():
    try:
        print("test")
        1/0
    except Exception as e:
        print(e)
        raise e

test_wait_fixed()
