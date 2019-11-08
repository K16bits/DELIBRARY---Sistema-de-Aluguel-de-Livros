from usuario import Usuario

class Administrador(Usuario):
    '''classe que representa um administrador'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    