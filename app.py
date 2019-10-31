from tela import Tela_inicial, Tela_administrador, Tela_bibliotecario, Tela_cliente
from usuario import Usuario
from administrador import Administrador
from cliente import Cliente
from bibliotecario import Bibliotecario

class Controle_tela_administrador():
    def __init__(self):
        self.tela_administrador = Tela_administrador()
    
    def voltar_tela(self):
        self.tela_administrador.janela_administrador.destroy()
    def start(self):
        self.tela_administrador.btn_voltar_tela.configure(command = self.voltar_tela)
        self.tela_administrador.iniciar()

class Controle_tela_bibliotecario():
    def __init__(self):
        self.tela_bibliotecario = Tela_bibliotecario()
    
    def voltar_tela(self):
        self.tela_bibliotecario.janela_bibliotecario.destroy()
    def start(self):
        self.tela_bibliotecario.btn_voltar_tela.configure(command = self.voltar_tela)
        self.tela_bibliotecario.iniciar()

class Controle_tela_cliente():
    def __init__(self):
        self.tela_cliente = Tela_cliente()
    
    def voltar_tela(self):
        self.tela_cliente.janela_cliente.destroy()
    def start(self):
        self.tela_cliente.btn_voltar_tela.configure(command = self.voltar_tela)
        self.tela_cliente.iniciar()




class Controle_tela_inicial():
    def __init__(self):
        self.tela = Tela_inicial()

    def finalizar_programa(self):
        self.tela.janela_inicial.destroy()


    def mudar_tela_administrador(self):
        Controle_tela_administrador().start()

    def mudar_tela_cliente(self):
        Controle_tela_cliente().start()

    def mudar_tela_bibliotecario(self):
        Controle_tela_bibliotecario().start()

    def start(self):
        '''Acoes dos botoes da tela'''
        self.tela.btn_administrador.configure(command = self.mudar_tela_administrador)
        self.tela.btn_bibliotecario.configure(command = self.mudar_tela_bibliotecario)
        self.tela.btn_cliente.configure(command = self.mudar_tela_cliente)
        self.tela.btn_fechar.configure(command = self.finalizar_programa)
        self.tela.iniciar()

Controle_tela_inicial().start()
