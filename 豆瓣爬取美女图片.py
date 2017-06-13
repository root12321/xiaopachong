#-*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
url='http://www.dbmeinv.com/dbgroup/show.htm?cid=4&pager_offset=1'
x=0
def crawl(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers)#模拟浏览器，因为这个网页有反扒功能
    page=urllib.request.urlopen(req,timeout=20)
    contents=page.read()
    #print(contents)
    soup=BeautifulSoup(contents,'html.parser')#Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码
    my_girl=soup.find_all('img')#找到标签img里面的内容
    for girl in my_girl:
        link=girl.get('src')#找到标签src里面的内容（图片网址）
        print(link)
        global x
        urllib.request.urlretrieve(link, 'img1\%s.jpg'% x)#下载功能，将link链接里的图片下载保存到img1文件夹，并命名为 数字.jpg
        x=x+1
        print('正在下载第%s张'%x)
for page in range(1,3):
    page=page+1
    url='http://www.dbmeinv.com/dbgroup/show.htm?cid=4&pager_offset=%s'%page
    crawl(url)
print('报告大人：图片已全部下载')