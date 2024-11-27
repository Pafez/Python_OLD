# Success #

import threading as t
from time import sleep as wait
d = 5
k = 0
def t1():
    while True:
        global k
        print(k)
        k += 1
        wait(0.05)
        if d == 1:
            break
            
def t2():
    while True:
        global d
        d = int(input())
        if d == 1:
            break
    
    
T1 = t.Thread(target = t1, args = ())
T2 = t.Thread(target = t2, args = ())

T2.start()
T1.start()