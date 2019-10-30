from usuario import Usuario
class Bibliotecario(Usuario):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def chamar_emprestimo(self):
        pass
    
    def display(self):
        print("BIBLIOTECARIO")
        return super().display()

