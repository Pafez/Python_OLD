import random

def roll(massDist):
        randRoll = random.random()
        sum = 0 
        result = 1 
        for mass in massDist:
            sum += mass 
            if randRoll < sum:
                return result
            result+=1 

probabs = [0.2, 0.3,0.1,0.1,0.2]

n = 10000
tes = []
for i in range(n):
    tes.append(roll(probabs))

for t in range(len(probabs)):
    print(t+1, "→", str(tes.count(t+1)*100/n)+"%")

