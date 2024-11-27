n = int(input("Enter the number you want to factor → "))
for i in range(1,n//2 + 1):
    if (n % i) == 0:
        print(i)
print(n)