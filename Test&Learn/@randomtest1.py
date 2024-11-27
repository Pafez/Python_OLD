from random import randint
from time import sleep
from os import system

def clear():
    return system("clear")

n1 = 0
n2 = 0
np1 = 0
np2 = 0
coun = 0
eqc = [0]
gen = 0

while True:
    clear()
    
    print("Iteration:",gen,"\n")
    print("n1 →",np1,"%")
    print("n2 →",np2,"%\n")
    print("Stops:",eqc)
    
    gen += 1
    
    n = randint(1,2)
    
    if n == 1:
        n1 += 1
    else:
        n2 += 1
    
    if n1 == n2:
        coun += 1
        eqc.append(int(gen/2))
        
    np1 = n1/(n1+n2)*100
    np2 = n2/(n1+n2)*100
    
    
        
    sleep(0.0)

