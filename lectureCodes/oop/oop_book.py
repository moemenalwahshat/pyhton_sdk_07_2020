# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:18:50 2020

@author: share
"""

class book :
    def __init__(self , auther_name,sale_price ,cost_price,title,page):
        self.an = auther_name
        self.sl = sale_price
        self.c = cost_price
        self.t = title
        self.p = page

    def netPrice(self):
        return (self.sl + self.c)
class E_book(book) :
    def __init__(self , auther_name,sale_price ,cost_price,title,page,sizeMB ,downloadSite):
           super().__init__(auther_name,sale_price ,cost_price,title,page)
           self.s = sizeMB
           self.d = downloadSite
    def tax(self) :
        return (.25 * self.netPrice())          
    def printDocument(self):
            print("doc is print")
    def pageSize(self) :
        return (self.s/self.p)        
    
class p_book(book) :
    def __init__(self , auther_name,sale_price ,cost_price,title,page,wight,paperType):
           super().__init__(auther_name,sale_price ,cost_price,title ,page)
           self.wight = wight
           self.pt = paperType
    def cover(self,color):
            print("color :" ,color)
    def tax(self) :
        return (.20 * self.netPrice())            

p1 = p_book("ahmd", 10, 5, "python", 100, 300, "white")
print(p1.netPrice())
print(p1.tax())
p1.cover("red")
