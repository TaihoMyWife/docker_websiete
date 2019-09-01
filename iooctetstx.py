#!/usr/bin/env python
#coding=utf-8

import requests
import json
import time
time.time()

url="http://202.117.10.37:8080/render?target=collectdip2collectd.interface-eth0.if_octets.rx&format=json"
content=requests.get(url).content.decode()
t = json.loads(content)
valuesio3=[]
timessio3=[]
for i in t:
    item = i
datapoints=item['datapoints']

for i in range(1,10):

    s = datapoints[-i]
    timeStamp = s[1]
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    valuesio3.append(str(s[0]))
    timessio3.append(str(otherStyleTime))

    #print('metric name:'+'cpu_idle'+'  '+'time:'+str(otherStyleTime)+'  '+'value:'+str(s[0]))
#print('1')
#print(timess)



