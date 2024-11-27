s=0
while 1==1:
    x = input("")
    

    if x == "start":
        if s == 0:
            print("Your car is now started")
            s = 1
        elif s == 1:
            print("Car is already started")

    elif x == "stop":
        if s == 1:
            print("Your car is now stopped")
            s = 0
        elif s == 0:
            print("Car is already stopped")
    elif x == "exit":
        break