from Pafez import factorize as factor

def infdecdiv(x,y,lim=20):
    for i in factor(x):
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
    
print(infdecdiv(25555,5555,50))
        

