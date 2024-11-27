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
            grid = grid + self.blocks[i] + "\n"
        grid = grid + self.blocks[-1]
        return print(grid)
        
    def get(self):
        grid = ""
        for i in range(len(self.blocks) - 1):
            grid = grid + self.blocks[i] + "\n"
        grid = grid + self.blocks[-1]
        return grid
    
    def state(self, row, column):
        row, column = row % self.row, column % self.column
        return self.blocks[row - 1][column - 1]
        
        
    def turn(self, row, column):
        row, column = row%self.row, column%self.column
        if self.state(row, column) == on:
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + off + self.blocks[row - 1][column:]
        elif self.state(row, column) == off:
            self.blocks[row - 1] = self.blocks[row - 1][:column - 1] + on + self.blocks[row - 1][column:]
            
    def turn_on(self, row, column):
        if self.state(row, column) == off:
            self.turn(row,column)
            
    def turn_off(self, row, column):
        if self.state(row, column) == on:
            self.turn(row,column)
        
    def row_turn(self, row):
        for column in range(1,self.column+1):
            self.turn(row,column)
                        
    def row_turn_on(self, row):
        for column in range(1, self.column+1):
            self.turn_on(row,column)
                        
    def row_turn_off(self, row):
        for column in range(1, self.column+1):
            self.turn_off(row,column)
            
    def column_turn(self, column):
        for row in range(1, self.row+1):
            self.turn(row,column)
            
    def column_turn_on(self, column):
        for row in range(1, self.row+1):
            self.turn_on(row,column)
                        
    def column_turn_off(self, column):
        for row in range(1, self.row+1):
            self.turn_off(row,column)
                    
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
                
    def coste(self, row1, column1, row2, column2):
        if self.state(row1, column1) != self.state(row2, column2):
            self.turn(row2, column2)
            
    def custe(self, row1, column1, row2, column2):
        if self.state(row1, column1) != self.state(row2, column2) == off:
            self.turn_off(row1, column1)
            self.turn_on(row2, column2)
            return 0
        elif self.state(row1, column1) != self.state(row2, column2) == on:
            self.turn_off(row1, column1)
            self.turn_off(row2, column2)
            return 1
    
    
    def reset(self):
        self.blocks = []
        row_model = ""
        for i in range(self.column):
            row_model = row_model + off
        for i in range(self.row):
            self.blocks.append(row_model)

    
       