# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:04:51 2024

@author: cseweb
"""
import math as m
p=int(input("enter principal ampunt"))
t=int(input("enter time"))
r=int(input("enter rate of intrest"))
si=(p*t*r)/100
print("simple intrest is:",si)
a=(1+r/100)
A=p*m.pow(a,t)
ci=A-p
print("compunt intrest",ci)