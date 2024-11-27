from time import sleep
from random import randint

x = "0"
for i in range(114):
    x = x + "0"

display = x
trial = 1
cursors = [57, 56,36,56]

def updtDisp(x,y):
    global display
    display = display[:x] + y + display[x+1:]

def switch(x):
    updtDisp(x, str(int(not bool(int(display[x])))))
    
def on(x):
    updtDisp(x, "1")
    
def off(x):
    updtDisp(x, "0")
    
def gamble(index ,amnt):
    r = randint(0,1)
    if bool(r):
        cursors[index] += amnt
    else:
        cursors[index] -= amnt

def portal(index):
    l = len(display)
    if cursors[index] < 0:
        cursors[index] = l - 1
    elif cursors[index] > l - 1:
        cursors[index] = 0
        

while True:
    print(display)
    sleep(0.02)
    
    for i in range(len(cursors)):
        
        if trial > 1:
            switch(cursors[i])
        
        
        gamble(i, 1)
        
        portal(i)
        
        
        switch(cursors[i])
   
    trial += 1
        
    
    
