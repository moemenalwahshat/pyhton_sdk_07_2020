# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:05:23 2020

@author: asf
"""

userName=""
password=""

def create() :
         global userName
         global password
         userName =input("user name :")
         password = input("password :") 
         print("\t\tplz try to login")
         login()
def login():
         
         userinput =input("user name :")
         passwordinput = input("password :") 
         if userinput == userName and passwordinput == password:
             print("\t\twelcome here ")
         else :
             print("username or password wrong ! ")
        

def checkAge():
        age = int(input("enter your age"))
        if age >=18:
            print("ok you can")
#            create()
        else:
            print(" you can't")
    
    
         
         
         
        