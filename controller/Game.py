
from model.MapReader import MapReader
from model.Snake import Snake
from model.Apple import Apple
from model.Position import Position
from model.Var import CELL_SIZE
from controller.GameMap import GameMap

class Game:
    
    def __init__(self):

        self.score = 0
        self.ticks = 0
        self.game_over = False

        self.observers = []

        self.map_path = "./maps/map.ss"
        self.game_map = GameMap( MapReader( self.map_path ).read() )

        aux = int( self.game_map.get_map_size() / 2 )
        self.snake = Snake([
            Position( aux, aux ),
            Position( aux+1,aux ),
            Position( aux+2,aux )
        ])

        self.apple = Apple( self.game_map.on_grid_random( self.snake ) )

    def execute_game_step(self):
        if not self.game_over:
            if self.snake.get_head().equals( self.apple.get_position() ):
                self.apple = Apple( self.game_map.on_grid_random( self.snake ) )
                self.snake.increment( Position(0,0) )
                self.score += 1
            
            if self.snake.bit_his_tail():
                self.game_over = True
                self.notify_game_over()

            self.snake.update()

            if self.game_map.collide_on_wall( self.snake.get_head() ) :
                self.game_over = True
                self.notify_game_over()
            
            self.ticks += 1

            if not self.game_over:
                self.notify_update()
    
    def add_observer( self, observer ):
        self.observers.append( observer )
    
    def get_map_size( self ):
        return self.game_map.get_map_size()
    
    def change_snake_direction( self, direction ):
        self.snake.set_direction( direction )
    
    def notify_game_over(self):
        for obs in self.observers:
            obs.notify_game_over()
    
    def notify_update( self ):
        for obs in self.observers:
            obs.notify_update( self.game_map.get_map( self.snake, self.apple ), self.score, self.ticks )