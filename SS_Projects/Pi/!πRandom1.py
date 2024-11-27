from random import randint
from os import system
from time import sleep

def factor(n):
    facts = []
    for i in range(2,n//2 + 1):
        if (n % i) == 0:
            facts.append(i)
    facts.append(n)
    return set(facts)
    
cp = 0
tn = 0
itert = 0

while True:
    r1 = factor(randint(1,100))
    r2 = factor(randint(1,100))
    
    inter = r1.intersection(r2)
    
    if inter == set():
        cp += 1
    tn += 1
    
    system("clear")
    print("Iteration:", itert)
    if cp>0:
        π = (6*tn/cp)**(1/2)
        print("π =", π)
    
    itert += 1
