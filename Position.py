class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals( self, p ):
        return self.x == p.x and self.y == p.y
    
    def get_coordenates(self):
        return (self.x,self.y)