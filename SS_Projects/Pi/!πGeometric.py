from random import randint as rng
from os import system as sys
from time import sleep

def sqr(n):
    return n**(1/2)
    
z = sqr(2)
itert = 0

while True:
    z = sqr(2 + z)
    zv = sqr(2 - z)
    
    π = zv*(2)**(itert+3)
    if π >3.15:
        break
    sleep(1)
    sys("clear")
    
    print("Iteration:", itert)
    print("π =", π)
    
    itert += 1
