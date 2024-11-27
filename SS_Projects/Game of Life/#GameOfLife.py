# Failed #

from os import system
from time import sleep

system("clear")
pre_display = str(10**(116*32))
pre_display0 = pre_display[1:]
display = pre_display0.replace("0"," ")


alive = "0"
dead = " "

def assign(string, index, value):
    old_string = string
    new_string = old_string[:index] + value + old_string[index+1:]
    return new_string

def cellulate(row, column):
    cell = (row-1)*116 + (column-1)
    return cell

def grid_resurrect(row, column):
    cell = cellulate(row, column)
    assign(display, cell, alive)
    
def grid_kill(row, column):
    cell = cellulate(row, column)
    assign(display, cell, dead)

def resurrect(cell):
    assign(display, cell, alive)
    
def kill(cell):
    assign(display, cell, dead)

def state(cell):
    return display[cell]

def genBT(row, column):
    main_cell = cellulate(row, column)
    neighbour_cells = [cellulate(row+1,column+1),cellulate(row+1,column),cellulate(row+1,column-1),cellulate(row,column+1),cellulate(row,column-1),cellulate(row-1,column+1),cellulate(row-1,column),cellulate(row-1,column-1)]
    
    neighbour_states = []
    for i in neighbour_cells:
        neighbour_states.append(state(i))
    
    alive_neighbours = neighbour_states.count(alive)
    
    if state(main_cell) == dead:
        if alive_neighbours == 3:
            resurrect(main_cell)
    elif state(main_cell) == alive:
        if alive_neighbours < 2 or alive_neighbours > 3:
            kill(main_cell)

def run():
    for row in range(2, 32):
        for column in range(2,116):
            genBT(row, column)

grid_resurrect(2,1)
grid_resurrect(2,2)
grid_resurrect(1,1)
grid_resurrect(1,2)
grid_resurrect(3,2)
grid_resurrect(2,3)


while True:
    print(display)
    
    sleep(0.1)
    system("clear")
    
    run()
    
    
    
    