run = False

import display, random
from time import sleep
from os import system

def clear():
    return system("clear")

display.on = "0"
display.off = " "

screen = display.Display(30,60)

def main():
    
    

while run:
    clear()
    screen.show()
    sleep(0.1)
    
    
