class Cell:
    def __init__(self, char):
        self.char = char
    
    def change(self, new_char):
        self.char = new_char
        
    def cell(self):
        return self.char
        
        
        
class Display:
    def __init__(self, l, w, h, default):
        self.x = l
        self.y = w
        self.z = h
        self.default = str(default)
        
        d1 = []
        for i in range(l):
            d1.append(self.default)
            
        d2 = []
        for i in range(w):
            d2.append(d1)
            
        d3 = []
        for i in range(h):
            d3.append(d2)
            
        self.main = d3
        
    
    def show(self):
        plot = ""
        for z in range(len(self.main)):
            sheet = ""
            for y in range(len(self.main[z])):
                line = ""
                for x in range(len(self.main[z][y])):
                    line = line + self.main[z][y][x]
                sheet = sheet + line + "\n"
            plot = plot + sheet + "\n"
        return print(plot)
        
    def show2D(self, z):
        sheet = ""
        for y in range(len(self.main[z])):
            line = ""
            for x in range(len(self.main[z][y])):
                line = line + self.main[z][y][x]
            sheet = sheet + line + "\n"
        return print(sheet)
        
    def show1D(self, y, z):
        line = ""
        for x in range(len(self.main[z][y])):
            	line = line + self.main[z][y][x]
        return print(line)
        
    def turn(self, x, y, z, state):
        self.main[z][y][x] = str(state)
        
    def turn_default(self, x, y, z):
        self.main[z][y][x] = self.default

        
    
        
    
    


