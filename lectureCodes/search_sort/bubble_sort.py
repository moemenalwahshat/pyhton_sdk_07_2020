# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:12:17 2020

@author: user2
"""

def bubble(l) :
    n= len(l) 
    
    for i in range (0,n) :
        isOrder ="true"
        for j in range (0,n-i-1)  :
            if l[j] > l[j+1] :
                l[j],l[j+1] = l[j+1],l[j]
                isOrder ="false"
        if isOrder == "true":
                break 
    return l 
print  (bubble([8,2,4,6,5]))    
print  (bubble([8,5,4,6,2]))   
                
                
                
                
            