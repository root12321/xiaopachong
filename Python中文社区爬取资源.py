# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
from urllib import request
text2=[]
url='http://www.pythontab.com/html/pythonhexinbiancheng/index.html'
url_list=[url]
for i in range(2,19):
    url_list.append('http://www.pythontab.com/html/pythonhexinbiancheng/%s.html'%i)
#print(url_list)
for j in url_list:
    request1=urllib.request.urlopen(j)
    html=request1.read().decode('utf-8')
    #print(html)
    soup=BeautifulSoup(html,'html.parser')
    titles=soup.select('#catlist > li > a')
    #print(titles)
    links = soup.select('#catlist > li > a')
    for title,link in zip(titles,links):
        data={
            'title':title.get_text(),
            'link':link.get('href')
        }
        text2.append(data)

    for l in text2:
        request1=urllib.request.urlopen(l['link'])
        html=request1.read()
        soup=BeautifulSoup(html,'html.parser')
        b=soup.select('div.content > p')
        text=[]
        for t in b :
            text.append(t.get_text().encode('utf-8'))

        title_text=l['title']
        title_text = l['title'].replace('*','').replace('/','or').replace('"','').replace('?','wh').replace(':','')
        with open('study/%s.txt'%title_text,'wb') as f :
            for i in text:
                f.write(i)

