def pos(h):
    return (h**2)**(1/2)
    
C = 0
m1 = 1
m2 = int(input(""))
u1 = 0
u2 = 1

while True:
    if u1 > u2:
        if not u1 == pos(u1) and not u2 == pos(u2):
            break
        else:
            u1 = u1*(-1)
    elif u1 < u2:
        v1 = ((m1-m2)*u1 + 2*m2*u2)/(m1+m2)
        v2 = ((m2-m1)*u2 + 2*m1*u1)/(m2+m1)
        u1 = v1
        u2 = v2
        C = C + 1
    elif u1 == u2:
        if u2 == pos(u2):
            u1 = u1*(-1)
        else:
            break
        

print(C)
