from usuario import Usuario

class Cliente(Usuario):
    '''classe que representa um cliente'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
