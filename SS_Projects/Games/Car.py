"Car" "version_0.3"



import random
speed = 0
sl = 9
ps = 0

while True:
    print("Enter 'start' to start the game. \nEnter 'm' to open the manual. \nEnter 'esc' to exit.")
    
    g = input("")

    if g == "start":
        print("The game is now started.")
        
        while True:
            print("Speed:",speed,"kmph")
            print("Speed Limit:",sl*10,"kmph")
            
            
            
            
            c = input("")
            if c == "w":
                speed = speed + 10
            elif c == "s":
                speed = speed - 10
            
            
            if ps > speed and sl*10 < speed:
                print("Police caught you!")
                print("Game over!")
                speed = 0
                sl = 9
                ps = 0
                res = input("Press enter to return to the menu.")
                break
            
            if sl*10 < speed:
                print("Police is after you as your speed was more than the speed limit.")
                ps = random.randint(5,speed)
                print("The police is after you at",ps,"kmph")
                
                
            if speed > 0 and sl*10 > speed:
                
                probabs = (0.5, 0.14, 0.14, 0.12, 0.1) 

                def roll(massDist):
                    randRoll = random.random()
                    sum = 0
                    result = 0
                    for mass in massDist:
                        sum += mass 
                        if randRoll < sum:
                            return result
                        result+=1 
                xe = roll(probabs)
                if xe == 1:
                    print("Turn right")
                    xc = input("")
                    if not xc == "d":
                        print("You crashed!")
                        print("Game Over!")
                        speed = 0
                        sl = 9
                        ps = 0
                        res = input("Press enter to continue to the menu.")
                        break
                        
                elif xe == 2:
                    print("Turn left")
                    xc = input("")
                    if not xc == "a":
                        print("You crashed!")
                        print("Game Over!")
                        speed = 0
                        sl = 9
                        ps = 0
                        res = input("Press enter to return to the menu.")
                        break
                        
                elif xe == 3 and ps == 0:
                    sl = random.randint((speed/10 - 1),12)
                    print("New speed limit is",sl*10,"kmph")
                        
                elif xe == 4:
                    print("Cracked road, JUMP!")
                    xc = input("")
                    if not xc == "p":
                        print("Your car fell into the river!")
                        print("Game over!")
                        speed = 0
                        sl = 9
                        ps = 0
                        res = input("Press enter to return to the menu.")
                        break
            if speed == -130:
                print("Congrats, you found the easter egg of this game which is the first easter egg of all of my games. I am S. H. Pafez aka Shah Tozen. And thanks for playing my game. (Don't forget to enter '13' in-game)")
            
            elif c == "13":
                print("GG")
            
            if c == "menu":
                print("Returning to the menu...")
                break           
            
    elif g == "m":
        print("This is the manual for this game")
        print("\nControls - \n w → Increases speed \n s → Decreases speed \n d → Turns right (When needed) \n a → Turns left (When needed) \n p → Jumps (When needed)")
        print("\nNavigation - \n Enter 'esc' anytime to exit. \n Enter 'menu' in-game to quickly return to the menu, your game progress will be saved automatically.")
        print("\nMission - \n Survive different challenges through actions. Do not drive more than the speed limit. Doing so may cause a direct Police patrol on you. If that happens, try not to drive less than the speed of the Police.")
        input("\nEnter to return to the menu.")
        
    elif g == "esc":
        print("Thanks for playing my game.")
        break
        
                        
            

