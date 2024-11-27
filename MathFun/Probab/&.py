import random
import time
while True:
    try:
        tt,m = (input().split())    
        tt = int(tt)
        m = int(m)
        s = []
        for i in range(tt):
            s.append(random.randint(1,m))
            
        for i in range(1,m+1):
            print(i, "→", s.count(i)*100/tt, "%")
        
    except Exception as e:
        print("Error:", e)
                 