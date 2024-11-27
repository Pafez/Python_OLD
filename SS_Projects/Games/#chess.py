from os import system
from time import sleep

startpos = [list("rnbqkbnr"), list("ppppppppp"), list("........"), list("........"), list("........"), list("........"), list("PPPPPPPP"), list("RNBQKBNR")]
board = startpos
wpieces = list("kqrbnp")
bpieces = list("KQRBNP")
blank = "."




def coor(c):
    c = list(c)
    alph = list("abcdefgh")
    for i in range(8):
        if alph[i] == c[0]:
            f = i
            break
    
    return [int(c[1]),f]
    
def inf(sq):
    c = coor(sq)
    return board[c[0]][c[1]]
    
def put(p,sq):
    c = coor(sq)
    board[c[0]][c[1]] = p
    
def clear(sq):
    c = coor(sq)
    board[c[0]][c[1]] = blank

def move(sq1,sq2):
    p1 = inf(sq1)
    p2 = inf(sq2)
    
    if p1 == blank or (p1 in wpieces and p2 in wpieces) or (p1 in bpieces and p2 in bpieces):
        return 1
    
    else:
        clear(sq1)
        put(p1,sq2)
        return 0
        
    
def show():
    screen = ""
    for ranks in range(8):
        for files in range(8):
            screen += board[7-ranks][files]
            screen += "     "
        screen += "\n\n\n"
    
    return print(screen)
    
while True:
    sleep(0.5)
    system("clear")
    sleep(0.1)
    show()
    inp = input()
    input()
    
    if inp == "esc":
        break
    elif inp == "restart":
        board = startpos
    else:
        
        if "," in inp:
            sq1, sq2 = inp.split(",")
        elif " " in inp:
            sq1, sq2 = inp.split()
        elif "x" in inp:
            sq1, sq2 = inp.split("x")
                
        move(sq1, sq2)
            

            
