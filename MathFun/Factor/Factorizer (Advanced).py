n = int(input("Enter the number you want factors of → "))
if n % 2 == 0:
    for i in range(1,n//2 + 1):
        if (n % i) == 0:
            print(i)
elif n % 3 == 0:
    for i in range(1,n//3 + 1):
        if (n % i) == 0:
            print(i)
elif n % 5 == 0:
    for i in range(1,n//5 + 1):
        if (n % i) == 0:
            print(i)
elif n % 7 == 0:
    for i in range(1,n//7 + 1):
        if (n % i) == 0:
            print(i)
elif n % 11 == 0:
    for i in range(1,n//11 + 1):
        if (n % i) == 0:
            print(i)
elif n % 13 == 0:
    for i in range(1,n//13 + 1):
        if (n % i) == 0:
            print(i)
elif n % 17 == 0:
    for i in range(1,n//17 + 1):
        if (n % i) == 0:
            print(i)
elif n % 19 == 0:
    for i in range(1,n//19 + 1):
        if (n % i) == 0:
            print(i)
print(n)