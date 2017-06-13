#-*- coding: utf-8 -*-
import urllib.request
import re
def page(pg):
    url='https://www.pengfu.com/index_%s.html'%pg
    html=urllib.request.urlopen(url).read().decode('utf-8')
    #print(html)
    return html
def title(html):
    reg=re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>')
    item=re.findall(reg,html)
    return item
def content(html):
    reg=r'img src="(.*?)" width='
    item=re.findall(reg,html)
    return item
def download(url,name):
    path='img\%s.jpg'% name
    urllib.request.urlretrieve(url,path)
for i in range(1,6):
    html=page(i)
    title_list=title(html)
    content_list=content(html)
    for i,z in zip(title_list,content_list):
        download(z,i)
        print(i,z)

