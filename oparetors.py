# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:59:36 2020
#
@author: asf
"""
#arathmatic oparetor
num1 , num2  = 55 , 6
s = num1 +num2
sub = num1 - num2
mult = num1 *num2
f_div = num1  / num2
in_div = num1  // num2
p = num1 ** num2
mod = num1 % num2
print ("sum= ", s)
print ("sub= ",sub)
print ("mult= ",mult)
print ("fdiv= ",f_div)
print ("in div = ",in_div)
print ("power ",p)
print ("modulus ",mod)

#input value 
x= complex(input("entaer int value\n "))
print(type(x))

#print formating
fn = input("first name :")
sn = input("second name :")
m , y = input("month of  date :") , input("year of  date :")
print(fn,sn,end= ":")
print(m,y,sep= "\t")
print()