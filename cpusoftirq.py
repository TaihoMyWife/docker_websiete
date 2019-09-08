#!/usr/bin/env python
#coding=utf-8

import requests
import json
import time
time.time()

url="http://202.117.10.37:8080/render?target=collectdip2collectd.cpu-0.cpu-softirq&format=json"
content=requests.get(url).content.decode()
t = json.loads(content)
values3=[]
timess3=[]
for i in t:
    item = i
datapoints=item['datapoints']

for i in range(1,10):

    s = datapoints[-i]
    timeStamp = s[1]
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    values3.append(str(s[0]))
    timess3.append(str(otherStyleTime))

