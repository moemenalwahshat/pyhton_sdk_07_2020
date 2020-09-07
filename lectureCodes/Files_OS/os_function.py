# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:24:51 2020

@author: user2
"""

import os 
os.chdir("\\")
print(os.getcwd())
l =os.listdir()
l2 = os.listdir(r"C:\Users\user2\Desktop")
os.chdir("C:\\Users\\user2\\Desktop")
# os.mkdir("new folder")
# os.renames("new folder", "a")
# os.rename("b", "1" )
# os.rmdir("b\\1")
os.removedirs("b\\1")
