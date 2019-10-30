from usuario import Usuario


class Administrador(Usuario):
    '''class administrador'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

    def display(self):
        print("ADMINISTRADOR")
        return super().display()

    
    