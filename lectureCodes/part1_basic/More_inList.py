# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:43:44 2020

@author: user2
"""
""" call by refrance in list """
# def testList (l1):
#     string = "welcome"
#     for i in string:
#         # l1.append(i)
#         l1+="hi"
#     print(id(l1))   
#     return l 

# l = [1,2,3]
# l2=[4,5]
# print(l)
# rt= testList(l)
# print(l)
# print(id(l))

# print("**************************")
# print(l2)
# rt= testList(l2)
# print(l2)
# print(id(l2))
# """ call by refrance in string """


# def testString (s1):

#     s1+="hi"
#     print(s1)
#     print(id(s1))   
#     return s1

# s= "hi"
# print(s)
# rt= testString(s)
# print(s)
# print(id(s))


""" call by refrance in tuble """


def testtuble (t1):

    t1*=2
    print(t1)
    print(id(t1))   
    return t1

t= ("hi",)
print(t)
rt= testtuble(t)
print(t)
print(id(t))



""" for with list """
""" way 1"""
# list1 = ["1",'2',"3"] 
# list2 = ["a","b" ,"c"]
# list3 = [i + j for i in list1 for j in  list2]
# print(list3)


# """ way 2 """
# l3= []
# for i in list1 :
#     for j in list2:
#         l3.append(i+j)
# print(l3)        

