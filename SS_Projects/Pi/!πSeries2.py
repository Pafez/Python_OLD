from os import system as sys
from time import sleep as wait

def fact(n):
    a = 1
    for i in range(n):
        a *= i+1
        
    return a

def sp(n):
    a = ((fact(4*n))*(1103 + 26390*n))/(((fact(n))**4)*(396**(4*n)))
    return a
    
x = 0
itert = 0
    
while True:
    x += sp(itert)
    x1 = x*((8**(1/2))/9801)
    
    π = 1/x1
    
    wait(1)
    sys("clear")
    print("Iteration:", itert, "\nπ =", π)
    
    itert += 1

