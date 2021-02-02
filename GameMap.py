import random
from Position import Position
from Var import *

class GameMap:

    def __init__(self):
        self.color = BLACK

    def on_grid_random(self):
        x = random.randint( 0, MAX ) // CELL_SIZE * CELL_SIZE
        y = random.randint( 0, MAX ) // CELL_SIZE * CELL_SIZE
        return Position( x, y )
    
    def its_off_the_map( self, head ):
        return head.x < 0 or head.x >= MAX or head.y< 0 or head.y >= MAX

    def get_map_size(self):
        return MAP_SIZE
    
    def get_cell_size(self):
        return CELL_SIZE
    
    def get_color(self):
        return self.color