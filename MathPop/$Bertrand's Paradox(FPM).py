from time import sleep

def prob(n):

    a = n
    b = int(a/3)
    top = 0
    
    for i in range(0, int(2*n/3)):
        
        top += b/a
        a -= 1
        
        if 0 <= i < int(n/3):
            continue
            
        else:
            b -= 1
            
    
        
    ans = top/n
    
    return ans
    
    
q = 3
while True:
    pq = prob(q)
    print(q, "→", pq)
    sleep(0.5)
    q *= 2
