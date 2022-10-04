#Date: 26/9/2022
import math
import sys
######################################################################
#check if x is a prime number or not
# x is a composite number if it can be divided by an integer y(!=1) smaller than x.
def isPrimeNumber(x: int) -> bool:
    # when x is 1
    if (x==1):
        return False
    # when x is greater than 1
    for y in range(2, x):
        if (x%y==0):
            return False
    return True
    
#print prime numbers between a and b (inclusive)
def showPrimeNumbers(a: int, b: int):
    print("prime numbers between ", a, " and ", b, ":")
    for x in range(a, b+1):
        if (isPrimeNumber(x)):
            print(x, end=", ")

######################################################################
showPrimeNumbers(1, 100)
