# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:12:16 2020

@author: user2
"""
# s=("3. os.error: All functions in this module "+ 
# "raise OSError in the case of invalid or "+
#  "inaccessible file names and paths, or other arguments "+
#  "that have the correct type, but are not accepted "+
#  "by the operating system. os.error is an alias for built-in OSError exception.")
# f = open("C:\\Users\\user2\\Desktop\\t1.txt","w")
# f.write(s) 
# f.close()

# f= open("C:\\Users\\user2\\Desktop\\t1.txt","r")
# s1=f.read()
# f.close()
# print(s)     

# f = open("t1.txt","w")
# f.write(s) 
# f.close()
""" read lines """
# s=("3. os.error: All functions in this module \n"+ 
# "raise OSError in the case of invalid or \n"+
#  "inaccessible file names and paths, or other arguments\n "+
#  "that have the correct type, but are not accepted\n "+
#  "by the operating system. os.error is an alias for built-in OSError exception.")

# f= open("C:\\Users\\user2\\Desktop\\t2.txt","w")
# f.write(s) 
# f.close()
# f= open("C:\\Users\\user2\\Desktop\\t2.txt","r")
# # x = f.read()
# for l in f :
#     print(l)
    
""" read of char """    
s=("3. os.error: All functions in this module \n"+ 
"raise OSError in the case of invalid or \n"+
  "inaccessible file names and paths, or other arguments\n "+
  "that have the correct type, but are not accepted\n "+
  "by the operating system. os.error is an alias for built-in OSError exception.")

f= open("C:\\Users\\user2\\Desktop\\t2.txt","w")
f.write(s) 
f.close()
f= open("C:\\Users\\user2\\Desktop\\t2.txt","r")
x = f.read(10)
print(x)
y= f.readlines(2)
f.close()
print(y)

