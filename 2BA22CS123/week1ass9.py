# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:42:00 2024

@author: cseweb
"""

n=int(input("enter a number"))
if n<1:
    print("not a prime")
else:
    for i in range(2,n//2+1):
        if(n%i==0):
            print("not a prime")
            break
    else:
        print("is a prime")
            