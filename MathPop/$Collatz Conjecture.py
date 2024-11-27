from time import sleep
from os import system as sys

def form(n):
    if int(n)%2 == 0:
        return n/2
    return 3*n+1
        
def rep_form(n):
    forms = []
    b = int(n)
    while not b in forms:
        forms.append(b)
        b = int(form(b))
    return forms


test = False
lans = True

while test:
    try:
        inp = int(input())
        ans = rep_form(inp)
        print(ans, len(ans))
    except:
        print("Please enter an integer")

lens = []
counter = 1
while not test:
    ans = rep_form(counter)
    if len(ans) > 0 and lans:
        lens.append(len(ans))
        print(lens)
        sys("clear")
        #print(counter,"→",len(ans))
    if len(ans) > 0 and not lans:
        print(ans, len(ans))
        sleep(1)
    
    counter += 1

