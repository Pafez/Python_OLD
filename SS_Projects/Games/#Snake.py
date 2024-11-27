import display_v2 as disp
from random import randint as ran
from time import sleep as wait
from threading import Thread as T

screen = disp.Display(30,60)
blockade = disp.Char(5,6,"#")
snakeHead = disp.Char("&")
snakeBody = disp.Char("@")
snake = [snakeHead.strc]
direction = "x+"
inp = ""

def getUserInp():
    global inp
    while True:
        inp = input()
    
def run():
    while True:
        
        if inp == "w":
            actr = snakeHead.row
            actc = snakeHead.column
            direction = "y+"
        elif inp == "d":
            actr = snakeHead.row
            actc = snakeHead.column
            direction = "x+"
        elif inp == "s":
            actr = snakeHead.row
            actc = snakeHead.column
            direction = "y-"
        elif inp == "a":
            actr = snakeHead.row
            actc = snakeHead.column
            direction = "x-"
            
        

tMain = T(target = run, args = ())
