from time import sleep
from os import system
from loading_animations import anim1
from typewriter import typer

def clear():
    return system("clear")

def typ(phrase):
    return typer(phrase, 0.07)
    
def animn1(t, intrvl):
    c = 0
    while c<t*intrvl:
        for i in range(4):
            print(anim1(i+1),flush=True)
            sleep(intrvl)
            print("\b")
            c += 1
            
def animn2(t, intrvl):
    c = 0
    while c<t*intrvl:
        for i in range(3):
            print(anim2(i+1),flush=True)
            sleep(intrvl)
            
            c += 1

def countdown(n):
    c = 0
    for i in range(n + 1):
        print(str(n-c), end="", flush=True)
        sleep(1)
        print("\b\b")
        c += 1

users = ["steve", "alex", "jeff", "notch", "tozen", "agnes", "henrik", "jasper"]

t = 0
clear()

    
while True:
    while t<5:
        for i in range(4):
            print("Connecting",anim1(i+1))
            sleep(0.2)
            clear()
            t += 1
    typ("Connected to MMD server-57.")
    sleep(3)
    clear()
    typ("Authentication required...")
    sleep(1)
    clear()
    typ("Please enter your username: ")
    user = input()
    typ("Searching user database ")
    while t<10:
        for i in range(4):
            print(anim1(i+1))
            sleep(0.2)
            clear()
            t += 1
    if not user in users:
        typer("Username not found...",0.1)
        sleep(1)
        clear()
        typ("Have a nice day :)",0.1)
        break
    
    typ("Username found. ")
    sleep(1)
    typ("Please enter the dev code: ")
    passw = input()
    clear()
    typ("Authenticating. Please wait...")
    sleep(2.5)
    
    clear()
    if not passw == "m0j4n6.m1n3cr4f7.d3v5":
            
        typer("Invalid password... ",0.25)
        sleep(1.25)
        clear()
        typer("Intruder detected!",0.25)
        typer("Blocking all access in 5",0.25)
        for i in range(5):
            print("Blocking all access in", 5 - i)
            sleep(1)
            clear()
        break
    
    typ("Authentication successful!")
    sleep(1)
    clear()
    typ("Welcome, Dev.")
            
        
    break
    t += 1
    clear()
