import matplotlib.pyplot as plt 
import numpy as nm
''' liener'''
# x = [ 1,2,3,4]
# y = [4,6,8,10]
# q1 = plt.plot(x,y , 'go',label = 'eq1' )
# q2 =plt.plot([1,2,3,4] , [5,7,9,11] , '*b', label = 'eq2')
# plt.legend()
# plt.show()
''' 2nd order eq'''
# x1 = range(-40,40)
# y1 = []
# for i in x1 :
#     y1.append(i**2+2*i+2)
# plt.plot(x1,y1) 
# plt.show()  

l =['group1' ,'group2','group3'] 
men = [10,15,35]
women = [6,12,45]
x = nm.arange(0,3)
fig ,s = plt.subplots()
r = s.bar(x,men ,.25,label=',men')
r = s.bar(x+.25,women ,.25,label='women')
s.set_ylabel('score')
s.set_xlabel('score per gruop')
s.set_title('result')
s.set_xticks(x)
s.set_xticklabels(l)
s.legend()
plt.show()
