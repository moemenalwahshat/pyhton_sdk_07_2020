""" lambda ex1 """
# Sum = lambda num1 , num2 : num1 + num2 
# print(Sum(2,3))

"""lambda ex2"""
# fun = lambda n: n * n
    
# doubler = fun
# triple = fun

# print(doubler(2))
# print(triple(3))

"""lambda ex3"""
# isEven = lambda num : num%2 == 0

# print(isEven(6))
# print(isEven(3))
 
""" recusion example """
def power(base ,index):
    if index == 0:
        return 1 
    else :
        return base*power(base ,index-1)
print(power(2,4))        

