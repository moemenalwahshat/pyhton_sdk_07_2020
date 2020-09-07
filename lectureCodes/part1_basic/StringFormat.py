# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:09:53 2020

@author: user2
"""

inp = input("enter text")
out= ""
for i in range(0,len(inp)) :
    if inp[i-1] == "." :
        out +="\n"+inp[i].upper()
        
    elif inp[i-1] == "," :
        out += " "+ inp[i].upper()
        
    else :
        out+= inp[i]
print(out)        
    
