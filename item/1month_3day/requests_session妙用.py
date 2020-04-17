# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 18:07
# @Author  : Mqz
# @FileName: requests_session妙用.py
import requests
# 1、requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
# s = requests.sessions()
# req_param = '{"belongId": "300001312","userName": "alitestss003","password":"pxkj88","captcha":"pxpx","captchaKey":"59675w1v8kdbpxv"}'
# res = s.post('http://test.e.fanxiaojian.cn/metis-in-web/auth/login', json=json.loads(req_param))
# # res1 = s.get("http://test.e.fanxiaojian.cn/eos--web/analysis/briefing")
# print(res.cookies.values())   获取登陆的所有session


# 实例化session
session = requests.session()

# 目标url
url = 'https://www.douban.com/accounts/login'

form_data = {
    'source': 'index_nav',
    'form_email': 'xxx',
    'form_password': 'xxx',
    'captcha-solution': 'stamp',
    'captcha-id': 'b3dssX515MsmNaklBX8uh5Ab:en'
}

# 设置请求头
req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# 使用session发起请求
response = session.post(url, headers=req_header, data=form_data)

if response.status_code == 200:

    # 访问个人主页：
    url = 'https://www.douban.com/people/175417123/'

    response = session.get(url, headers=req_header)

    if response.status_code == 200:
        with open('douban3.html', 'w', encoding='utf-8') as file:
            file.write(response.text)


# https: // blog.csdn.net / weixin_42575020 / article / details / 95179840