# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:18:55 2024

@author: cseweb
"""
l="abcdefghijklmnopqrstuvwxyz"
s=input("enter the string")
s=s.lower()
p=False
for i in l:
    if(i not in s):
        p=False
    else:
        p=True
if(p==True):
    print("it is pangram")
else:
    print("not a pangram")