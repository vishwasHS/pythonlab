# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:31:53 2024

@author: cseweb
"""
import math as m
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if(a%2!=0 and b%2!=0):
    if(a!=b):
        a,b=b,a
        print("after swaping")
        print("1st number",a,"2nd number",b)
    else:
        print("both are equal")
        print("factorial",m.factorial(a))
elif(a%2==0 and b%2==0):
    if(a==b):
        print("factorial",m.factorial(a))
    else:
        if(a>b):
            print("large is a")
        else:
            print("b is large")
else:
    print("factorial of a ",m.factorial(a))
    print("factorial of b",m.factorial(b))