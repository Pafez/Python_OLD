# Success #

import display
from time import sleep
from os import system
display.on = "0"
on = display.on
off = display.off

def clear():
    return system("clear")
    
clear()
    
screen = display.Display(30, 60)

screen.row_turn(2)
screen.row_turn(3)
screen.column_turn(4)
screen.column_turn(5)

counter = 0

while True:
    print("Gen:",counter)
    
    screen.show()
    sleep(0.005)
    
    
    for i in range(2, screen.row):
        for j in range(2, screen.column):
            neighbours = [screen.state(i+1,j+1),screen.state(i+1,j-1),screen.state(i-1,j+1),screen.state(i-1,j-1),screen.state(i+1,j),screen.state(i,j-1),screen.state(i,j+1),screen.state(i-1,j)]
            n_counter = neighbours.count(on)
            if screen.state(i, j) == on:
                if n_counter > 3 or n_counter < 2:
                    screen.turn(i, j)
            elif screen.state(i, j) == off:
                if n_counter == 3:
                    screen.turn(i, j)
            
   
    counter += 1
    
    clear()
                    

