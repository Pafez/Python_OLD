import time
import random
import androidhelper
adh = androidhelper.Android()
def say(x):
    adh.ttsSpeak(x)
def d(x):
    time.sleep(x)
def p(x):
    print(x)
def show(x):
    adh.maketoast(x)
def psa(x):
    p(x)
    say(x)
def psh(x):
    p(x)
    show(x)
def ss(x):
    say(x)
    show(x)

while True:
    
    menu = input("")
    if menu.lower() == "start":
        
        d(2)
        p('"Time is the only way in" -Jack Rider')
        d(3)
        psa("Hello, I am RAIS.")
        d(2)
        psa("RAIS stands for Retro Artificially Intelligent System")
        d(5)
        psa("Enter 4 digit pin code to be verified")
        d(0.5)
        for i in range(0,3):
            passin = input()
            if passin == time.strftime("%I%M"):
                passcheck = 1
                psa("Access granted")
                d(1.5)
                break
            else:
                psa("Access denied, reason: Pin code did not match")
                passcheck = 0
        if passcheck == 0:
            d(3.02)
            psa("Intruder detected through several invalid pin code entry")
            d(3.21)
            psa("Clearing database in 3")
            d(2.3)
            psa("2")
            d(1)
            psa("1")
            d(1)
            psa("Database cleared!")
            
            break
        elif passcheck == 1:
            psa("Welcome, sir")
            passcheck = -1
        while True:
                
            d(2)
            psa("What would you like to do now? Because there is no way out...")
            do = input()
            
            
            
        
        
        
