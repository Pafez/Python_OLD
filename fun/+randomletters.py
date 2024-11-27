from Pafez import rollprob
from time import sleep
from os import system as sys
from say import say
from r256 import init
from random import randint

letts = "abcdefghijklmnopqrstuvwxyz "

letperc = init()

sys("clear")
while True:
    
    msg = ""
    for i in range(randint(0,20)):
        l = rollprob(letperc)
        msg += letts[l-1]
    
    inp = input()
    sys("clear")
    print("User:", inp, "\n")
    print("C:", msg, "\n")

