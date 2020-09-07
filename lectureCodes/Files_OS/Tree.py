# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:02:56 2020

@author: user2
"""

import os 
os.chdir("\\")
list_curent =  os.listdir()
path = os.getcwd()
inp = input ("file name : ")
while(1) :
    if inp in list_curent :
        path+= "\\"+inp
        os.chdir(path)
        list_curent =  os.listdir()
        
        
        
    else :
         print("not found") 
    inp = input ("file name : ")
    print("to exit press Q or q : ")
    if inp == "Q" or inp =="q" :
        print(path)
        break 
        
while(1):    
    
    inp2 = input ("folder nmae to create  or file.type to create : ")
    os.mkdir(inp2)
    input("selsect create folder in same dir or in new one , ")
    # path+= "\\"+inp2
    # os.chdir(path) 
# inp3 = input ("enter name  : ")
# os.mkdir(inp2)

   

