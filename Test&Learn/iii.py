s = 0

while 1>0:
    a = input("")
    if a == "start":
        if s == 0:
            print("Car is started")
            s = 1
        elif s == 1:
            print("Car is already started")
    elif a == "stop":
        if s == 1:
            print("Car is stopped")
            s = 0
        elif s == 0:
            print("Car is already stopped")
    
    