import pygame
from pygame.locals import *

from controller.Observer import Observer
from controller.Game import Game
from model.Var import *

class UI( Observer ):

    def __init__(self):

        self.game_over = False

        self.game = Game()
        self.game.add_observer( self )

        #mudar nome da variavel
        self.SCREEN_SIZE = self.game.get_map_size()*SCALE
        self.SCREEN_WIDTH = self.SCREEN_SIZE
        self.SCREEN_HEIGTH = self.SCREEN_SIZE + 5*SCALE

        pygame.init()

        self.screen  = pygame.display.set_mode( (self.SCREEN_WIDTH, self.SCREEN_HEIGTH) )
        pygame.display.set_caption( TXT_APP_NAME )

        map_skin = pygame.Surface( (self.SCREEN_SIZE,self.SCREEN_SIZE) )
        map_skin.fill( MAP_COLOR )
        self.screen.blit( map_skin, (0,0) )
    
    def notify_update(self, map, score, ticks ):
        self.update_view( map, score, ticks )
    
    def notify_game_over(self):
        self.game_over = True
        self.write_game_over()
        
    def run(self):
        events = []

        while True:
            clock = pygame.time.Clock()
            clock.tick(10)
            events = pygame.event.get()

            if self.game_over:
                if self.check_exit(events):
                    break
            else:
                self.check_direction( events )
                self.game.execute()
                
            pygame.display.update()

    def write_game_over(self):
        pygame.font.init()                                ##### inicia font
        fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
        fontesys=pygame.font.SysFont(fonte, 6*SCALE)      ##### usa a fonte padrão
        txttela = fontesys.render(TXT_GAME_OVER, 1, RED)  ##### renderiza o texto na cor desejada
        self.screen.blit(txttela,(self.SCREEN_WIDTH*(1/3),self.SCREEN_WIDTH*(1/3)))

    def update_view(self, map, score, ticks ):
        self.screen.fill( GRAY )

        # acho que não precisa dessas três linhas
        map_skin = pygame.Surface( ( self.SCREEN_SIZE, self.SCREEN_SIZE ) )
        map_skin.fill( MAP_COLOR )
        self.screen.blit( map_skin, (0,0) )

        # melhorar o código
        cell_skin = pygame.Surface( (CELL_SIZE, CELL_SIZE) )
        i = 0
        for line in map:
            j = 0
            for position in line:
                if position == EMPTY:
                    color = MAP_COLOR
                elif position == WALL:
                    color = WALL_COLOR
                elif position == SNAKE:
                    color = SNAKE_COLOR
                elif position == APPLE:
                    color = APPLE_COLOR
                cell_skin.fill( color )
                self.screen.blit( cell_skin, (i*SCALE,j*SCALE) )
                j += 1
            i += 1
        
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 6*SCALE)
        str_ = "Score: " + str(score) + " Ticks: " + str(ticks)
        txttela = fontesys.render(str_, 1, WHITE)
        self.screen.blit(txttela,(10*SCALE,self.game.get_map_size()*SCALE+SCALE))

    def check_exit( self, events ):
        for event in events:
            if event.type == QUIT:
                return True
        return False

    def check_direction( self, events ):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.game.change_snake_direction( UP )
                elif event.key == K_RIGHT:
                    self.game.change_snake_direction( RIGHT )
                elif event.key == K_DOWN:
                    self.game.change_snake_direction( DOWN )
                elif event.key == K_LEFT:
                    self.game.change_snake_direction( LEFT )