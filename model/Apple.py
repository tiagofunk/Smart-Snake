from model.Var import RED

class Apple:

    def __init__(self, position):
        #retirar a cor daqui
        self.color = RED
        self.position = position
    
    def get_position(self):
        return self.position
    
    def get_color(self):
        return self.color