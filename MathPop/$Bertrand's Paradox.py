from os import system as sys
from time import sleep
from random import randint


r = 344
s = ((r**2 - (r/2)**2)**(1/2))*2
t = 0
p = 0
ramp = 1000

while True:
    sys("clear")
    
    r1 = randint(-ramp*r,ramp*r)/ramp
    r2 = randint(-ramp*r,ramp*r)/ramp
    r3 = randint(0,1)
    r4 = randint(0,1)
    
    p1 = [r1, (-1)**(r3)*(r**2-r1**2)**(1/2)]
    p2 = [r2, (-1)**(r4)*(r**2-r2**2)**(1/2)]
    
    l = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)
    
    if l > s:
        p += 1
    t += 1

    prob = p/t
    print("P[l>s] =", prob)

