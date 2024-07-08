# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:45:30 2024

@author: cseweb
"""

n=input("enter the string")
if(n.isalpha()):
    print("string is only alphabet")
    if(n.isupper()):
        print("string is in uppercase")
    else:
        print("string is in lower case")
elif(n.isdigit()):
    print("string contains numbers")
    sum=0
    for i in n:
        sum+=int(i)
    print("sum is",sum)
elif(n.isalnum()):
    print("string contains both alphabet and numbers")

else:
    print("special characters")
    c=0
    for i in n:
        if(not i.isalpha() and not i.isdigit()):
            c=c+1
    print("total count of specail characters",c)