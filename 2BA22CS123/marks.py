# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:26:59 2024

@author: cseweb
"""

a=float(input("enter the student mark of 1 subjects"))
b=float(input("enter the student mark of 2 subjects"))
c=float(input("enter the student mark of 3 subjects"))
d=float(input("enter the student mark of 4 subjects"))
e=float(input("enter the student mark of 5 subjects"))
total=a+b+c+d+e
print(total)
per=(total*5)/100
print(per)
if per>90:
    print("s grade")
elif per>80 and per>89:
    print("A grade")
elif per>70 and per>79:
    print("B grade")
elif per>60 and per>79:
    print("C grade")
elif per>50 and per>59:
    print("D grade")
else:
    print("fail")    
    
    
    