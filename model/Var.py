from typing_extensions import Final

BLACK : Final = (0,0,0)
RED   : Final = (255,0,0)
WHITE : Final = (255,255,255)
GRAY  : Final = (20,20,20)

MAP_COLOR   : Final = BLACK
WALL_COLOR  : Final = WHITE
SNAKE_COLOR : Final = WHITE
APPLE_COLOR : Final = RED

UP     : Final = 0
RIGHT  : Final = 1
DOWN   : Final = 2
LEFT   : Final = 3

SCALE     : Final =  10
CELL_SIZE : Final =  1 * SCALE

TXT_APP_NAME  : Final = "SMART SNAKE"
TXT_GAME_OVER : Final = "GAME OVER"

EMPTY   : Final = "e"
WALL    : Final = "w"
SNAKE   : Final = "s"
APPLE   : Final = "a"