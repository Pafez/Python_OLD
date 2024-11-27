l = int(input("Starting number = "))
u = int(input("Ending number = "))

print("Prime numbers between",l, "and",u,"are:")

for n in range(l,u+1):
    if n > 1:
        for i in range(2,n//2 + 1):
            if (n % i) == 0:
                break
        else:
            print(n)