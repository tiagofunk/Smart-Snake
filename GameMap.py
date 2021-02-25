import random
from Position import Position
from Var import *

class GameMap:

    def __init__(self, map):
        self.color = BLACK
        self.map = map

    def on_grid_random(self, snake):
        x = -1
        y = -1
        while True:
            x = random.randint( 0, len( self.map ) ) - 1
            y = random.randint( 0, len( self.map ) ) - 1
            if self.map[x][y] == WALL:
                continue
            for i in range( snake.get_size() ):
                x_snake, y_snake = snake.get_position( i ).get_coordenates()
                if x == x_snake and y == y_snake:
                    continue
            break
        return Position( x, y )
    
    def its_off_the_map( self, head ):
        return head.x < 0 or head.x >= len( self.map ) or head.y< 0 or head.y >= len( self.map )
    
    def collide_on_wall( self, head ):
        x, y = head.get_coordenates()
        return self.map[ x ][ y ] ==  WALL

    def get_map_size(self):
        return len( self.map )
    
    def get_color_in_position( self, i, j ):
        if self.map[i][j] == EMPTY:
            return BLACK
        return WHITE
    
    def get_color(self):
        return self.color