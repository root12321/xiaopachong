# -*- coding=utf-8 -*-
import urllib.request
import re

domo='http://www.quanshuwang.com'
def getSortList(sort):
    res=urllib.request.urlopen('http://www.quanshuwang.com/map/%s.html'%sort)
    html=res.read().decode('gbk')
    reg=r'<a href="(/book/.*?)" target="_blank">(.*?)</a>'
    reg=re.findall(reg,html)
    return reg
def getNoveList(url):
    html=urllib.request.urlopen(url).read().decode('gbk')
    reg=r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    reg=re.findall(reg,html)
    return reg
def getCharter(url):
    html=urllib.request.urlopen(url).read().decode('gbk')
    reg=r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    reg=re.findall(reg,html)
    return reg
for sort in range(1,10):
    for i in getSortList(sort):
        for j in getNoveList(domo+i[0]):
            url=domo+i[0].replace('index.html',j[0])
            content=getCharter(url)
            print(content)
            break
