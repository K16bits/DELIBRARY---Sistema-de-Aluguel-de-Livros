from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_inicial(Tela):
    '''Classe que modela a interface grafica da tela inicial'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("DELIBRARY")
        self.lb_janela_inicial = Label(self.janela, text = "ENTRAR NO SISTEMA COMO: ")
        
        self.btn_administrador = Button(self.janela, width = 15, text="Administrador")
        self.btn_bibliotecario = Button(self.janela, width = 15, text="Bibliotecario")
        self.btn_cliente = Button(self.janela, width = 15, text="Cliente")        
        self.btn_fechar = Button(self.janela, width = 15, text="Sair")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_inicial.grid(row=0,column=0)
        self.btn_administrador.grid(row=1,column=0)
        self.btn_bibliotecario.grid(row=2,column=0)
        self.btn_cliente.grid(row=3,column=0)
        self.btn_fechar.grid(row=4,column=0)      
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()