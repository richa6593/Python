'''
#the Factorial of a Number Using Recursive approach


def factorial(n):

 return 1 if (n==1 or n==0) else n*factorial(n-1)

num=5
print("Factorial of ",num,"is",factorial(num))
'''


#the Factorial of a Number Using using In-built function 
import math
def factorial(n):
    return(math.factorial(n))
    
num=5
print("Factorial of ",num,"is",factorial(num))
    