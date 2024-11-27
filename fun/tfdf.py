from random import randint
c1 = 0
c2 = 0
while True:
    r = randint(1,2)
    if r == 1:
        c1 += 1
    else:
        c2 += 1
    p1 = c1/(c1+c2)
    p2 = c2/(c1+c2)
    print(p1*100,"      ",p2*100)
