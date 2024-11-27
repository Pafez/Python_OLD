a = int(input("Enter the number you want to factor → "))

if a == 1:
    print(1)
elif a < 0:
    print(-1)
    b = -a
    while 1 < b:
        for i in range(2, int(b+1)):
            if (b % i) == 0:
                print(i)
                b = b/i
                break
else:
    b = a
    while 1 < b:
        for i in range(2, int(b+1)):
            if (b % i) == 0:
                print(i)
                b = b/i
                break