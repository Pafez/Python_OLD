def factorial(n):
    b = 1
    for i in range(n):
        b = b*(i+1)
    return b
    
def permutations(n,r):
    return int(factorial(n)/factorial(n-r))
    
while True:
    k = int(input("Enter number "))
    print(f"Your answers for {k} are:")
    for i in range(k):
        print(permutations(k,i))