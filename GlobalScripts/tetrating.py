def tetrate(b,t):
    b0=b
    for i in range(1,t):
        b = b0**b
    return print(b)

def tetration(b,t):
    b0 = b
    for i in range(1,t):
        b = b0**b
    return b

