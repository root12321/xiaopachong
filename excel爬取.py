# -*- coding:utf-8 -*-
import requests,json,xlwt

pn=1
item=[]
def get_content(pn):
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data={'first':'true',
          'pn':pn,
          'kd':'python'}
    html=requests.post(url,data).text
    #print(html)
    html=json.loads(html)
    for i in range(14):
        items=[]
        items.append(html['content']['positionResult']['result'][i]['positionName'])#招聘职位
        items.append(html['content']['positionResult']['result'][i]['companyFullName'])#公司名称
        items.append(html['content']['positionResult']['result'][i]['salary'])#薪资
        items.append(html['content']['positionResult']['result'][i]['city'])#地点
        items.append(html['content']['positionResult']['result'][i]['positionAdvantage'])#福利
        items.append(html['content']['positionResult']['result'][i]['companyLabelList'])#条件
        items.append(html['content']['positionResult']['result'][i]['firstType'])#类型
        item.append(items)
        #print(item)
    #print(html)
    return item
def excel_write(items):
    newTable='text.xls'#表的名称
    wb=xlwt.Workbook(encoding='utf-8')#创建excel文件
    ws=wb.add_sheet('test1')#创建表的名称
    headData=['招聘职位','公司名称','薪资','地点','福利','条件','类型']
    for hd in range(0,7):
        ws.write(0,hd,headData[hd],xlwt.easyxf('font:bold on'))#0行，hd列
    index=1
    for items in item:
         for i in range(0,7):
             ws.write(index,i,str(items[i]))
         index+=1
         wb.save(newTable)

if __name__=='__main__':
    items=get_content(pn)
    excel_write(items)
