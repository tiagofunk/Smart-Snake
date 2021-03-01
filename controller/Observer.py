
class Observer:
    def __init__(self):
        pass

    def notify_update( self, map, score, ticks ):
        raise NotImplementedError( "Faltou implementar notify_update( self, map, score, ticks )")

    def notify_game_over( self ):
        raise NotImplementedError( "Faltou implementar notify_game_over( self )")