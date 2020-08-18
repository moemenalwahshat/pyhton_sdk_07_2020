#assing value of current date
pd ,pm , py = 17,8,2020
#read value of current date
bd,bm,by =int( input("enter day of birth")),int( input("enter month of birth")),int(input("enter year of birth"))
#calculate number of year 
y = py - by
#test if the person has not complete the previous years in age
if(pm<bm):
    y-=1
    m = 12-(bm-pm)
else:
    m= pm-bm
if(pd<bd):
    m-=1
    if(pm in range(1,8,2) or pm in range(8,13,2) ):
        d = 31-(bd-pd)
    elif ((pm in range(2,7,2) or pm in range(9,12,2)) and pm!=2 ) :
        d = 30-(bd-pd)
    else:
        d = 29-(bd-pd)
       
else:
    d= pd-bd
print("your age : ",y,"years",m,"months",d,"days") 

