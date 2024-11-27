from os import system
from time import sleep
from threading import Thread as T

def clear():
    return system("clear")
    
display = 0
screen = ""
curs1 = "_"
curs2 = " "
cursB = True
screen += curs2
On = True

def outputC():
    while On:
        global cursB, screen, display
        
        
        print("Screen:", screen)
        print("Output:", display)
        sleep(0.5)
        
        clear()

def inputC():
    global screen
    while On:
        inp = input()
        screen += inp
        inp = ""
        
Tin = T(target = inputC, args = ())
Tout = T(target = outputC, args = ())

Tout.start()
Tin.start()
