import random
import display
from time import sleep
from os import system

def roll(massDist):
        randRoll = random.random()
        sum = 0 
        result = 1 
        for mass in massDist:
            sum += mass 
            if randRoll < sum:
                return result
            result+=1 
disp = display.Display(30,20)
probabs = [0.50,0.50]

n=[]
nC = 0

while True:
    system("clear")
    n.append(roll(probabs))
    
    n1 = n.count(1)
    n2 = n.count(2)
    nT = n1+n2
    
    if n1==n2:
        nC += 1
    
    print(1,"→",n1/nT*100,"%")
    print(2,"→",n2/nT*100,"%")
    print("50-50 count:", nC)
