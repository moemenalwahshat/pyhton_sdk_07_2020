# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:54:45 2020

@author: share
"""

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
class c(b,a) :
    def __init__(self):
        super().__init__()

        print("hii from c ")        
        
