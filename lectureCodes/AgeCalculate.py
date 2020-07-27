



d= int(input("enter day of date :" ))
m= int(input("enter month of date: " ))
y= int(input("enter year of date : " ))
#compute the age 
dAge = 27-d
mAge = 7-m
yAge = 2020-y
print("your age :")
print(yAge,"year")
if(dAge<0 ):
    dAge = dAge*-1
    print(dAge,"day")
else :
    print(dAge,"day")

    
if(mAge<0 ):
   mAge = mAge*-1 
   print(mAge,"day")
else :
    print(mAge,"day")

    