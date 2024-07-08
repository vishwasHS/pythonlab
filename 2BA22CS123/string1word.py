# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:02:18 2024

@author: cseweb
"""

s=input("enter the string")
fd=False
fa=False
for i in s:
    if(i.isalpha()):
        fa=True
    if(i.isdigit()):
        fd=True
if(fa==True and fd==True):
    print("strings conatins lettter and digit")
else:
    print("no letters and digit")
    