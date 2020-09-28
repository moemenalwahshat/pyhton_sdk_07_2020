# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:37:23 2020

@author: user2
"""

t1 = ("a" ,"b","c")
t2 = ("a" ,"b","c",("a" ,"b","c"))
t3 =(1,2,3)
t1[0]="m" # error

n= (5)
print(type(n))
n= (5,)
print(type(n))
n=()
print(type(n))
print(t1+t2)
print(t1*3)
print(t1 in t2)
for i in t1:
    print(i)



""" set """
# s = {1,"a",2,"b"}

# # print(s[0])
# for i in s :
#     print(i)
# s.add("hi")   
# print(s) 
# print("\n\n") 
# s.update(["ab","cv"])
# print(s)
# s.update(["ab","cv"]) # add and update ignore duplicate
# print(s)
# print(len(s))
# s.discard("cv")
# print(s)
# # s.remove("cv") #error
# # print(s)
# print(s.pop())
# print(s)
# s.clear()
# print(s)
# del(s)
# #print(s) undefiened

""" set bulit-in method  """
s1 = {1,2,3}
s2 = {"a","b","c"}

# s2.update(s1)
# print(s2)
# s3 = s1.union(s2)
# s4 =s1|{1,"a"} # union
# print(s4)
s5 =s1
s5.add(5)
s1.add(6)
print(s5 ,"\n",s1)
print(id(s1),"\n",id(s5))

s6 = s1.copy()
print(s6 ,"\n",s1)
print(id(s1),"\n",id(s6))





