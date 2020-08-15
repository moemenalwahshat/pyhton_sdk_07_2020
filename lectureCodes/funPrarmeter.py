#h = int(input("h =  "))
#w = int(input("w =  "))

"""without return"""  
#def area(h , width):
#    a = h*width
#    print("area= ",a)
#area(5,6)    

"""with return"""
#def area(h , width):
#    a = h*width
#    return a
#returnedValue = area(5,6)  

""" EX1"""
#def returnWelcome():
#    return "welcome"
#print(returnWelcome())

""" EX2"""
#def returnAge():
#    age = int(input("enter age"))
#    return age 
#age = returnAge()
#print(age)    
    
""" EX3"""
#def returnParameter(x ,num= 0):
#    print("num= ",num) 
#    print("x= ",x)
#returnParameter(5)

"""calculate area of Trapezoidal 1"""
#b1 = 30
#b2 = 20
#h = 10
#def tArae(b1= 0 ,b2 = 0,h=1 ):
#    if b1 == 0 and b2 == 0 and h == 0:
#        print("no value")
#     
#    area= ((b1+b2)/2)*h
#    print("area= ", area)
#    
#tArae() # no vlaua .. area = 0 
#tArae(2,3)  # 2.5
#tArae(h= 5 , b1 = 6 , b2 = 8) #35

"""calculate area of Trapezoidal """
#b1 = 30
#b2 = 20
#h = 10
#def tArae(b1= 0 ,b2 = 0,h=0 ):
#    if b1 == 0 and b2 == 0 and h == 0:
#        print("no value")     
#    else : 
#        area= ((b1+b2)/2)*h
#        return area
#    
#a= tArae() # no vlaua .. area = 0 
#b = tArae(2,3)  # 2.5
#c = tArae(h= 5 , b1 = 6 , b2 = 8) #35
#print(a,b,c,sep= "\n ")


        
    
    
