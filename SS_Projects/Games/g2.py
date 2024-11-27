while 1 == 1:
    print ("\nEnter 'Start' to start the game.")
    print ("Enter 'Esc' to exit")
    go = input("")
    if go == "Start" or go == "start":
        print ("Game STARTED")
        x = 0
        y = 0
        z = 0
        while -1000 <= x <= 1000 and -1000 <= y <= 1000 and -1000 <= z <= 1000:
            print ("Co-ordinates:",x, y, z)
            c = input("")
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
            else:
                print ("Unknown command")
        else:
            print ("Out of the region")

    elif go == "Esc" or go == "esc":
        print ("\nSee you next time! :)")
        break
    else:
        print ("Invalid Syntax")
