# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:52:16 2024

@author: cseweb
"""
s=input("enter the string")
for i in s:
    if(i==','):
        print(i.replace(i,'.'),end="")
    elif(i=='.'):
        print(i.replace(i,','),end="")
    else:
        print(i,end="")