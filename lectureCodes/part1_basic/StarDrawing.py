# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 02:51:11 2020

@author: asf
"""
row = int(input("number of row = "))
for i in range(1,row+1):
    for x in range(0,i):
        print("*",end="")   
    print("")        