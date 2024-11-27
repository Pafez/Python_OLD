from time import sleep

def write(phrase):
    print(phrase, end="", flush=True)
    
    return 0
    

def typer(phrase, interval):
    c = 0
    while len(phrase)>c:
        sleep(interval)
        write(phrase[c])
        c += 1
        