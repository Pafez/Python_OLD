def checkfactors(n):
    factors = []
    for i in range (2,int(n**(1/2)+1)):
        if n % i == 0:
            for p in range (1,n//i+1):
                if n % p == 0:
                    factors.append(p)
            break
    factors.append(n)
    return factors
    
    

def checkprime(n):
    if n > 1:
        for i in range(2, n//2 + 1):
            if (n % i) == 0:
                print(n," is not a prime number.")
                prime = 1
                break
        else:
            print(n," is a prime number.")
            prime = 0
    else:
        print(n," is not a prime number")
        prime = 1



def factorize(a):
    factor = []
    
    if a == 1:
        print(1)
    elif a < 0:
        print(-1)
        b = -a
        while 1 < b:
            for i in range(2, int(b+1)):
                if (b % i) == 0:
                    factor.append(i)
                    b = b/i
                    break
    else:
        b = a
        while 1 < b:
            for i in range(2, int(b+1)):
                if (b % i) == 0:
                    factor.append(i)
                    b = b/i
                    break
    return factor


def primes(l,u):
    prime = []
    for n in range(l,u+1):
        if n > 1:
            for i in range(2,n//2 + 1):
                if (n % i) == 0:
                    break
            else:
                prime.append(n)
    return prime

def pos(a):
    return (a**2)**(1/2)

def benfordise(entry):
    
    letters = " abcdefghijklmnopqrstuvwxyz0123456789.,;:!?"
    l = list(entry)
    
    nlet = []
    for i in letters:
        nlet.append(0)
        
    for char in l:
        for num in range(len(letters)):
            if char.lower() == letters[num]:
                nlet[num] += 1
                
    return nlet
    
def benfordperc(entry):
    nlets = benfordise(entry)
    
    t = sum(nlets)
    nlp = []
    for i in nlets:
        nlp.append(i/t)
        
    return nlp

def infdecdiv(x,y,lim=20):
    for i in factorize(x):
        if y%i == 0:
            x //= i
            y //= i
    
    ans = ""
    digits = len(ans)
    carry = ""
    
    for i in range(len(str(x))):
        dA = int(carry + str(x)[i])//y
        dR = int(carry + str(x)[i])%y
        
        ans += str(dA)
        carry = str(dR)
        
        digits = len(ans)
    
    for i in range(digits - 1):
        if ans[0] == "0":
            ans = ans[1:]
    
    if dR == 0:
        return ans
    
    ans += "."
    
    while digits <= lim:
        
        dA = int(carry + "0")//y
        dR = int(carry + "0")%y
        
        ans += str(dA)
        carry = str(dR)
        
        digits = len(ans) - 1
    
   
    return ans

def sepDecs(x):
    x = str(x)
    decas = x
    decis = ""
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

import random
def rollprob(massDist):
    randRoll = random.random()
    sum = 0 
    result = 1 
    for mass in massDist:
        sum += mass 
        if randRoll < sum:
            return result
        result += 1 
    return 0
