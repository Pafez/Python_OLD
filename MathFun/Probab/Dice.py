import random

print("Enter 'r' to roll the dice. \nEnter 's' to reset the number of sides. \nEnter 'esc' to exit.")
ex = "no"
while 1 == 1:
    mn = 1
    sides = int(input("How many sides should the dice have? → "))
    if sides == 0 or sides < 0:
        print("Mate, are you okay?")
    else:
        mx = sides
    
        while 1 == 1:
            c = input("")
            if c == "r":
                print ("You rolled", random.randint(mn,mx))
            elif c == "s":
                break
            elif c == "esc":
                ex = input("Are you sure you want to exit? Enter 'yes' or 'no'.")
                if ex == "yes":
                    break
                elif ex == "no":
                    print("Okay, please continue...")
                else:
                    print("Invalid Syntax")
            else:
                print("Invalid Command!")
        if ex == "yes":
            print("Hope You Enjoyed, Goodbye!")
            break
            

