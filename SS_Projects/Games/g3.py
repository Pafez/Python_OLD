import random

while True:
    probabs = (1/3,1/3,1/3) 

    def roll(massDist):
        randRoll = random.random()
        sum = 0 
        result = 0
        for mass in massDist:
            sum += mass 
            if randRoll < sum:
                return result
            result+=1 
    rr = input("")
    if rr == "":
        x = roll(probabs)
        if x == 0:
            print("Rock")
        elif x == 1:
            print("Paper")
        else:
            print("Cessors")