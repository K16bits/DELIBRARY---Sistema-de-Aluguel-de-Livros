from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_administrador_login(Tela):
    '''Classe que modela a interface grafica da tela de login do administrador'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("administrador - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        
        self.ent_login = Entry(self.janela, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela, textvariable=self.txt_senha, show="*")       
        
        self.btn_voltar_tela = Button(self.janela, width = 15, text = "Voltar")
        self.btn_login = Button(self.janela, width = 15, text = "Entrar")
        
        self.lb_janela_administrador_login = Label(self.janela, text = "LOGIN: ")
        self.lb_janela_administrador_senha = Label(self.janela, text = "SENHA: ")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_administrador_login.grid(row=0,column=0)
        self.lb_janela_administrador_senha.grid(row=1,column=0)
        self.ent_login.grid(row=0,column=1)
        self.ent_senha.grid(row=1,column=1)
        self.btn_login.grid(row=2,column=1)
        self.btn_voltar_tela.grid(row=3,column=1)  
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()