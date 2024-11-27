n = int(input("Enter the number → "))
for i in range (2,int(n**(1/2)+1)):
    if n % i == 0:
        for p in range (1,n//i+1):
            if n % p == 0:
                print(p)
        break
print(n)