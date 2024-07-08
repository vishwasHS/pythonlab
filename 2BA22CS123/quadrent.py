# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:38:56 2024

@author: cseweb
"""

a=int(input("enter a coordinate"))
b=int(input("enter b coordinate"))
if a==0 and b==0:
    print(a,b,"lie at origin")
elif a>0 and b>0:
    print(a,b,"lie at 1st quadrent")
elif a<0 and b>0:
    print(a,b,"lie on 2rd quadrent")
elif a<0 and b<0:
    print(a,b,"lie on 3th quadrent")
elif a>0 and b<0:
        print(a,b,"lie on 4th quadrent")
elif a==0 :
    print("lies on y axis")
elif b==0:
    print("lies on x axis")
else:
    print("invalid")
    
