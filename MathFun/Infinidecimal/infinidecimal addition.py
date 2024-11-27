def sepDecs(x):
    x = str(x)
    for i in range(len(x)):
        if x[i] == ".":
            decas = x[:i]
            decis = x[i+1:]
    return [decas, decis]

def add(m,n,c):
    carry = 0
    m = int(m)
    n = int(n)
    c = int(c)
    
    ans = m+n+c
    if len(str(ans)) > 1:
        carry = str(ans)[0] 
        base = str(ans)[1]
        
    else:
        base = str(ans)[0]
        
    return [base, carry]



def infdecadd(x,y):
    a = sepDecs(x)
    b = sepDecs(y)
    
    t = [str(int(a[0]) + int(b[0])),""]
    
    ddiff = len(a[1]) - len(b[1])
    if ddiff > 0:
        for i in range(ddiff):
            b[1] += "0"
    else:
        for i in range(ddiff*(-1)):
            a[1] += "0"
    
    
    carry = 0
    tf = []
    for i in range(len(a[1])):
        dadd = add(a[1][-1-i], b[1][-1-i], carry)
        tf.append(dadd[0])
        carry = int(dadd[1])
        
    
    for i in range(len(tf)):
        t[1] += tf[-1-i]
    
    t[0] = str(int(t[0])+carry)
    
    while True:
        if len(t[1]) > 1 and t[1][-1] == "0":
            t[1] = t[1][:-1]
        else:
            break
    
    ans = t[0] + "." + t[1]
    
    return ans
    
print(infdecadd(56.999999, 4.000001))
        

