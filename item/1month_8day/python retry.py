# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 16:25
# @Author  : Mqz
# @FileName: python retry.py
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class RetryRequests(object):

    def __init__(self, connect_timeout, read_timeout, max_retry, status_forcelist=None, session=None):
        self.session = session or requests.Session()
        retry = Retry(
            total=max_retry,  #最大重试多少次
            backoff_factor=0.1,  # 每次重试时间间隔（0.1， 0.2， 0.4）
            status_forcelist=status_forcelist,    # 返回哪些状态码时进行重试
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.timeout = (connect_timeout, read_timeout)

    def get(self, url, timeout=None, **kwargs):
        if timeout is None:
            timeout = self.timeout
        return self.session.get(url, timeout=timeout, **kwargs)

    def post(self, url, timeout=None, data=None, json_data=None, **kwargs):
        if timeout is None:
            timeout = self.timeout
        return self.session.post(url, timeout=timeout, data=data, json=json_data, **kwargs)


# common_request_service = RetryRequests(10, 30, 3, [500, 502, 503, 504])


# if __name__ == "__main__":
#     import time
#     rr = common_request_service
#     now = time.time()
#     try:
#         print(rr.get("http://localhost:8888").text)
#     except Exception as e:
#         print(e)
#     print(time.time() - now)

import requests
from retrying import retry

headers = {}


@retry(stop_max_attempt_number=3)  # 最大重试3次，3次全部报错，才会报错
def _parse_url(url):
    print(url)
    response = requests.get(url, headers=headers, timeout=3)  # 超时的时候回报错并重试
    assert response.status_code == 200  # 状态码不是200，也会报错并充实
    return response


try:  # 进行异常捕获
    response = _parse_url("127.0.0.1")
except Exception as e:
    print(e)
    response = None
