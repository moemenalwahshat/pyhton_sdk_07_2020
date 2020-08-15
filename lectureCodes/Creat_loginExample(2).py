# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:05:23 2020

@author: asf
"""

def facebook():
    userName=""
    password=""
    
    def login():
         userinput =input("user name :")
         passwordinput = input("password :") 
         if userinput == userName and passwordinput == password:
             print("welcome here ")
         else :
             print("username or password wrong ! ")
    def create() :
         
        nonlocal userName
        userName =input("user name :")
        nonlocal password
        password = input("password :") 
        login()
    def checkAge():
        age = int(input("enter your age"))
        if age >=18:
            print("ok you can")
            create()
        else:
            print(" you can't")
    checkAge()        
   
    
facebook()
         
         
         
        