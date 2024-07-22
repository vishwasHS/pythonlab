# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:55:10 2024

@author: cseweb
"""
class book:
    def __init__(self,name,author,price):
        self.__title=name
        self.__author=author
        self.__price=price
    def display(self):
        if self.__title[0]=='D' or self.__title[0]=='d':
            print("title of the book:",self.__title)
            print("author of the book:",self.__author)
            print("price of the book:",self.__price)
b1=book("python","asd",475)
b=book("Def","efr",123)
b1.display()
b.display()