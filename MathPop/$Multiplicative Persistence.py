inputOn = False

def mul(n):
    digits = list(str(n))
    new = 1
    for i in digits:
        new = new*int(i)
    return new
    
def mp(num):
    n = num
    ans = []
    while True:
        ans.append(mul(n))
        if len(str(mul(n))) == 1:
            return ans
        n = mul(n)


while inputOn:
    inp = input()
    try:
        s = mp(int(inp))
        print(s, len(s))
    except:
        if inp.lower() == "quit":
            break

counter = 0        
while not inputOn:
    s = mp(counter)
    if len(s) > 5:
        print(str(counter)+":", s, len(s))
    counter += 1

