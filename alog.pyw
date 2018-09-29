# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:07:58 2018

@author: Wong Chihung
"""

import time
import threading
import tkinter
import requests
import json

def login():
    addr="http://p.nju.edu.cn/portal_io/login"
    
    uname='**********'   #账号
    upswd='**********'    #密码
    data={'password':upswd, 'username':uname}
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'Cache-Control': 'no-cache',
        'Connection': 'Keep-Alive',
        'Content-Length': '36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'safedog-flow-item=',
        'Host': 'p.nju.edu.cn',
        'Origin': 'http://p.nju.edu.cn',
        'Referer': 'http://p.nju.edu.cn/portal/index.html?v=201806151414',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'X-Requested-With': 'XMLHttpRequest'}
    
    z=requests.post(addr,data,headers)
    j=json.loads(z.text)
    #print(j)   #调试用
    msg = j['reply_msg']
    if msg in ['登录成功!', '已登陆!']:
        name = j['userinfo']['fullname']
        yue = j['userinfo']['balance']/100
        con = '%s\n用户：%s\n余额：%s元'%(msg,name,yue)
    else:
        con = msg
    return con

def Close():
    root.destroy()

def autoClose(n=3):
    '''自动关闭函数，参数n为自动关闭的秒数'''
    for i in range(n):
        lbtime['text'] = '%s秒后自动关闭'%(n-i)
        root.update()
        time.sleep(1)
    Close()

con = login()

#主窗口
root = tkinter.Tk()
root.wm_attributes('-topmost',1)
root.focus_force()
root.title('校园网')
sw, sh = (root.winfo_screenwidth(), root.winfo_screenheight())  #系统分辨率
ww, wh = (220,140)                                              #窗口分辨率
x ,y = ((sw-ww)/2,(sh-wh)/2)
root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))                       #窗口居中
root.resizable(False,False)
#文字内容
text = tkinter.Text(root)
text.place(x = 10, y = 10, width = 200, height = 80)
text.insert('0.0',con)
#倒计时文字标签
lbtime = tkinter.Label(root, anchor ='w')
lbtime.place(x = 10, y = 100, width = 150)
#按钮
butn = tkinter.Button(root, text ='确定', command = Close)
butn.place(x = 170, y = 100, width = 40)
butn.focus_set()

t = threading.Thread(target = autoClose)
t.start()

root.mainloop()
