


#prime number in tow way : 
#1 using for else 
print("Prime numbers between", 20, "and", 70, "are:")

for num in range(30, 100):
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#2 using variable as a flag 
flag = "prime"
for num in range(30, 100):
       for i in range(2, num):
           if (num % i) == 0:
              flag = "not prime"  
       if flag ==  "prime":
           print (num)
       else:
           flag = "prime"
       