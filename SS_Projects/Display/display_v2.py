class Char:
    def __init__(self, row, column, strc):
        self.strc = strc
        self.row = row
        self.column = column
        
class Entity:
    def __init__(self, strc):
        self.strc = strc
    
        
on = "#"
off = " "
class Display:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.blocks = []
        row_model = ""
        for i in range(self.column):
            row_model = row_model + off
        for i in range(self.row):
            self.blocks.append(row_model)
            
    def show(self):
        grid = ""
        for i in range(len(self.blocks) - 1):
            grid = grid + self.blocks[i] +"\n"
        grid = grid + self.blocks[-1]
        print(grid)
        
    def state(self, row, column):
        return self.blocks[row - 1][column - 1]
        
        
    def turn(self, row, column):
        if self.state(row, column) == on:
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + off + self.blocks[row - 1][column:]
        elif self.state(row, column) == off:
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + on + self.blocks[row - 1][column:]
            
    def turn_on(self, row, column):
        if self.state(row, column) == off:
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + on + self.blocks[row - 1][column:]
            
    def turn_off(self, row, column):
        if self.state(row, column) == on:
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + off + self.blocks[row - 1][column:]
        
    def row_turn(self, row):
        for column in range(1,self.column+1):
            if self.state(row, column) == on:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + off + self.blocks[row - 1][column:]
            elif self.state(row, column) == off:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + on + self.blocks[row - 1][column:]
            
    def row_turn_on(self, row):
        for column in range(1, self.column+1):
            if self.state(row, column) == off:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + on + self.blocks[row - 1][column:]
            
    def row_turn_off(self, row):
        for column in range(1, self.column+1):
            if self.state(row, column) == on:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + off + self.blocks[row - 1][column:]
        
    def column_turn(self, column):
        for row in range(1, self.row+1):
            if self.state(row, column) == on:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + off + self.blocks[row - 1][column:]
            elif self.state(row, column) == off:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + on + self.blocks[row - 1][column:]
            
    def column_turn_on(self, column):
        for row in range(1, self.row+1):
            if self.state(row, column) == off:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + on + self.blocks[row - 1][column:]
            
    def column_turn_off(self, column):
        for row in range(1, self.row+1):
            if self.state(row, column) == on:
                self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + off + self.blocks[row - 1][column:]
        
    def tile_turn(self, row1, column1, row2, column2):
        for row in range(row1, row2+1):
            for column in range(column1, column2+1):
                self.turn(row, column)
                
    def tile_turn_on(self, row1, column1, row2, column2):
        for row in range(row1, row2+1):
            for column in range(column1, column2+1):
                self.turn_on(row, column)
                
    def tile_turn_off(self, row1, column1, row2, column2):
        for row in range(row1, row2+1):
            for column in range(column1, column2+1):
                self.turn_off(row, column)
                
    def change(self, row, column, char):
        self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + char + self.blocks[row - 1][column:]
        
    def row_change(self, row, char):
        for column in range(1,self.column+1):
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + char + self.blocks[row - 1][column:]
           
    def column_change(self, column, char):
        for column in range(1,self.row+1):
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + char + self.blocks[row - 1][column:]
           
    def initialize(self, chars):
        for i in chars:
            self.change(i.row, i.column, i.strc)
            
    class Entity:
        def __init__(self, row, column, strc):
            self.row = row
            self.column = column
            self.strc = strc
        
        def move(self, vector, space):
            self.row = vector*space
        
            
    def reset(self):
        self.blocks = []
        row_model = ""
        for i in range(self.column):
            row_model = row_model + off
        for i in range(self.row):
            self.blocks.append(row_model)

    
       