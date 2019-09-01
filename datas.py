#!/usr/bin/env python
#coding=utf-8

import requests
import json
import time
time.time()

url="http://192.168.121.131:8080/render?target=collectdip2collectd.cpu-0.cpu-idle&format=json"
content=requests.get(url).content
t = json.loads(content)
values=[]
timess=[]
for i in t:
    item = i
datapoints=item['datapoints']

for i in range(1,10):

    s = datapoints[-i]
    timeStamp = s[1]
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    values.append(str(s[0]))
    timess.append(str(otherStyleTime))

    #print('metric name:'+'cpu_idle'+'  '+'time:'+str(otherStyleTime)+'  '+'value:'+str(s[0]))
#print('1')
#print(timess)



