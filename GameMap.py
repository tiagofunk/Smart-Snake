import random
from Position import Position

class GameMap:

    def __init__(self):
        self.MIN   =   0
        self.CELL  =  10
        self.SIZE  = 600
        self.MAX   = 590
        self.color = (0,0,0)

    def on_grid_random(self):
        x = random.randint( self.MIN, self.MAX ) // self.CELL * self.CELL
        y = random.randint( self.MIN, self.MAX ) // self.CELL * self.CELL
        return Position( x, y )
    
    def its_off_the_map( self, head ):
        return head.x < MIN or head.x >= SIZE or head.y< MIN or head.y >= SIZE
    
    def get_size(self):
        return self.SIZE
    
    def get_cell(self):
        return self.CELL