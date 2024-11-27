from os import system
from time import sleep
from random import randint
from Pafez import *
from display import Display

class subject:
    def __init__(self,lbl,name,pos,energy=50,state="alive",mvp=[.23,.23,.23,.23],mtr=[.2,.05,.01],mrp=[1,0]):
        self.lbl = lbl
        self.name = name
        self.mvp = mvp
        self.pos = pos
        self.energy = energy
        self.mrp = mrp
        self.mtr = mtr
        self.state = state
        
        
    def move(self,d):
        if d == 1:
            self.pos[0]-=1
        elif d == 2:
            self.pos[1]-=1
        elif d == 3:
            self.pos[0]+=1
        elif d == 4:
            self.pos[1]+=1
        if d != 0:
            self.energy -= 1
            
    def energy_increment(self, amount):
        self.energy += amount
    
    def mope(self):
        return self.move(rollprob(self.mvp))
        
    def mutate(self):
        for i in range(rollprob(self.mtr)):
            
            top = rollprob(self.mrp)
            if top == 1:
                self.mvp[randint(0,3)] = randint(1,25)/100
    
    def change_name(self,name):
        self.name = name
        
    def kill(self):
        self.state = "dead"
        
    def revive(self):
        self.state = "alive"

                
screen = Display(30,60)

subs = []
for i in range(100):
    c = subject(i+1,"testcase"+str(i+1),[randint(1,screen.row),randint(1,screen.column)])
    subs.append(c)

gen = 0
while True:
    screen.reset()
    total = len(subs)
    for i in subs:
        
        if i.energy <= 0:
            i.kill()
            
        
        if i.state == "dead":
            total -= 1
            continue
            
        cp = i.pos
        screen.turn_on(cp[0],cp[1])
        
        
        i.mope()
        i.mutate()
        i.energy_increment(0.5)
        
        
    
    
    sleep(0.0)
    system("cls")
    screen.show()
    print("Generation:", gen,"       Total:", total)
    
    
    
    gen += 1
    
