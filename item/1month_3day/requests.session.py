# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 18:28
# @Author  : Mqz
# @FileName: requests.session.py
import requests
import time
# mycookie = { "PHPSESSID":"56v9clgo1kdfo3q5q8ck0aaaaa" }
# x = requests.session()
# requests.utils.add_dict_to_cookiejar(x.cookies,{"PHPSESSID":"07et4ol1g7ttb0bnjmbiqjhp43"})
# x.get("https://baidu.com", cookies = mycookie)
# time.sleep(5)
#请求以后抓包可以检验一下是不是添加成功
# x.get("http://127.0.0.1:80")
# 这样，通过requests.utils.add_dict_to_cookiejar对session对象设置cookie，之后所有的请求都会自动加上我自定义的cookie内容。

# 也可以通过requests.utils.cookiejar_from_dict 先生成一个cookiejar对象，时候在赋值给session.cookies。貌似还可以使用session.cookies.set()或者update()。
# https://blog.csdn.net/weixin_42575020/article/details/95179840

# 处理cookie内容为字典
cookie = "SINAGLOBAL=821034395211.0111.1522571861723; wb_cmtLike_1850586643=1; un=tyz950829@sina.com; wb_timefeed_1850586643=1; UOR=,,login.sina.com.cn; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWsNeq71O_sXkkXNnXFHgOW5JpX5KMhUgL.Fo2RSK5f1hqcShe2dJLoI0qLxK-L12qLB-zLxKqL1hnL1K2LxK-LBo5L12qLxKqL1hML1KzLxKnL1K.LB-zLxK-L1K-LBKqt; YF-V5-G0=c99031715427fe982b79bf287ae448f6; ALF=1556795806; SSOLoginState=1525259808; SCF=AqTMLFzIuDI5ZEtJyAEXb31pv1hhUdGUCp2GoKYvOW0LQTInAItM-ENbxHRAnnRUIq_MR9afV8hMc7c-yVn2jI0.; SUB=_2A2537e5wDeRhGedG7lIU-CjKzz-IHXVUm1i4rDV8PUNbmtBeLVrskW9NUT1fPIUQGDKLrepaNzTEZxZHOstjoLOu; SUHB=0IIUWsCH8go6vb; _s_tentry=-; Apache=921830614666.5322.1525261512883; ULV=1525261512916:139:10:27:921830614666.5322.1525261512883:1525239937212; YF-Page-G0=b5853766541bcc934acef7f6116c26d1"
cookie_dict = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
print(cookie_dict)
print(type(cookie))
cookies = cookie.split("; ")
print(cookies)
for i in cookie.split("; "):
    x = i.split("=")[0]
    print(x)
#     print(i)
