# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:59:33 2024

@author: cseweb
"""

l=[1,8,3,4,26,31,25,22,21,78]
ec=0
oc=0
odsum=0
evsum=0
for i in l:
    if i%2==0:
        evsum+=i
        ec+=1
    else:
        odsum+=i
        oc+=1
print("even sum is",evsum)
print("odd sum is",odsum)
print("odd count",oc)
print("even count",ec)