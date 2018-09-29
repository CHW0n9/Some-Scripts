#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 21 17:11:03 2018

@author: Wong Chihung
"""

import requests
import json
import time

addr="http://p.nju.edu.cn/portal_io/login"

uname='**********'  #用户名
upswd='**********'  #密码
data={'password':upswd,
      'username':uname}

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

msg = j['reply_msg']
if msg in ['登录成功!', '已登陆!']:
    name = j['userinfo']['fullname']
    yue = j['userinfo']['balance']/100
    con = '%s\n用户：%s\n余额：%s元'%(msg,name,yue)
    print(con)
else:
    print(msg)

#3秒后关闭
n = 3
for i in range(n):
    print(n-i,'秒后关闭窗口')
    time.sleep(1)
