# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:28:46 2024

@author: cseweb
"""
import math as m
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=b*b-4*a*c
if d==0:
    root=b/2*a
    print("roots are equal",root)
elif d>0:
    r1=(-b-m.sqrt(d))/(2*a)
    r2=(-b+m.sqrt(d))/(2*a)
    print("roots are real and different",r1,r2)
else:
    print("roots are imaginary")
    