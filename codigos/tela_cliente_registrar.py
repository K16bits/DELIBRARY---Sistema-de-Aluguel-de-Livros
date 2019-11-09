from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_cliente_registrar(Tela):
    '''Classe que modela a interface grafica da tela para o cliente fazer o cadastro'''
    def __init__(self):
        self.janela = Tk()
        self.janela.wm_title("Cadastro de cliente - DELIBRARY")
        self.janela.geometry("800x200+50+50")

        self.txt_nome_cliente = StringVar()
        self.txt_sobrenome_cliente = StringVar()
        self.txt_cpf_cliente = StringVar()
        self.txt_login_cliente = StringVar()
        self.txt_senha_cliente = StringVar()
        self.txt_email_cliente = StringVar()
        
        self.lbl_nome_cliente = Label(self.janela, text="Nome")
        self.lbl_sobrenome_cliente = Label(self.janela, text="Sobrenome")
        self.lbl_cpf_cliente = Label(self.janela, text="CPF")
        self.lbl_login_cliente = Label(self.janela, text="Criar login")
        self.lbl_senha_cliente = Label(self.janela, text="Criar senha")
        self.lbl_email_cliente = Label(self.janela, text = "Email ")

        self.ent_nome_cliente = Entry(self.janela, textvariable=self.txt_nome_cliente)
        self.ent_sobrenome_cliente = Entry(self.janela, textvariable=self.txt_sobrenome_cliente)
        self.ent_cpf_clienteo = Entry(self.janela, textvariable=self.txt_cpf_cliente)
        self.ent_login_cliente = Entry(self.janela, textvariable=self.txt_login_cliente)
        self.ent_senha_cliente = Entry(self.janela, textvariable=self.txt_senha_cliente)
        self.ent_email_cliente = Entry(self.janela, textvariable=self.txt_email_cliente)

        self.bnt_registrar_cliente = Button(self.janela, width = 15, text="Comfirmar")
        self.btn_sair = Button(self.janela, width = 15, text="Sair")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lbl_nome_cliente.grid(row = 1, column = 0)
        self.lbl_sobrenome_cliente.grid(row = 2, column = 0)
        self.lbl_cpf_cliente.grid(row = 3, column = 0)
        self.lbl_email_cliente.grid(row = 4, column = 0)
        self.lbl_login_cliente.grid(row = 5, column = 0)
        self.lbl_senha_cliente.grid(row = 6, column = 0)
        self.ent_nome_cliente.grid(row = 1, column = 1)
        self.ent_sobrenome_cliente.grid(row = 2, column = 1)
        self.ent_cpf_clienteo.grid(row = 3, column = 1)
        self.ent_login_cliente.grid(row = 4, column = 1)
        self.ent_senha_cliente.grid(row = 5, column = 1)
        self.ent_email_cliente.grid(row = 6, column = 1)
        self.bnt_registrar_cliente.grid(row = 7, column = 0)
        self.btn_sair.grid(row = 7, column = 1)
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()