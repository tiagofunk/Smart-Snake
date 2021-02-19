from Position import Position
from Var import DOWN, LEFT, RIGHT, UP, WHITE

class Snake:

    def __init__(self, body):
        self.body = body
        self.color = WHITE
        self.direction = LEFT
        self.is_dead = False

    def bit_his_tail( self ):
        for i in range( 1, len( self.body ) ):
            if self.body[0].equals( self.body[i] ):
                self.is_dead = True
                return True
        return False
    
    def its_off_the_map( self, min, max ):
        value  = (self.body[0].x <= min or self.body[0].x >= max
            or self.body[0].y<= min or self.body[0].y >= max)
        self.is_dead = value
        return value

    def get_head(self):
        return self.body[ 0 ]
    
    def get_color(self):
        return self.color
    
    def get_size(self):
        return len( self.body )
    
    def get_position( self, pos ):
        return self.body[ pos ]
    
    def set_is_dead(self, is_dead):
        self.is_dead = is_dead
    
    def set_direction( self, direction ):
        if not (direction == UP or direction == DOWN or direction == LEFT or direction == RIGHT):
            pass
        elif (self.direction == LEFT and direction == RIGHT or
            self.direction == RIGHT and direction == LEFT or
            self.direction == UP and direction == DOWN or
            self.direction == DOWN and direction == UP
            ):
            pass
        else:
            self.direction = direction
    
    def increment( self, position ):
        self.body.append( position )
    
    def update(self):
        if self.is_dead:
            return
        for i in range( len(self.body)-1,0,-1 ):
            self.body[i] = self.body[i-1]
        
        if self.direction == UP:
            self.body[0] = Position(self.body[0].x, self.body[0].y-1)
        if self.direction == DOWN:
            self.body[0] = Position(self.body[0].x, self.body[0].y+1)
        if self.direction == LEFT:
            self.body[0] = Position(self.body[0].x-1, self.body[0].y)
        if self.direction == RIGHT:
            self.body[0] = Position(self.body[0].x+1, self.body[0].y)