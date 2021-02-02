
class Apple:

    def __init__(self, position):
        self.color = (255,0,0)
        self.position = position
    
    def set_position(self, position):
        self.position = position
    
    def get_position(self):
        return self.position
    
    def get_color(self):
        return self.color