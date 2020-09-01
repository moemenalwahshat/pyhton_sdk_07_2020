# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:23:37 2020

@author: user2
"""

""" dictionary"""
dec = {"a": ["ahmad",'Amer'] , "b" : "bara'a" ,"c": [ "cat" , "carmel"]  }
# print(dec)
# print(dec["c"])
# print(dec.get("c"))
# print(dec.keys())
# print(dec.values())

Convert_list = list(dec)
# print(Convert_list)
comvet_item = dec.items()
# print(comvet_item)
# print(type(comvet_item))
dec["b"] = 12
print(dec["b"])

dec["a"].append('1')
print(dec["a"])
# dec.clear()
# print(dec)
""" dec of keys"""
x = ['key1', 'key2', 'key3']
y = [0,1,3]
for i in range (0,len(y)) :
    thisdict = dict.fromkeys(x, y[i])
    print(thisdict)






