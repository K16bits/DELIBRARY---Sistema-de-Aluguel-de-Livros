class Usuario():
    '''classe que representa um  usuario'''
    def __init__(self, nome = '',sobrenome = '',cpf= '',email= '', login = '', senha= '', **kwargs):
        super().__init__(**kwargs)
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.email = email
        self.login = login
        self.senha = senha


    
