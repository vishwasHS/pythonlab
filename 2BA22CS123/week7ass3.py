# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:19:05 2024

@author: cseweb
"""

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name={self.name}\nage={self.age}")
    def __eq__(self,other):
        if isinstance(other,person):
            return self.name==other.name and self.age==other.age
        return False
    
p1=person("asd",12)
p2=person("sd",12)

if p1==p2:
    print("identical")
    p1.display()
else:
    print("not identical")
    
    