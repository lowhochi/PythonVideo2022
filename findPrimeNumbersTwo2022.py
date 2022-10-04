#Date: 4/10/2022
import math
import sys
import time
######################################################################
#find prime numbers between 1 and N(=20000) more efficiently
#idea: iterate over the numbers from 1 to N
#      store any prime numbers we encounter
#      get rid of composite numbers

"""
iterate x over [2, 3, 4, 5, 6, 7, ,8, 9, 10, ... , 20_000]
(x==2)  visited[2]=False -> 2 doesn't have a factor(>1) smaller than 2 -> 2 is a prime
        find out all multiples 2*y(<=N) of 2 -> mark visited[2*y]=True
        
(x==3)  visited[3]=False -> 3 doesn't have a factor(>1) smaller than 3 -> 3 is a prime
        find out all mulitples 3*y(<=N) of 3 -> mark visited[3*y]=True
        
(x==4)  visited[4]=True -> skip x=4 (composite) ...
continue until x = 141 = floor(sqrt(N))

when x > 141==floor(sqrt(20_000)),
    if x has been visited -> x is composite
    if x hasn't been visited -> x must be a prime
    *if x = x1*x2 at this point, either x1 or x2 must be <= 141
    ** therefore x must have been visited

"""

def findPrimeNumbers02(N: int):
    #visited = [False(0), False(1), False(1), ..., False(N)]
    #visited[x] = True if the number x is composite (skip the number x)
    visited = [False for x in range(0, N+1)]
    visited[0] = True #by default
    visited[1] = True #by default
    #myList stores prime numbers
    myList = []
    #sqrtN = largest possible integer which is <= sqrt(N) 
    sqrtN = math.floor(math.sqrt(N))

    for x in range(2, sqrtN+1):
        # visited[x] => x is known to be a composite number
        if (visited[x]):
            continue
        # not visited[x] =>x is an unvisited prime
        if (~visited[x]):
            myList.append(x)
        # clear all multiples of x which are smaller than or equal to N
        # make sure that the multiples x*y <= N
        y0 = N//x #so that x*y0 <= N
        for y in range(1, y0+1):
            visited[x*y] = True
   
    # handle all integers sqrtN < x <= N
    for x in range(sqrtN+1, N+1):
        if (~visited[x]):
            myList.append(x)
    return myList

######################################################################
#use the old method to find prime numbers between 1 and 20_000
def isPrimeNumber(x: int)->bool:
    if (x==1):
        return False
    for y in range(2, x):
        if (x%y==0):
            return False
    return True;

def findPrimeNumbers01(a: int, b: int):
    u = []
    for x in range(a, b+1):
        if (isPrimeNumber(x)):
            u.append(x)
    return u

######################################################################
#comparing these two methods
def comparison():
    print("find prime numbers between 1 and 20,000 by method01 :")
    start01 = time.time()
    u = findPrimeNumbers01(1, 20_000)
    end01 = time.time()
    print("there are {:} prime numbers".format(len(u)))
    print("elapsed time: {:.5f} seconds".format(end01-start01))
    print("")
    # # # # #
    print("find prime numbers between 1 and 20,000 by method02 :")
    start02 = time.time()
    v = findPrimeNumbers02(20_000)
    end02 = time.time()
    print("there are {:} prime numbers".format(len(u)))
    print("elapsed time: {:.5f} seconds".format(end02-start02))
    print("")
    return v
    # # # # #

def printPrimeNumbers(v):
    count = 0
    for x in v:
        count += 1
        if (count%10==0):
            print(x, end="\n")
        else:
            print(x, end=", ")
    return

######################################################################
if (__name__ == "__main__"):
    v = comparison()


