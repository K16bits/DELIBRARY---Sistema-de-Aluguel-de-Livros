from tela import Tela,Tela_inicial, Tela_administrador_login, Tela_bibliotecario_login, Tela_cliente_login, Tela_cliente,Tela_administrador,Tela_bibliotecario, Tela_cliente_registrar, Tela_emprestimo_devolucao
from usuario import Usuario
from administrador import Administrador
from cliente import Cliente
from bibliotecario import Bibliotecario

class Controle_tela_administrador():
    '''Classe para controlar a tela do administrador depois de feito o login'''
    def __init__(self):
        self.tela_administrador = Tela_administrador()
    def voltar_tela(self):
        self.tela_administrador.janela.destroy()
    def criar_acesso_bibliotecario(self):
        # implementar futuramente botao de criar acesso bibliotecario
        pass
    def retirar_acesso_bibliotecario(self):
        # implementar futuramente botao de retirar acesso bibliotecario
        pass
    def ver_todos_bibliotecario(self):
        # implementar futuramente botao de ver todos os bibliotecario
        pass
    def start(self):
        '''Inicia a tela do administrador e os eventos dos botoes'''
        self.tela_administrador.btn_fechar.configure(command=self.voltar_tela)
        self.tela_administrador.btn_criar_acesso_bibliotecario.configure(command=self.criar_acesso_bibliotecario)
        self.tela_administrador.btn_retirar_acesso_bibliotecario.configure(command=self.retirar_acesso_bibliotecario)
        self.tela_administrador.btn_ver_todos_bibliotecario.configure(command=self.ver_todos_bibliotecario)
        self.tela_administrador.iniciar()

class Controle_tela_emprestimo_devolucao():
    '''Classe para controlar a tela de emprestimo e devolucao do livro'''
    def __init__(self):
        self.tela_emprestimo_devolucao = Tela_emprestimo_devolucao()
    def sair(self):
        self.tela_emprestimo_devolucao.janela.destroy()
    def emprestimo(self):
        # implementar futuramente botao de emprestar livro
        pass
    def devolucao(self):
        # implementar futuramente botao de devolvar livro
        pass
    def start(self):
        '''Inicia a tela e os eventos dos botoes'''
        self.tela_emprestimo_devolucao.btn_sair.configure(command=self.sair)
        self.tela_emprestimo_devolucao.btn_emprestimo.configure(command=self.emprestimo)
        self.tela_emprestimo_devolucao.btn_devolucao.configure(command=self.devolucao)
        self.tela_emprestimo_devolucao.iniciar()


class Controle_tela_bibliotecario():
    '''Classe para controlar a tela do bibliotecario depois de feito o login'''
    def __init__(self):
        self.tela_bibliotecario = Tela_bibliotecario()
    def fechar_janela(self):
        self.tela_bibliotecario.janela.destroy()
    def emprestimo_devolucao(self):
        Controle_tela_emprestimo_devolucao().start()
    def criar_acesso_cliente(self):
        # implementar futuramente botao de criar acesso do cliente
        pass
    def retirar_acesso_cliente(self):
        # implementar futuramente botao de retirar acesso do cliente
        pass
    def ver_todos_cliente(self):
        # implementar futuramente botao de ver todos os clientes
        pass
    def atualizar(self):
        # implementar futuramente botao de atualizar dados do clientes
        pass
    def cadastro_livro(self):
        # implementar futuramente botao cadastrar livro
        pass
    def retirar_livro(self):
        # implementar futuramente botao de retirar livro
        pass
    def start(self):
        '''Inicia a tela do bibliotecario e os eventos dos botoes'''
        self.tela_bibliotecario.btn_fechar.configure(command = self.fechar_janela)
        self.tela_bibliotecario.btn_realizar_emprestimo_devolucao.configure(command = self.emprestimo_devolucao)
        self.tela_bibliotecario.btn_criar_acesso_cliente.configure(command = self.criar_acesso_cliente)
        self.tela_bibliotecario.btn_retirar_acesso_cliente.configure(command = self.retirar_acesso_cliente)
        self.tela_bibliotecario.btn_ver_todos_cliente.configure(command = self.ver_todos_cliente)
        self.tela_bibliotecario.btn_atualizar.configure(command = self.atualizar)
        self.tela_bibliotecario.btn_cadastro_livro.configure(command = self.cadastro_livro)
        self.tela_bibliotecario.btn_retirar_livro.configure(command = self.retirar_livro)
        self.tela_bibliotecario.iniciar()

