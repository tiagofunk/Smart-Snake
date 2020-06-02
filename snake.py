import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1,c2):
    return c1[0] == c2[0] and c1[1] == c2[1]

def bit_his_tail( snake ):
    for i in range( 1, len( snake ) ):
        if collision( snake[0], snake[i] ):
            return True
    return False

def its_off_the_map( head ):
    return head[0] < 0 or head[0] >= SIZE or head[1] < 0 or head[1] >= SIZE

def write_game_over():
    txt='GAME OVER'                                   ##### armazena o texto
    pygame.font.init()                                ##### inicia font
    fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
    fontesys=pygame.font.SysFont(fonte, 60)           ##### usa a fonte padrão
    txttela = fontesys.render(txt, 1, (255,255,255))  ##### renderiza o texto na cor desejada
    screen.blit(txttela,(200,200))

UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3
CELL  = 10
SIZE  = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)

NAME  = "SNAKE"
SNAKE_STARTING_POSITION = [(200,200),(210,200),(220,200)]

pygame.init()
screen = pygame.display.set_mode( (SIZE,SIZE) )
pygame.display.set_caption( NAME )

snake = SNAKE_STARTING_POSITION
snake_skin = pygame.Surface( (CELL,CELL) )
snake_skin.fill( WHITE )
direction = LEFT

apple_pos = on_grid_random()
apple = pygame.Surface( (CELL,CELL) )
apple.fill( RED )

clock = pygame.time.Clock()

game_over = False

while True:
    clock.tick(10)
    screen.fill( BLACK )

    if game_over:
        write_game_over()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
    else:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = UP
                if event.key == K_DOWN:
                    direction = DOWN
                if event.key == K_LEFT:
                    direction = LEFT
                if event.key == K_RIGHT:
                    direction = RIGHT
        
        if collision( snake[0], apple_pos ):
            apple_pos = on_grid_random()
            snake.append( (0,0) )

        if bit_his_tail( snake ):
            game_over = True
        
        for i in range( len(snake)-1,0,-1 ):
            snake[i] = (snake[i-1][0],snake[i-1][1])

        if its_off_the_map( snake[0] ):
            game_over = True
        
        if direction == UP:
            snake[0] = (snake[0][0], snake[0][1]-10)
        if direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1]+10)
        if direction == LEFT:
            snake[0] = (snake[0][0]-10, snake[0][1])
        if direction == RIGHT:
            snake[0] = (snake[0][0]+10, snake[0][1])

        screen.blit( apple, apple_pos )
        for pos in snake:
            screen.blit( snake_skin, pos )
    
    pygame.display.update()

