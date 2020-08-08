
#print("output with break ")
for x in range(1,6):
    if x==3:
        break
    print(x)
#print("output with continue ")

for x in range(1,6):
    if x==3:
        continue
    print(x)
   
#print("output with pass ")
for x in range(1,6):
    if x==3:
        pass
    print(x)


#break with nested loop
for x in "abcd":
      for i in range(1,5):
          if i==3:
             break
          print(i)
      print("outer loop")   

#for else(3 example)
 #Ex1     
for i in range(1,5):
    print(i)
    if(i==2):
        break
else:
    print("if no break happen , i will appear" )              

#EX2
for i in range(1,5):
    print(i)
   
else:
    print(" if no break happen , i will appear" )             
    
#Ex3
for i in range(1,5):
     print(i)
     if(i==0):
        break
   
else:
    print(" if no break happen , i will appear" )        