# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:54:43 2024

@author: cseweb
"""

n=int(input("enter a number"))
fi=[0,1]
for i in range(2,n):
    fib=fi[i-1]+fi[i-2]
    fi.append(fib)
if(n==0):
    print("zero")
elif(n==1):
    print(fi[0])
else:
    print("fibonacci sequence")
    for j in fi:
        print(j,end="->")