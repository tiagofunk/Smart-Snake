from Position import Position

class Snake:

    def __init__(self):
        self.body  = [ Position(200,200),Position(210,200),Position(220,200) ]
        self.color = (255,255,255)
        self.UP    = 0
        self.RIGHT = 1
        self.DOWN  = 2
        self.LEFT  = 3
        self.direction = 3

    def bit_his_tail( self ):
        for i in range( 1, len( self.body ) ):
            if self.body[0].equals( self.body[i] ):
                return True
        return False
    
    def its_off_the_map( self, min, max ):
        return (self.body[0].x < min or self.body[0].x >= max
            or self.body[0].y< min or self.body[0].y >= max)

    def get_head(self):
        return self.body[ 0 ]
    
    def get_color(self):
        return self.color
    
    def get_size(self):
        return len( self.body )
    
    def get_position( self, pos ):
        return self.body[ pos ]
    
    def set_direction( self, direction ):
        if not (direction == self.UP or direction == self.RIGHT 
            or direction == self.DOWN or direction == self.LEFT):
            self.direction = self.LEFT 
        else:
            self.direction = direction
    
    def increment( self, position ):
        self.body.append( position )
    
    def update(self):
        for i in range( len(self.body)-1,0,-1 ):
            self.body[i] = self.body[i-1]
        
        if self.direction == self.UP:
            self.body[0] = Position(self.body[0].x, self.body[0].y-10)
        if self.direction == self.DOWN:
            self.body[0] = Position(self.body[0].x, self.body[0].y+10)
        if self.direction == self.LEFT:
            self.body[0] = Position(self.body[0].x-10, self.body[0].y)
        if self.direction == self.RIGHT:
            self.body[0] = Position(self.body[0].x+10, self.body[0].y)