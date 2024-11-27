def fact(a):
    facts = []
    if a == 1:
        facts.append(1)
    elif a < 0:
        facts.append(-1)
        b = -a
        while 1 < b:
            for i in range(2, int(b+1)):
                if (b % i) == 0:
                    facts.append(i)
                    b = b/i
                    break
    else:
        b = a
        while 1 < b:
            for i in range(2, int(b+1)):
                if (b % i) == 0:
                    facts.append(i)
                    b = b/i
                    break
    
    return(facts)

while True:    
    try:
        inp = int(input("Enter the number you want to factor → "))
        print(fact(inp))
    except:
        try:
            if inp.lower() == "exit":
                break
            else:
                print("Enter an integer")
        except:
            print("Enter an integer")
    

