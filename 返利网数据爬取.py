# -*- coding:utf-8 -*-
import urllib2,re,time,socket,bs4
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
fanli_url='http://zhide.fanli.com/p'#主页
format_url='http://zhide.fanli.com/detail/1-'#商品
class Faly():
    def __init__(self):
        self.user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        self.html_data=[]
    def get_html(self,start_page=1,end_page=2):
        for i in range(start_page,end_page+1):
            rt=urllib2.Request(fanli_url+str(i))#创建一个request对象
            rt.add_header('User_Agent',self.user_agent)
            try:
                my_data=urllib2.urlopen(rt).read()
                self.html_data.append(my_data)
                time.sleep(2)
                socket.setdefaulttimeout(15)#控制下载源码的时间
            except urllib2.URLError,e:
                if hasattr(e,'reason'):
                    print '连接失败'
        return self.html_data
class GetData():
    def __init__(self):
        self.html=Faly().get_html()
        self.href=[]
        self.ls=[]
        self.url=[]
    def get_hrefurl(self):
        reg=r'data-id="\d{6}"'
        result=re.compile(reg)
        #for i in self.html:
        tag=result.findall(str(self.html))
        #print tag
        reg2=r'\d{6}'
        result2=re.findall(reg2,str(tag))
        if len(result2):
            for data in result2:
                if data not in self.ls:
                    self.ls.append(data)
                    url=format_url+str(data)
                    self.url.append(url)
                    #print self.url
        return self.url
a=GetData().get_hrefurl()
class Href_mg():
    def __init__(self):
        self.list=GetData().get_hrefurl()
        self.txt_list=[]
    def show_mg(self):
        for item in range(len(self.list)):
            if len(self.list):
                url=str(self.list[item])
                mg=urllib2.Request(url)
                try:
                    req=urllib2.urlopen(mg).read()
                    soup=BeautifulSoup(req,'html.parser')
                    txt=soup.find_all('h1')
                    self.txt_list.append(txt)
                except urllib2.URLError,e:
                    print e.reason
        return str(self.txt_list).decode('unicode_escape')
data=Href_mg().show_mg()
if __name__=='__main__':
    path='a.txt'
    with open(path,'a') as file:
        data_s=Href_mg().show_mg()
        reg4=r'<.+?>'
        data=re.sub(reg4,'',data).replace(',','\n').replace('[','').replace(']','').strip()
        print data
        file.write(data)
#html=Faly().get_url()