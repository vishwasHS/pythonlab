# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:47:31 2024

@author: cseweb
"""

n=int(input("enter the number"))
m=int(input("enter the number"))
for j in range(n,m+1):
    if j>1:
        for i in range(2,j//2+1):
            if(j%i==0):
                break
        else:
            print(j)
            