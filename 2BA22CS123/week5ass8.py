# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:15:38 2024

@author: cseweb
"""
def isPowerOfTwo(n): 
       return (n and (not(n & (n - 1)))) 
def check_thabit(n):
    n=n+1
    if(n%3==0):
        n=n//3
    else:
        return False
    
    if(isPowerOfTwo(n)):
        return True
    else:
        return False    
n=int(input("enter a number"))
if check_thabit(n):
    print("yes it is thabit")
else:
    print("no")