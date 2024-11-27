for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if (a*10000 + b*1000 + c*100 + d*10 + a) % 5 == 0 and (a+b+c+d+a)%5 == 0:
                    print(a,b,c,d,a)
