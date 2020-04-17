# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 15:44
# @Author  : Mqz
# @FileName: js_demo_spider.py
# js逆向
import execjs
import re
import requests
from lxml import html


def get_cookie(text):
    text = re.search(r'(var x=.*?pop\(\)\);)', text).group(1)
    print(text)
    js_string = """
        get_eval_string = function (){
            %s
            var data="";
            while(data.indexOf('__jsl_clearance=15') === -1 && z++){
                data = y.replace(/\\b\w+\\b/g, function(y){return x[f(y,z)-1]||("_"+y)});
            }
            return data;
        };
    """ % text
    js = execjs.compile(js_string)
    print('js', js)
    eval_string = js.call('get_eval_string')
    print(eval_string)
    eval_string = re.search(r"('__jsl_clearance.*?\(\))\+';Expires", eval_string).group(1)
    # p_name = re.search('function\(\){var (.*?)=document', eval_string).group(1).split(' ')[-1]
    # b_text = "var %s='www.gsxt.gov.cn/';" % p_name
    # eval_string = re.sub(r'var ' + p_name + '.*?toLowerCase\(\);', b_text, eval_string)
    js_string_cookie = """
        window = {};
        cookie = %s
    """ % eval_string
    js_cookie = execjs.compile(js_string_cookie)
    cookie = js_cookie.eval('cookie')
    print(cookie)
    print({k: v for k, v in [cookie.split('=')]})
    return {k: v for k, v in [cookie.split('=')]}


s = requests.session()
s.headers = {
    'Host': 'www.mps.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
}
res = s.get('http://www.mps.gov.cn/n2253534/n2253535/index.html')
print('count%s' % res.text)
cookie = get_cookie(res.text)
print('cookie%s' % cookie)
s.cookies.update(cookie)
res = s.get('http://www.mps.gov.cn/n2253534/n2253535/index.html')
print(res.text)
select = html.fromstring(res.text)
print(select)
# lis = select.xpath('//ul[@class="listUla"]/li//div[@class="co1 ellipsis fl"]/text()')
# print(lis)
"""
"""
