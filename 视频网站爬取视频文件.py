# -*- coding:utf-8 -*-
import urllib,re,requests
url_name=[]
def get():
    hd={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    url='http://www.budejie.com/video/'
    html=requests.get(url,headers=hd).text
    url_content=re.compile(r'<div class="j-r-list-c">(.*?)</div>(.*?)</div>',re.S)
    url_contents=re.findall(url_content,html)

    url_reg=r'data-mp4="(.*?)">'
    url_item=re.findall(url_reg,str(url_contents))
    name_reg=re.compile(r'<a href="/detail-.{8}.html">(.*?)</a>',re.S)
    name_item=re.findall(name_reg,str(url_contents))
    for j,k in zip(name_item,url_item):
        try:
            urllib.request.urlretrieve(k,'video\\%s.mp4'%j)
        except:
            pass
    return html
a=get()
