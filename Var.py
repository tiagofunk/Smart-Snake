from pygame.constants import FINGERDOWN
from typing_extensions import Final

BLACK : Final = (0,0,0)
RED   : Final = (255,0,0)
WHITE : Final = (255,255,255)
GRAY  : Final = (20,20,20)

UP     : Final = 0
RIGHT  : Final = 1
DOWN   : Final = 2
LEFT   : Final = 3

SCALE     : Final =  10
CELL_SIZE : Final =  1 * SCALE
MAP_SIZE  : Final = 60 * SCALE
MAX       : Final = MAP_SIZE - CELL_SIZE
SCREEN_HEIGHT : Final = MAP_SIZE + 5 * SCALE
SCREEN_WIDTH  : Final = MAP_SIZE

TXT_APP_NAME  : Final = "SMART SNAKE"
TXT_GAME_OVER : Final = "GAME OVER"