from Pafez import *
from random import randint
from os import system as sys

s = 0
t = 0
while True:
    print(s/t)
    x = randint(1,6)
    y = randint(1,6)
    
    if y<x:
        s += 1
        x = y
    t += 1
    sys("clear")
