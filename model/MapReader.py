class MapReader:

    def __init__( self, file_name ):
        self.file_name = file_name

    def read( self ):
        file = open( self.file_name, "r" )
        lines = file.readlines()
        map = []
        for l in lines:
            linha = []
            for c in l:
                if c != '\n':
                    linha.append( c )
            map.append( linha )
        file.close()
        return map 
