class Usuario():
    '''Class usuario'''
    def __init__(self, nome = '',cpf= '',email= '',senha= '', **kwargs):
        super().__init__(**kwargs)
        self.nome = nome
        self.cpf = cpf
        self.email = email 
        self.senha = senha

    def display(self):
        print("Nome: ",self.nome)
        print("CPF: ",self.cpf)
        print("EMAIL:",self.email)
        print("SENHA: ",self.senha)
    
    def pesquisar_livro(self):
        pass
    
    def verificar_data_entrega(self):
        pass
    
    @staticmethod
    def prompt():
        return dict(nome = input("Nome: "),
        cpf = int(input("CPF: ")),
        email = input("Email: "),
        senha = int(input("Senha: ")))

    
