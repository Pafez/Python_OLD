from os import system
from time import sleep
def wait(x):
    return sleep(x)
def clear():
    return system("clear")
clear()
run = True

while run:
    
    print ("\nEnter 'Start' to start the game.")
    print ("Enter 'Esc' to exit")
    print ("Enter 'Manual' to open the manual")
    go = input("")
    clear()
    if go.lower() == "start":
        print ("Game STARTED")
        wait(2)
        x = 0
        y = 0
        z = 0
        i1 = "Wood"
        i2 = "Stone"
        i3 = "Ice"
        i4 = "Dirt"
        i5 = "Glass"
        while -1000 <= x <= 1000 and -1000 <= y <= 1000 and -1000 <= z <= 1000:
            print ("Co-ordinates:",x, y, z)
            print ("Inventory:",i1,i2,i3,i4,i5)
            c = input("")
            clear()
            if c == "w":
                x = x + 1
            elif c == "s":
                x = x - 1
            elif c == "d":
                z = z + 1
            elif c == "a":
                z = z - 1
            elif c == "o":
                y = y + 1
            elif c == "k":
                y = y - 1
            elif c == "esc":
                print ("Thanks for playing my game")
                break
            elif c == "i1":
                print ("Selected",i1)
                e = input("")
                clear()
                if e == "p":
                    print (i1,"placed at",x,y,z)
                elif e == "np":
                    print ("Nothing placed at",x,y,z)
            elif c == "i2":
                print ("Selected",i2)
                e = input("")
                clear()
                if e == "p":
                    print (i2,"placed at",x,y,z)
                elif e == "np":
                    print ("Nothing placed at",x,y,z)
            elif c == "i3":
                print ("Selected",i3)
                e = input("")
                clear()
                if e == "p":
                    print (i3,"placed at",x,y,z)
                elif e == "np":
                    print ("Nothing placed at",x,y,z)
            elif c == "i4":
                print ("Selected",i4)
                e = input("")
                clear()
                if e == "p":
                    print (i4,"placed at",x,y,z)
                elif e == "np":
                    print ("Nothing placed at",x,y,z)
            elif c == "i5":
                print ("Selected",i5)
                e = input("")
                clear()
                if e == "p":
                    print (i5,"placed at",x,y,z)
                elif e == "np":
                    print ("Nothing placed at",x,y,z)
            
            else:
                print ("Unknown command")
        else:
            print ("Out of the region")

    elif go == "Esc" or go == "esc":
        print ("\nSee you next time! :)")
        break
    elif go == "Manual" or go == "manual":
        while True:
            
    
            print ("\nThis is the manual for this game.")
            print ("\nControls: \nForward - w \nBackward - s \nRight - d \nLeft - a \nUpward - o \nDownward - k")
            print ("\nThe 1st co ordinate tells your position in the forward-backward axis. \nThe 2nd co ordinate tells your position in the up-down axis. \nThe 3rd co ordinate tells your position in the right-left axis.")
            print ("\nInventory: \nTo open the inventory - i \nInventory contains the items you have, entering 'i' will let you gain control over it to edit.")
            print ("\nEnter 'esc' anytime to quit the game.")
            mi = input()
            clear()
            if mi.lower() == "back":
                break
            elif mi.lower() == "esc":
                run = False
                break
    else:
        print ("Invalid Syntax")
