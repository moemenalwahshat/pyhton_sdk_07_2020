# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:50:34 2020

@author: user2
"""

class dog :
    plyer_num = 0 
    def __init__(self , n , c , eColor,l=0,h=0):
        dog.plyer_num+=1 
        self.name =n
        self.color = c
        self.length = l
        self.hight = h
        
    def info(self) :
        print(dog.plyer_num ,"name : " , self.name , "color : " , self.color , "length : " , self.length ,  "hight : " , self.hight) 
    def chnage_color (self ,color) :
        self.color = color
        return self.color
d1 =dog("rex",["red","blue","black"],"pink",20,30)
d1.info()
d2 = dog(n="rex" , c= ["red","black"],eColor= "pink")
d2.info()
d1.chnage_color("black")
d1.info()




