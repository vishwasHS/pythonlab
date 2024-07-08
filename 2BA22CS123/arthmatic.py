# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:11:45 2024

@author: cseweb
"""

a=int(input("enter first number:"))
b=int(input("enter second integer:"))
print("enter A for arthmatic operation \n or B for bitwise operations")
ch=input("enter your choice")
if(ch=="A"):
    c=input("enter operations to be performered +\n-\n*\n/\n")
    if(c=="+"):
        print("addition of A and B is :",a+b)
    elif(c=="-"):
        print("subraction of A and B is :",a-b)
    elif(c=="*"):
        print("multiplication of A and B is :",a*b)
    elif(c=="/"):
        print("dividion of  A and B:",a/b)
    else:
        print("invalid choice")
elif(ch=="B"):
    c=input("enter bitwise operators 1 for AND\n 2 for OR\n 3 for NOT\n 4 for XOR\n")
    if(c=="1"):
        print("bitwise AND ",bin(a&b))
    elif(c=="2"):
        print("bitwise OR ",bin(a|b))
    elif(c=="3"):
        print("bitwise NOT ",bin(~b),bin(~a))
    elif(c=="4"):
        print("bitwise XOR ",bin(a^b))
    else:
        print("invalid choice")
    


    