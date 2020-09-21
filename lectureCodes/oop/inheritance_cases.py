# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:54:45 2020

@author: share
"""
""" case one single inharitance """
#class a :
#    x=5
#    def __init__(self):
#        print("hii from a ")
#    def info (self):
#        print("hi")
#class b(a) :
#    def __init__(self):
#        super().__init__()
#        print("hii from b ")
#class c :
#    def __init__(self):
#        super().__init__()
#
#        print("hii from c ")        
#        
#boj = b()

""" case tow hirarchial inharitance """
#class a :
#    x=5
#    def __init__(self):
#        print("hii from a ")
#    def info (self):
#        print("hi")
#class b(a) :
#    def __init__(self):
#        super().__init__()
#        print("hii from b ")
#class c(a) :
#    def __init__(self):
#        super().__init__()
#
#        print("hii from c ")        
#        
#boj1 = b()
#obj2 = c()

""" case three multiLevel inharitance """
#class a :
#    x=5
#    def __init__(self):
#        print("hii from a ")
#    def info (self):
#        print("hi")
#class b(a) :
#    def __init__(self):
#        super().__init__()
#        print("hii from b ")
#class c(b) :
#    def __init__(self):
#        super().__init__()
#
#        print("hii from c ")        
#        
#boj1 = b()
#obj2 = c()

""" case one multiple inharitance """
class a :
    x=5
    def __init__(self):
        print("hii from a ")
    def info (self):
        print("hi")
class b :
    def __init__(self):
        super().__init__()
        print("hii from b ")
class c(a,b) :
    def __init__(self):
        super().__init__()

        print("hii from c ")        
        
boj = c()

