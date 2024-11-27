import display
from os import system as sys
from time import sleep as wait

display.off
display.on

screen = display.Display(10,20)

cp = [5,10]
screen.turn(cp[0],cp[1])

def move(row, column, comm):
    if comm == "d": 
        screen.custe(row, column, row, column+1)
        return "cp[1] += 1"
    elif comm == "a":
        screen.custe(row, column, row, column-1)
        return "cp[1] -= 1"
    elif comm == "s":
        screen.custe(row, column, row+1, column)
        return "cp[0] += 1"
    elif comm == "w":
        screen.custe(row, column, row-1, column)
        return "cp[0] -= 1"

sys("clear")
screen.show()
while True:
    inp = input()
    if inp in list("asdw"):
        try:
            exec(move(cp[0],cp[1],inp))
        except Exception as e:
            print(e)
            
    sys("clear")
    screen.show()
            
    
            

