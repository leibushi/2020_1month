# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 13:47
# @Author  : Mqz
# @FileName: tuxing_show.py

from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts import options as opts

# 不习惯链式调用的开发者依旧可以单独调用方法
# bar = Bar()
# bar.add_xaxis(["测试A", "测试B", "测试C", "测试D", "测试E", "测试F"])
# bar.add_yaxis("隧道ip", [5993, 5976, 6448, 6361, 6257, 90])
# bar.add_yaxis("直连ip", [7128, 6450, 5664, 6915, 6979, 10])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="IP测试", subtitle="每个ip10分钟测试"))
# bar.render()
line = Line()
line.add_xaxis(["测试A", "测试B", "测试C", "测试D", "测试E", "测试F"])
line.add_yaxis("隧道ip", [5993, 5976, 5664, 6361, 6257, 5312])
line.add_yaxis("直连ip", [7128, 6450, 6448, 6915, 6979, 7101])
line.set_global_opts(title_opts=opts.TitleOpts(title="IP测试", subtitle="每个ip10分钟采集数量测试"))
line.render()