# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:38:21 2020

@author: user2
"""

nameList =[]
countryList = []
number_customer= int(input("number_customer : "))
for i in range(0,number_customer) :
    
    nameList.append((input("name : ")))
    countryList.append((input("country : ")))
s =   set(countryList)  
import pandas as pd

data = pd.DataFrame(s)   
<<<<<<< HEAD
data.to_excel(("C:\\Users\\share\\Desktop\\c.xlsx"),index= 0) 
=======
data.to_excel(("C:\\Users\\user2\\Desktop\\c1.xlsx"),index= 0) 
>>>>>>> c4b77a5c713eead44b7a314f52ab299a152c1fb7

