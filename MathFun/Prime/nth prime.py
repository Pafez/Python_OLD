p = []
j=2
n = int(input("Prime? "))

if n > 0:
    while True:
        for i in range(2,j//2 + 1):
            if (j % i) == 0:
                break
        else:
            p.append(j)
        j = j + 1
        if len(p) == n:
            break
            
ans = p[n-1]

print(ans)

