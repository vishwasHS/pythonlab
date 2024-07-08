# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:43:15 2024

@author: cseweb
"""

def freq_count(d):
    d2={}
    for value in d.values():
        if value not in d2:
            d2[value]=1
        else:
            d2[value]+=1
    return d2

d={1:10,2:10,3:20,4:20,5:40,6:10,7:70}
print(freq_count(d))