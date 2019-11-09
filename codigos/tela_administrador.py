from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_administrador(Tela):
    '''Classe que modela a interface grafica da tela do administrador depois de feito o login'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("administrador - DELIBRARY")

        self.txt_nome_bibliotecario = StringVar()
        self.txt_sobrenome_bibliotecario = StringVar()
        self.txt_cpf_bibliotecario = StringVar()
        self.txt_login_bibliotecario = StringVar()
        self.txt_senha_bibliotecario = StringVar()
        self.txt_email_bibliotecario = StringVar()

        self.lbl_janela_bibliotecario = Label(self.janela, text="CADASTRO DE BIBLIOTECARIO")
        self.lbl_nome_bibliotecario = Label(self.janela, text="Nome")
        self.lbl_sobrenome_bibliotecario = Label(self.janela, text="Sobrenome")
        self.lbl_cpf_bibliotecario = Label(self.janela, text="CPF")
        self.lbl_login_bibliotecario = Label(self.janela, text="Criar login")
        self.lbl_senha_bibliotecario = Label(self.janela, text="Criar senha")
        self.lbl_email_bibliotecario = Label(self.janela, text = "Email ")

        self.ent_nome_bibliotecario = Entry(self.janela, textvariable=self.txt_nome_bibliotecario)
        self.ent_sobrenome_bibliotecario = Entry(self.janela, textvariable=self.txt_sobrenome_bibliotecario)
        self.ent_cpf_bibliotecario = Entry(self.janela, textvariable=self.txt_cpf_bibliotecario)
        self.ent_login_bibliotecario = Entry(self.janela, textvariable=self.txt_login_bibliotecario)
        self.ent_senha_bibliotecario = Entry(self.janela, textvariable=self.txt_senha_bibliotecario)
        self.ent_email_bibliotecario = Entry(self.janela, textvariable=self.txt_email_bibliotecario)
        
        self.btn_criar_acesso_bibliotecario = Button(self.janela, width = 15, text="Criar Acesso")
        self.btn_retirar_acesso_bibliotecario = Button(self.janela, width = 15, text="Retirar Acesso")
        self.btn_ver_todos_bibliotecario = Button(self.janela, width = 15, text="Ver Todos")
        self.btn_fechar = Button(self.janela, width = 15, text="Sair")

        self.list_bibliotecario = Listbox(self.janela, width=77)
        self.scroll_bibliotecario = Scrollbar(self.janela)
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lbl_janela_bibliotecario.grid(row = 0, column = 0)
        self.lbl_nome_bibliotecario.grid(row = 1, column = 0)
        self.lbl_sobrenome_bibliotecario.grid(row = 2, column = 0)
        self.lbl_cpf_bibliotecario.grid(row = 3, column = 0)
        self.lbl_email_bibliotecario.grid(row = 4, column = 0)
        self.lbl_login_bibliotecario.grid(row = 5, column = 0)
        self.lbl_senha_bibliotecario.grid(row = 6, column = 0)
        self.btn_ver_todos_bibliotecario.grid(row = 7, column = 0)
        self.btn_criar_acesso_bibliotecario.grid(row = 8, column = 0)
        self.btn_retirar_acesso_bibliotecario.grid(row = 9, column = 0)
        self.btn_fechar.grid(row = 10, column = 0)
        self.ent_nome_bibliotecario.grid(row = 1, column = 1)
        self.ent_sobrenome_bibliotecario.grid(row = 2, column = 1)
        self.ent_cpf_bibliotecario.grid(row = 3, column = 1)
        self.ent_email_bibliotecario.grid(row = 4, column = 1)
        self.ent_login_bibliotecario.grid(row = 5, column = 1)
        self.ent_senha_bibliotecario.grid(row = 6, column = 1)
        self.list_bibliotecario.grid(row=1, column=2,rowspan=7)
        self.scroll_bibliotecario.grid(row=1, column=3, rowspan=7)
        self.list_bibliotecario.configure(yscrollcommand=self.scroll_bibliotecario.set)
        self.scroll_bibliotecario.configure(command=self.list_bibliotecario.yview)

    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()