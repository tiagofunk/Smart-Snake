import pygame, random
from pygame.locals import *

from GameMap import GameMap
from Snake import Snake
from Apple import Apple
from Position import Position
from MapReader import MapReader
from Var import CELL_SIZE, GRAY, RED, SCALE, TXT_APP_NAME, TXT_GAME_OVER, WHITE

class UI:

    def __init__(self):
        self.score = 0
        self.ticks = 0
        self.game_over = False

        self.mr      = MapReader( "map.ss" )
        self.map     = GameMap( self.mr.read() )

        self.SCREEN_WIDTH = self.map.get_map_size()*SCALE
        self.SCREEN_HEIGTH = self.map.get_map_size()*SCALE + 5*SCALE

        aux = int( self.map.get_map_size() / 2 )
        self.snake = Snake([
            Position( aux,aux ),
            Position( aux+CELL_SIZE,aux ),
            Position( aux+2*CELL_SIZE,aux )
        ])

        self.apple   = Apple( self.map.on_grid_random( self.snake ) )

        pygame.init()

        self.screen  = pygame.display.set_mode( (self.SCREEN_WIDTH, self.SCREEN_HEIGTH) )
        pygame.display.set_caption( TXT_APP_NAME )

        map_skin = pygame.Surface( (self.map.get_map_size()*SCALE,self.map.get_map_size()*SCALE) )
        map_skin.fill( self.map.get_color() )
        self.screen.blit( map_skin, (0,0) )

    def run(self):
        events = []

        while True:
            clock = pygame.time.Clock()
            clock.tick(10)
            events = pygame.event.get()

            if self.game_over:
                self.write_game_over()
                if self.check_exit(events):
                    break

            else:
                for event in events:
                    self.check_direction( event )
                
                if self.snake.get_head().equals( self.apple.get_position() ):
                    self.apple = Apple( self.map.on_grid_random( self.snake ) )
                    self.snake.increment( Position(0,0) )
                    self.score += 1

                if self.snake.bit_his_tail():
                    self.game_over = True
                
                self.snake.update()

                if self.map.collide_on_wall( self.snake.get_head() ):
                    self.game_over = True

                self.ticks += 1
                if not self.game_over:
                    self.update_view()
                
            pygame.display.update()

    def write_game_over(self):
        pygame.font.init()                                ##### inicia font
        fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
        fontesys=pygame.font.SysFont(fonte, 6*SCALE)      ##### usa a fonte padrão
        txttela = fontesys.render(TXT_GAME_OVER, 1, RED)  ##### renderiza o texto na cor desejada
        self.screen.blit(txttela,(self.SCREEN_WIDTH*(1/3),self.SCREEN_WIDTH*(1/3)))

    def update_view(self):
        self.screen.fill( GRAY )

        map_skin = pygame.Surface( ( self.map.get_map_size(), self.map.get_map_size() ) )
        map_skin.fill( self.map.get_color() )
        self.screen.blit( map_skin, (0,0) )

        cell_skin = pygame.Surface( (CELL_SIZE, CELL_SIZE) )
        for i in range( self.map.get_map_size() ):
            for j in range( self.map.get_map_size() ):
                color = self.map.get_color_in_position( i, j )
                cell_skin.fill( color )
                self.screen.blit( cell_skin, (i*SCALE,j*SCALE) )

        apple_skin = pygame.Surface( (CELL_SIZE,CELL_SIZE) )
        apple_skin.fill( self.apple.get_color() )
        x, y = self.apple.get_position().get_coordenates()
        x *= SCALE
        y *= SCALE
        self.screen.blit( apple_skin, (x,y) )

        snake_skin = pygame.Surface( (CELL_SIZE,CELL_SIZE) )
        snake_skin.fill( self.snake.get_color() )
        for i in range( 0, self.snake.get_size() ):
            x, y = self.snake.get_position(i).get_coordenates()
            x *= SCALE
            y *= SCALE
            self.screen.blit( snake_skin, (x,y) )
        
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 6*SCALE)
        str_ = "Score: " + str(self.score) + " Ticks: " + str(self.ticks)
        txttela = fontesys.render(str_, 1, WHITE)
        self.screen.blit(txttela,(10*SCALE,self.map.get_map_size()*SCALE+SCALE))

    def check_exit( self, events ):
        for event in events:
            if event.type == QUIT:
                return True
        return False

    def check_direction( self, event ):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.snake.set_direction( 0 )
            elif event.key == K_RIGHT:
                self.snake.set_direction( 1 )
            elif event.key == K_DOWN:
                self.snake.set_direction( 2 )
            elif event.key == K_LEFT:
                self.snake.set_direction( 3 )