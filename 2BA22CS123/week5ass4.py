# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:02:15 2024

@author: cseweb
"""

l1=["s001","s002","s003","s004"]
l2=["AAA","BBB","CCC","DDD"]
l3=[1,2,3,4]
di={}
sd={}
for i in range(len(l1)):
    sd = {l2[i]: l3[i]}
    di[l1[i]] = sd
print(di)
 