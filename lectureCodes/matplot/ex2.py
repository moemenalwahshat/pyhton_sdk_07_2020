# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:51:07 2020

@author: share
"""


number_customer= int(input("number_customer : "))
dic = {'name' : [] , 'country' : []}
for i in range(0,number_customer) :
    dic['name'].append(input('enter name'))
    dic['country'].append(input('enter country'))
s =set(dic['country'])    
count_of_each_country = []
for i in s :
    count_of_each_country.append(dic['country'].count(i)) 
import matplotlib.pyplot as plt 
fig, axs = plt.subplots(1,2, figsize=(10,3) , sharey=True)
axs[0].bar(list(s),count_of_each_country)
axs[1].bar(list(s),count_of_each_country) 
plt.show()   