class Controle_tela_cliente():
    '''Classe para controlar a tela do cliente depois de feito o login'''
    def __init__(self):
        self.tela_cliente = Tela_cliente()
    def sair(self):
        self.tela_cliente.janela.destroy()
    def pesquisar_livro(self):
        # implementar futuramente botao de pesquisar livro
        pass
    def ver_livros(self):
        # implementar futuramente botao que visualiza livro que estao com o cliente(emprestado)
        pass
    def renovar_livro(self):
        # implementar futuramente botao que renova livro do cliente
        pass
    def start(self):
        '''Inicia a tela do cliente e os eventos dos botoes'''
        self.tela_cliente.btn_pesquisar.configure(command = self.pesquisar_livro)
        self.tela_cliente.btn_ver_livros.configure(command = self.ver_livros)
        self.tela_cliente.btn_renovar.configure(command = self.renovar_livro)
        self.tela_cliente.btn_sair.configure(command = self.sair)
        self.tela_cliente.iniciar()

class Controle_tela_administrador_login():
    '''Classe para controlar a tela de login do administrador'''
    def __init__(self):
        self.tela_administrador_login = Tela_administrador_login()
    def voltar_tela(self):
        self.tela_administrador_login.janela.destroy()
        Controle_tela_inicial().start()
    def fazer_login(self):
        self.tela_administrador_login.janela.destroy()
        Controle_tela_administrador().start()
    def start(self):
        '''Inicia a tela de login do administrador e os eventos dos botoes'''
        self.tela_administrador_login.btn_voltar_tela.configure(command = self.voltar_tela)
        self.tela_administrador_login.btn_login.configure(command = self.fazer_login)
        self.tela_administrador_login.iniciar()

class Controle_tela_bibliotecario_login():
    '''Classe para controlar a tela de login do bibliotecario'''
    def __init__(self):
        self.tela_bibliotecario_login = Tela_bibliotecario_login()
    def voltar_tela(self):
        self.tela_bibliotecario_login.janela.destroy()
        Controle_tela_inicial().start()
    def fazer_login(self):
        self.tela_bibliotecario_login.janela.destroy()
        Controle_tela_bibliotecario().start()
    def start(self):
        '''Inicia a tela de login do bibliotecario e os eventos dos botoes'''
        self.tela_bibliotecario_login.btn_voltar_tela.configure(command = self.voltar_tela)
        self.tela_bibliotecario_login.btn_login.configure(command = self.fazer_login)
        self.tela_bibliotecario_login.iniciar()

class Controle_tela_cliente_registrar():
    '''Classe para controlar a tela do cliente para fazer o cadastro'''
    def __init__(self):
        self.tela_cliente_registrar = Tela_cliente_registrar()
    def confirmar_registro(self):
        # implementar futuramente botao de criar cadastro do cliente
        pass
    def sair(self):
        self.tela_cliente_registrar.janela.destroy()
    def start(self):
        self.tela_cliente_registrar.btn_sair.configure(command = self.sair)
        self.Tela_cliente_registrar.bnt_registrar_cliente.configure(command = self.confirmar_registro)
        self.tela_cliente_registrar.iniciar()

class Controle_tela_cliente_login():
    '''Classe para controlar a tela de login do cliente'''
    def __init__(self):
        self.tela_cliente_login = Tela_cliente_login()
    def voltar_tela(self):
        self.tela_cliente_login.janela.destroy()
        Controle_tela_inicial().start()
    def fazer_login(self):
        self.tela_cliente_login.janela.destroy()
        Controle_tela_cliente().start()
    def fazer_cadastro(self):
        Controle_tela_cliente_registrar().start()
    def pesquisar_livro(self):
        # implementar futuramente botao de pesquisar livro
        pass
    def start(self):
        '''Inicia a tela de login do cliente e os eventos dos botoes'''
        self.tela_cliente_login.btn_pesquisar.configure(command = self.pesquisar_livro)
        self.tela_cliente_login.btn_voltar_tela.configure(command = self.voltar_tela)
        self.tela_cliente_login.btn_login.configure(command = self.fazer_login)
        self.tela_cliente_login.btn_cadastro.configure(command = self.fazer_cadastro)
        self.tela_cliente_login.iniciar()

class Controle_tela_inicial():
    '''Classe para controlar a tela inicial do aplicativo'''
    def __init__(self):
        self.tela = Tela_inicial()
    def finalizar_programa(self):
        self.tela.janela.destroy()
    def mudar_tela_administrador(self):
        self.tela.janela.destroy()
        Controle_tela_administrador_login().start()
    def mudar_tela_cliente(self):
        self.tela.janela.destroy()
        Controle_tela_cliente_login().start()
    def mudar_tela_bibliotecario(self):
        self.tela.janela.destroy()
        Controle_tela_bibliotecario_login().start()
    def start(self):
        '''Inicia a tela inicial e os eventos dos botoes'''
        self.tela.btn_administrador.configure(command = self.mudar_tela_administrador)
        self.tela.btn_bibliotecario.configure(command = self.mudar_tela_bibliotecario)
        self.tela.btn_cliente.configure(command = self.mudar_tela_cliente)
        self.tela.btn_fechar.configure(command = self.finalizar_programa)
        self.tela.iniciar()

Controle_tela_inicial().start()