# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:19:42 2024

@author: cseweb
"""

from datetime import datetime
now=datetime.now()
print(now)
month=now.strftime("%B")
print(month)
year=now.year
print(year)
day=now.day
print(day,month,year)
if (year%400!=0) and (year%100==0) or (year%4==0):
        print("is a leap year")
else:
    print("not a leap year")