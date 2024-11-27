import display
from time import sleep
from os import system

def clear():
    return system("cls")

ground = display.Display(10,20)
ground.turn(5,10)
while True:
    
    clear()
    ground.show()
    g = 1
    for i in range(1,11):
        for j in range(1,21):
            if ground.state(i,j) == display.on:
                try:
                    ground.turn(i,j)
                    ground.turn_on(i+1,j+1)
                    g = 0
                    break
                except Exception as e:
                    print(e)
        if g == 0:
            break
    sleep(1)
    

