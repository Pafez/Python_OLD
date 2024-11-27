from Pafez import sepDecs

def sepMuls(n):
    s = sepDecs(n)
    
    num, exdiv = int(str(s[0])+str(s[1])), len(s[1])
    
    return [num, exdiv]

def infdecmul(x,y):
    a = sepMuls(x)
    b = sepMuls(y)
    
    mnum = a[0]*b[0]
    mexdiv = a[1] + b[1]
    for i in range(mexdiv):
        mnum = "0" + str(mnum)
    
    ans = str(mnum)[:-mexdiv] + "." + str(mnum)[-mexdiv:]
    
    return ans
    

print(infdecmul(0.0001,0.0015))
