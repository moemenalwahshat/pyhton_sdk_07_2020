# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:16:52 2020

@author: user2
"""
""
""" string built in method """
"""# capitalize"""

# s ="created on Sat Aug 22 16:16:52 2020 "
# sCap = s.capitalize()
# print(sCap) 
# print(s.count("e", 0 , len(s)))

# def cap(s):
#     x= ord(s[0])
#     y = str(chr(x-32))
#     sCap= y+s[1:]
#     return sCap
# print(cap("hi"))   

"""#max min"""
# s1 = "wlecome" 
# s2 = "148910"
# s3 = "abf325B"
# print( max(s1)  )
# print( max(s2)  )       
# print( max(s3)  )

# print( min(s1)  )
# print( min(s2)  )       
# print( min(s3)  )

"""#find : return the index of char if found else return -1 mean not found """
# s1 = "wlecome*"    
# print(s1.find("n")) 
# print(s1.find(""))

# def findChar (s,c) :
#     for i in s :
#         if i == c:
#             return s.index(i)
            
#     else :
#             return -1
# print(findChar(s1,'e'))    
# print(findChar(s1,'+')) 
 
# print(s1.index('n'))
# print(s1.index("w" ,1 , (len(s1)-1)) )  
# print(s1.find("w" ,1 , (len(s1)-1)) )

""" example """
# s = "  string Built IN method "
# s2 = "hi"
# print(s.upper())
# print(s.lower())
# print(s.isalnum())
# print(s2.isalpha())
# print(s.isalpha())
# print(s.join"1))

# print(s.replace("m", "f"))
# print(s.split())

""" split """
# s1 = "  string Built IN method "
# l1 = s1.split()
# print(type(l1), l1 ,sep= "\n")

# s2 = "welcome here e"
# l2 = s2.split('e')
# print(l2)

""" split build """

# def splitNew(string,sep) :
#     l= []
#     j =0
#     for i in range(0,len(string)) :
#         if string[i] == sep :
#             l.extend(string[j:i]) 
#         j = i  
#         if(string[i] == sep and i== len(string)-2 ) :
#             l.extend(string[j:i+1]) 
            
#     return l   

# print(splitNew("herem" ,"e"))        
 
           
    
           
        
        
    
    

        
        
   
        
            
       
    