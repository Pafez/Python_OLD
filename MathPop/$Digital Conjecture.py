from time import sleep
from os import system

def clear():
    return system("clear")
    
def digits(n):
    return list(str(n))
    

coun = [0,0,0,0,0,0,0,0,0]
pcoun = [0,0,0,0,0,0,0,0,0]
total = 0
    
gen = 0
while True:
    clear()
    
    print("Iteration:",gen)
    print(pcoun)
    
    gen += 1
    for i in digits(gen):
        coun[int(i)-1] += 1
    
    total += len(digits(gen))
    for i in range(9):
        pcoun[i] = str(coun[i]/total*100)[:4] + " %"
    
