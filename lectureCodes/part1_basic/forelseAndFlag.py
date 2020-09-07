#
#
#
##prime number in tow way : 
##1 using for else 
#print("Prime numbers between", 20, "and", 70, "are:")
#
#for num in range(30, 100):
#       for i in range(2, num):
#           if (num % i) == 0:
#               break
#       else:
#           print(num)
#
##2 using variable as a flag 
#flag = "prime"
#for num in range(30, 100):
#       for i in range(2, num):
#           if (num % i) == 0:
#              flag = "not prime"  
#       if flag ==  "prime":
#           print (num)
#       else:
#           flag = "prime"
#     
#for i in range(2, 5):
#          print("hi")
#               
#else:
#           print("bye")  

s= [1,"a",[1,2,3,4]]
def c (l):
    l[1]= 2
print(s[1])
c(s)
print(s[1])    

a = [10, 20, 30] 
b = [10, 20, 30] 
  
# return the location 
# where the variable  
# is stored 
print(id(a)) 
  
# return the location 
# where the variable  
# is stored 
print(id(b))
#s.join("1")

