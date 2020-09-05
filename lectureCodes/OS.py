# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:51:16 2020

@author: user2
"""
s=("3. os.error: All functions in this module "+ 
"raise OSError in the case of invalid or "+
 "inaccessible file names and paths, or other arguments "+
 "that have the correct type, but are not accepted "+
 "by the operating system. os.error is an alias for built-in OSError exception.")
import os 
print(os.getcwd())
print("****************************\n")
f = open("t3.txt","w")
f.write(s) 
f.close()
os.chdir(r"C:\Users\user2\Desktop")
print(os.getcwd())
f = open("t3.txt","w")
f.write(s) 
f.close()

