import display
from os import system
from time import sleep

run = True
play = True
screen = display.Display(30,60)

px = screen.row//2
py = screen.column//2


pre = """Enter 'Play' to start the game.
Enter 'Manual' to know how to play.
Enter 'Esc' anytime to quit the game.""" 
thanks = "Thanks for playing my game."
manual = """"""

def clear():
    return system("clear")
    
clear()
while run:
    print(pre)
    nav = input()
    clear()
    if nav.lower() == "play":
        while play:
            screen.turn(px, py)
            screen.show()
            do = input()
            if do == "w":
                screen.turn(px, py)
                px -= 1
            elif do == "s":
                screen.turn(px, py)
                px += 1
            elif do == "d":
                screen.turn(px, py)
                py += 1
            elif do == "a":
                screen.turn(px, py)
                py -= 1
                
            if px < 1:
                px = 30
            elif px > 30:
                px = 1
            if py < 1:
                py = 30
            elif py > 30:
                py = 1
            
            
            
            elif do.lower() == "menu":
                play = False
            elif do.lower() == "esc":
                play = False
                run = False
                print(thanks)
            
            clear()
    
            

