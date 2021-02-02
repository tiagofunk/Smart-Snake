import pygame, random
from pygame.locals import *

from GameMap import GameMap
from Snake import Snake
from Apple import Apple
from Position import Position

def write_game_over(screen):
    txt='GAME OVER'                                   ##### armazena o texto
    pygame.font.init()                                ##### inicia font
    fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
    fontesys=pygame.font.SysFont(fonte, 60)           ##### usa a fonte padrão
    txttela = fontesys.render(txt, 1, (255,0,0))  ##### renderiza o texto na cor desejada
    screen.blit(txttela,(200,200))
    print("game over")

def setup( screen_size ):
    pygame.init()

    screen = pygame.display.set_mode( ( screen_size, screen_size ) )
    pygame.display.set_caption( "SNAKE" )

    return screen

def check_exit( events ):
    for event in events:
        if event.type == QUIT:
            pygame.quit()

def check_direction( event, snake ):
    if event.type == KEYDOWN:
        if event.key == K_UP:
            snake.set_direction( 0 )
        if event.key == K_RIGHT:
            snake.set_direction( 1 )
        if event.key == K_DOWN:
            snake.set_direction( 2 )
        if event.key == K_LEFT:
            snake.set_direction( 3 )

def update_view(screen, apple, snake, cell_size):
    apple_skin = pygame.Surface( (cell_size,cell_size) )
    apple_skin.fill( apple.get_color() )
    screen.blit( apple_skin, apple.get_position().get_coordenates() )

    snake_skin = pygame.Surface( (cell_size,cell_size) )
    snake_skin.fill( snake.get_color() )
    for i in range( 0, snake.get_size() ):
        screen.blit( snake_skin, snake.get_position(i).get_coordenates() )

def run():
    myMap    = GameMap()
    snake    = Snake()
    apple    = Apple( myMap.on_grid_random() )

    score = 0
    game_over = False
        
    screen = setup( myMap.get_size() )
    events = []

    while True:
        clock = pygame.time.Clock()
        clock.tick(10)

        screen.fill( (0,0,0) )
        events = pygame.event.get()

        if game_over:
            write_game_over( screen )

            check_exit(events)

        else:
            for event in events:
                check_direction( event, snake )
            
            if snake.get_head().equals( apple.get_position() ):
                apple = Apple( myMap.on_grid_random() )
                snake.increment( Position(0,0) )

            if snake.bit_his_tail():
                game_over = True
            
            snake.update()

            if snake.its_off_the_map( 0, myMap.get_size() ):
                game_over = True
                print("game over")

            update_view(screen, apple, snake, myMap.get_cell() )

        pygame.display.update()
        
        

run()