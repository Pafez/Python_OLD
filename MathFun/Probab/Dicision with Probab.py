while True:
    import random 
    probabs = (0.2, 0.1, 0.15, 0.15, 0.25, 0.15) 

    def roll(massDist):
        randRoll = random.random()
        sum = 0 
        result = 1 
        for mass in massDist:
            sum += mass 
            if randRoll < sum:
                return result
            result+=1 
    rr = input("")
    if rr == "q":
        print(roll(probabs))