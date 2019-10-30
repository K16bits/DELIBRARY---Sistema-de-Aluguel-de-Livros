from tela import Tela, Tela_administrador, Tela_bibliotecario, Tela_cliente
from usuario import Usuario
from administrador import Administrador
from cliente import Cliente
from bibliotecario import Bibliotecario

class Controle_tela():
    def __init__(self):
        self.tela = Tela()
        self.tela_administrador = Tela_administrador()
        self.tela_cliente = Tela_cliente()
        self.tela_bibliotecario = Tela_bibliotecario()

    def finalizar_programa(self):
        self.tela.janela.destroy()

    def tela_administrador(self):
        self.tela_administrador.janela_bibliotecario.destroy()
    def tela_cliente(self):
        self.tela_cliente.janela_cliente.destroy()
    def tela_bibliotecario(self):
        self.tela_administrador.janela_bibliotecario.destroy()

    def mudar_tela_administrador(self):
        # self.tela_administrador = Tela_administrador()
        self.tela_administrador.btn_voltar_tela.configure(command = self.tela_administrador)
        self.tela_administrador.iniciar()
    def mudar_tela_cliente(self):
        # self.tela_cliente = Tela_cliente()
        self.tela_cliente.btn_voltar_tela.configure(command = self.tela_cliente)
        self.tela_cliente.iniciar()
    def mudar_tela_bibliotecario(self):
        # self.tela_bibliotecario = Tela_bibliotecario()
        self.tela_bibliotecario.btn_voltar_tela.configure(command = self.tela_bibliotecario)
        self.tela_bibliotecario.iniciar()

    def start(self):
        '''Acoes dos botoes da tela'''
        self.tela.btn_administrador.configure(command = self.mudar_tela_administrador)
        self.tela.btn_bibliotecario.configure(command = self.mudar_tela_bibliotecario)
        self.tela.btn_cliente.configure(command = self.mudar_tela_cliente)
        self.tela.btn_fechar.configure(command = self.finalizar_programa)
        self.tela.iniciar()

Controle_tela().start()