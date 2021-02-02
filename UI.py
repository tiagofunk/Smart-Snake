import pygame, random
from pygame.locals import *

from GameMap import GameMap
from Snake import Snake
from Apple import Apple
from Position import Position
from Var import BLACK, CELL_SIZE, GRAY, MAP_SIZE, MAX, RED, SCALE, SCREEN_HEIGHT, SCREEN_WIDTH, TXT_APP_NAME, TXT_GAME_OVER, WHITE

def write_game_over(screen):
    pygame.font.init()                                ##### inicia font
    fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
    fontesys=pygame.font.SysFont(fonte, 6*SCALE)      ##### usa a fonte padrão
    txttela = fontesys.render(TXT_GAME_OVER, 1, RED)  ##### renderiza o texto na cor desejada
    screen.blit(txttela,(MAP_SIZE*(1/3),MAP_SIZE*(1/3)))

def setup( map ):
    pygame.init()

    screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
    pygame.display.set_caption( TXT_APP_NAME )

    #screen.fill( BLACK )

    map_skin = pygame.Surface( (MAP_SIZE,MAP_SIZE) )
    map_skin.fill( map.get_color() )
    screen.blit( map_skin, (0,0) )

    return screen

def update_view(screen, map, apple, snake, score, ticks):
    screen.fill( GRAY )

    map_skin = pygame.Surface( (MAP_SIZE,MAP_SIZE) )
    map_skin.fill( map.get_color() )
    screen.blit( map_skin, (0,0) )

    apple_skin = pygame.Surface( (CELL_SIZE,CELL_SIZE) )
    apple_skin.fill( apple.get_color() )
    screen.blit( apple_skin, apple.get_position().get_coordenates() )

    snake_skin = pygame.Surface( (CELL_SIZE,CELL_SIZE) )
    snake_skin.fill( snake.get_color() )
    for i in range( 0, snake.get_size() ):
        screen.blit( snake_skin, snake.get_position(i).get_coordenates() )
    
    pygame.font.init()
    fonte=pygame.font.get_default_font()
    fontesys=pygame.font.SysFont(fonte, 6*SCALE)
    str_ = "Score: " + str(score) + " Ticks: " + str(ticks)
    txttela = fontesys.render(str_, 1, WHITE)
    screen.blit(txttela,(10*SCALE,MAP_SIZE+SCALE))

def check_exit( events ):
    for event in events:
        if event.type == QUIT:
            return True
    return False

def check_direction( event, snake ):
    if event.type == KEYDOWN:
        if event.key == K_UP:
            snake.set_direction( 0 )
        elif event.key == K_RIGHT:
            snake.set_direction( 1 )
        elif event.key == K_DOWN:
            snake.set_direction( 2 )
        elif event.key == K_LEFT:
            snake.set_direction( 3 )

def run():
    myMap    = GameMap()
    snake    = Snake()
    apple    = Apple( myMap.on_grid_random() )

    score = 0
    ticks = 0
    game_over = False
        
    screen = setup( myMap  )
    events = []

    while True:
        clock = pygame.time.Clock()
        clock.tick(10)
        events = pygame.event.get()

        if game_over:
            write_game_over( screen )
            if check_exit(events):
                break

        else:
            for event in events:
                check_direction( event, snake )
            
            if snake.get_head().equals( apple.get_position() ):
                apple = Apple( myMap.on_grid_random() )
                snake.increment( Position(0,0) )
                score = score + 1

            if snake.bit_his_tail():
                game_over = True
            
            snake.update()

            if snake.its_off_the_map( 0, MAX ):
                game_over = True

            update_view(screen, myMap, apple, snake, score, ticks )

        if not game_over:
            ticks = ticks + 1
        pygame.display.update()
        
        

run()