from tetrating import tetration

def pentration(b,p):
    bp = b
    for i in range(1,p):
        b = tetration(bp,b)
    return b
    
def pentrate(b,p):
    bp = b
    for i in range(1,p):
        b = tetration(bp,b)
    return print(b)
    
pentrate(2,2)
