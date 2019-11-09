from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_cliente_login(Tela):
    '''Classe que modela a interface grafica da tela de login do cliente'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("cliente - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        self.txt_id_livro = StringVar()
        self.txt_nome_livro = StringVar()
        self.txt_genero_livro = StringVar()
        self.txt_autor_livro = StringVar()
        self.txt_area_livro = StringVar()
        self.txt_editora_livro = StringVar()
        self.txt_edicao_livro = StringVar()

        self.ent_login = Entry(self.janela, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela, textvariable=self.txt_senha, show="*")  

        self.btn_voltar_tela = Button(self.janela, width = 15, text = "Voltar")
        self.btn_login = Button(self.janela, width = 15, text = "Entrar")
        self.btn_cadastro = Button(self.janela,  width = 15, text ="Cadastrar")

        self.lb_janela_cliente_login = Label(self.janela, text = "LOGIN: ")
        self.lb_janela_cliente_senha = Label(self.janela, text = "SENHA: ")
        self.lb_pesquisar_livro = Label(self.janela, text = "Pesquisar livro")
        self.lbl_id_livro = Label(self.janela, text = "ID")
        self.lbl_nome_livro = Label(self.janela,text="Nome")
        self.lbl_genero_livro = Label(self.janela,text="Genero")
        self.lbl_autor_livro = Label(self.janela,text="Autor")
        self.lbl_area_livro = Label(self.janela,text="Area")
        self.lbl_editora_livro = Label(self.janela,text="Editora")
        self.lbl_edicao_livro = Label(self.janela,text="Edicao")

        self.ent_id_livro = Entry(self.janela,textvariable=self.txt_id_livro)
        self.ent_nome_livro = Entry(self.janela, textvariable=self.txt_nome_livro)
        self.ent_genero_livro = Entry(self.janela, textvariable=self.txt_genero_livro)
        self.ent_autor_livro = Entry(self.janela, textvariable=self.txt_autor_livro)
        self.ent_area_livro = Entry(self.janela, textvariable=self.txt_area_livro)
        self.ent_editora_livro = Entry(self.janela, textvariable=self.txt_editora_livro)
        self.ent_edicao_livro = Entry(self.janela, textvariable=self.txt_edicao_livro)
        self.btn_pesquisar = Button(self.janela, width = 15, text ="Pesquisar")

        self.list = Listbox(self.janela, width=85)
        self.scroll = Scrollbar(self.janela)
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_cliente_login.grid(row=0,column=0)
        self.lb_janela_cliente_senha.grid(row=1,column=0)
        self.ent_login.grid(row=0,column=1)
        self.ent_senha.grid(row=1,column=1)
        self.btn_login.grid(row=2,column=1)
        self.btn_cadastro.grid(row = 2, column = 0)
        self.btn_voltar_tela.grid(row=3,column=1)  
        self.lb_pesquisar_livro.grid(row = 4, column=0)
        self.list.grid(row=5, column=2,rowspan=10)
        self.scroll.grid(row=5, column=3, rowspan=10)
        self.list.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.list.yview)
        self.lbl_id_livro.grid(row=5,column=0)
        self.lbl_nome_livro.grid(row=6,column=0)
        self.lbl_genero_livro.grid(row=7,column=0)
        self.lbl_autor_livro.grid(row=8,column=0)  
        self.lbl_area_livro.grid(row=9,column=0) 
        self.lbl_editora_livro.grid(row=10,column=0)
        self.lbl_edicao_livro.grid(row=11,column=0)
        self.ent_id_livro.grid(row = 5, column = 1)
        self.ent_nome_livro.grid(row = 6, column = 1)
        self.ent_genero_livro.grid(row = 7, column = 1)
        self.ent_autor_livro.grid(row = 8, column = 1)
        self.ent_area_livro.grid(row = 9, column = 1)
        self.ent_editora_livro.grid(row = 10, column = 1)
        self.ent_edicao_livro.grid(row = 11, column = 1)
        self.btn_pesquisar.grid(row = 12, column = 0)
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()