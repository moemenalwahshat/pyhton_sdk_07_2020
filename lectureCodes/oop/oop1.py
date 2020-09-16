# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:50:34 2020

@author: user2
"""

class dog :
    plyer_num = 0 
    def __init__(self , n , c , eColor,l,h):
        dog.plyer_num+=1 
        self.name =n
        self.color = c
        self.length = l
        self.hight = h

       
d1 =dog("rex",["red","blue","black"],"pink",20,30)

print("the number of plyer = " ,d1.plyer_num)
print(d1.color)

d2 = dog(n="rex" , c= ["red","blue","black"],eColor= "pink",h= 20,l = 30)
print("the number of plyer = " ,d2.plyer_num)
print(d2.color)
print(dog.plyer_num)
# jex =dog()
# print("the number of plyer in dog = " ,jex.plyer_num)
# print("the number of plyer in dog = " ,dog.plyer_num)
# print("the number of plyer = " ,rex.plyer_num)





# d2 =dog()
# d2 =dog()
# d2.name= "rex"
# d2.color=["brown","blue"]
# d2.eyeColor= "green"
# d2.h= 20
# d2.l=10

# print(dog.name , "colrr" , dog.color ,"eye color" , dog.eyeColor , "hight" ,dog.h,  "lenght" , dog.l, "wight " , dog.w )

# print(d1.name , "colrr" , d1.color ,"eye color" , d1.eyeColor , "hight" , d1.h,  "lenght" , d1.l, "wight " , d1.w )
# print(d2.name , "colrr" , d2.color ,"eye color" , d2.eyeColor , "hight" , d2.h,  "lenght" , d2.l, "wight " , d2.w )

