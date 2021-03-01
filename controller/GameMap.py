import random

from model.Position import Position
from model.Var import *

class GameMap():

    def __init__(self, map):
        self.map = map

    def on_grid_random(self, snake):
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
    
    def get_map( self, snake, apple ):
        new_map = []
        for i in range( len( self.map ) ):
            new_map.append( [] )
            for j in range( len( self.map[i] ) ):
                new_map[i].append( self.map[i][j] )
        
        x, y = apple.get_position().get_coordenates()
        new_map[x][y] = APPLE
        for i in range( snake.get_size() ):
            x, y = snake.get_position( i ).get_coordenates()
            new_map[x][y] = SNAKE
        return new_map
    
    def its_off_the_map( self, head ):
        return head.x < 0 or head.x >= len( self.map ) or head.y< 0 or head.y >= len( self.map )
    
    def collide_on_wall( self, head ):
        x, y = head.get_coordenates()
        return self.map[ x ][ y ] ==  WALL

    def get_map_size(self):
        return len( self.map )