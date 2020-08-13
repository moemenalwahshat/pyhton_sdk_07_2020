""" test for global and local """

#x= "outside"
#def test ():
#    x= "inside"
#    print(x)
#print(x)
#test()
#print(x)    
   

""" tset for global ,enclosing local and local """

#y= "global"
#def test():
#    y = "enclose local"
#    print(y)
#    def test2():
#        y="local"
#        print(y)
#    test2()    
#print(y)#global
#test()#enclose #local

""" more than tow nested functions  """

#def test1():
#    y="enclose local"
#    def test2():
#       y= "local"
#       def test3():
#           print(y)
#       test3()    
#    def test4() :
#          print(y)
#    test2()
#    test4()
#test1()  

""" using the global keyword """

#y= "global"
#def test():
#    global y 
#    y = "i'm global editing from enclose scope"
#    print(y)
#    def test2():
#        y="local"
#        print(y)
#    test2()    
#print(y)#global
#test()#enclose #local   
#print(y)#enclose local



""" using the global keyword in both scope """

#y= "global"
#def test1():
#    global y 
#    y = "i'm global editing from enclose scope after calling tset1"
#    print(y)
#    def test2():
#         global y 
#         y = "i'm global editing from local scope after calling tset2"
#         print(y)
#    test2()    
#print(y)
#test1() 
#print(y)#have the final assignment value
#y = "i'm global editing from global scope "
#print(y)

""" using the nonlocal """

#y= "global"
#def test(): 
#    y = "enclose local"
#    print(y)
#    def test2():
#        nonlocal y 
#        y="i'm enclose local after editting from local scope"
#        print(y)
#    test2()
#    print(y)
#    
#print(y)#global
#test()#enclose #local#local

""" using the nonlocal in nested funtion """

#y= "global"
#def test(): 
#    y = "enclose local"
#    print(y)
#    def test2():
#        nonlocal y 
#        y="i'm editing in local"
#        print(y)
#        def test3():
#            print(y)
#        test3()    
#    test2()
#    print(y)
#    
#print(y)#global
#test()#enclose #local#local
