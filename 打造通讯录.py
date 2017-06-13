# -*- coding=utf-8 -*-
import pickle
import re
import os
if os.path.exists('D:\Persion.data')==False:
    f=open('D:\Persion.data','wb')
    temp={'total':0}
    pickle.dump(temp,f)
    f.close()
else:
    pass
def add():
    f=open('D:\Persion.data','rb')
    a=pickle.load(f)

    f.close()
    b=0
    name=input('请输入所要添加的联系人：')
    for key in a.keys():
        if key==name:
            print('联系人已存在，请重新添加')
            break
        if key!=name:
            number=input('请输入号码：')
            information={name:number}
            a['total']+=1
            a.update(information)
            f=open('D:\Persion.data','wb')
            pickle.dump(a,f)
            f.close()
            print('添加成功')
            break


def showall():
    f=open('D:\Persion.data','rb')
    a=pickle.load(f)
    print('一共有{}个联系人'.format(a['total']-1))
    for key in a.keys():
        if key !='total':
            print('{''}:{''}'.format(key,a[key]))
    f.close()
def exit():
    quit()
def Search(name):
    f=open('D:\Persion.data','rb')
    a=pickle.load(f)
    if name in a.keys():
        print('{}的号码是{}'.format(name,a[name]))
    else:
        print('该联系人不存在')
    f.close()
def delete(name):
    f= open('D:\Persion.data','rb')
    a=pickle.load(f)
    f.close()
    if name in a.keys():
        a.pop(name)
        a['total']-=1
        f=open('D:\Persion.data','wb')
        pickle.dump(a, f)
        f.close()
        print('删除成功')
    else:
        print('联系人不存在，无法删除')
def change(name):
    f=open('D:\Persion.data','rb')
    a=pickle.load(f)
    f.close()
    if name in a.keys():
        y=input('请输入修改后的号码:')
        a[name]=y
        f=open('D:\Persion.data','wb')
        pickle.dump(a,f)
        print('修改成功')
    else:
        print('该联系人不存在，请查证后重新输入')



def point():
    print('显示所有联系人请输入：0')
    print('添加联系人请输入：1')
    print('查找联系人请输入:2')
    print('删除联系人请输入：3')
    print('修改联系人请输入：4')
    print('退出请输入：5')
point()
while True:
    x=input('请输入你的选择：')
    if x=='1':
        add()
        continue
    if x=='0':
        showall()
        continue
    if x=='5':
        exit()
        continue
    if x=='3':
        name = input('请输入要删除的姓名：')
        delete(name)
    if x=='2':
        name=input('请输入要查找的姓名：')
        Search(name)
        continue
    if x=='4':
        name = input('请输入要修改的姓名：')
        change(name)
        continue
