def draw():#creation
    num = 1
    for i in range(1,5):
        for j in range (0,i):
            print(num,end="")
            num+=1
        print()    
draw()#calling        