from usuario import Usuario
class Cliente(Usuario):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def renovar_livro_cliente(self):
        pass

    def display(self):
        print("CLIENTE")
        return super().display()

