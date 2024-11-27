from os import system as sys
from time import sleep as wait

t = 426880*(10005)**(1/2)
x = 0

def fact(n):
    a = 1
    for i in range(n):
        a = a*(i+1)
        
    return a


def d(n):
    p = ((fact(6*n))*(545140134*n + 13591404))/(((fact(n))**3)*(fact(3*n))*(-640320)**(3*n))
    return p

itert = 0

while True:
    x += d(itert)
    π = t/x
    
    wait(1)
    
    sys("clear")
    print("Iteration:", itert)
    print("π =", π)
    
    itert += 1
