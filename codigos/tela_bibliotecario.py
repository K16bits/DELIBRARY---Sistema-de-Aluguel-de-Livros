from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_bibliotecario(Tela):
    '''Classe que modela a interface grafica da tela do bibliotecario depois de feito o login'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("bibliotecario - DELIBRARY")

        self.txt_nome_cliente = StringVar()
        self.txt_sobrenome_cliente = StringVar()
        self.txt_cpf_cliente = StringVar()
        self.txt_login_cliente = StringVar()
        self.txt_senha_cliente = StringVar()
        self.txt_email_cliente = StringVar()

        self.txt_id_livro = StringVar()
        self.txt_nome_livro = StringVar()
        self.txt_genero_livro = StringVar()
        self.txt_autor_livro = StringVar()
        self.txt_area_livro = StringVar()
        self.txt_editora_livro = StringVar()
        self.txt_edicao_livro = StringVar()

        self.lbl_janela_cliente = Label(self.janela, text="ATUALIZAR CADASTRO DE CLIENTE")
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

        self.btn_criar_acesso_cliente = Button(self.janela, width = 15, text="Criar Acesso")
        self.btn_retirar_acesso_cliente = Button(self.janela, width = 15, text="Retirar Acesso")
        self.btn_ver_todos_cliente = Button(self.janela, width = 15, text="Ver Todos")
        self.btn_atualizar = Button(self.janela, width = 15, text="Atualizar")
        self.btn_realizar_emprestimo_devolucao = Button(self.janela, width = 15, text="Emprestimo/Devolucao")
        self.btn_fechar = Button(self.janela, width = 15, text="Sair")

        self.list = Listbox(self.janela, width=72)
        self.scroll = Scrollbar(self.janela)

        self.lbl_janela_livro = Label(self.janela, text="CADASTRO DE LIVRO")
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

        self.btn_cadastro_livro = Button(self.janela, width = 15, text="Cadastrar Livro")
        self.btn_retirar_livro = Button(self.janela, width = 15, text="Retirar Livro")

    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lbl_janela_cliente.grid(row = 0, column = 0)
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
        self.btn_criar_acesso_cliente.grid(row = 7, column = 0) 
        self.btn_retirar_acesso_cliente.grid(row = 7, column = 1)
        self.btn_ver_todos_cliente.grid(row = 8, column = 0)
        self.btn_atualizar.grid(row = 8, column = 1)
        self.list.grid(row=1, column=3,rowspan=16)
        self.scroll.grid(row=1, column=4, rowspan=16)
        self.list.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.list.yview)

        self.lbl_janela_livro.grid(row = 9, column = 0)
        self.lbl_id_livro.grid(row = 10, column =0)
        self.lbl_nome_livro.grid(row = 11, column = 0)
        self.lbl_genero_livro.grid(row = 12, column = 0)
        self.lbl_autor_livro.grid(row = 13, column = 0)
        self.lbl_area_livro.grid(row = 14, column = 0)
        self.lbl_editora_livro.grid(row = 15, column = 0)
        self.lbl_edicao_livro.grid(row = 16, column = 0)
        self.ent_id_livro.grid(row = 10, column = 1)
        self.ent_nome_livro.grid(row = 11, column = 1)
        self.ent_genero_livro.grid(row = 12, column = 1)
        self.ent_autor_livro.grid(row = 13, column = 1)
        self.ent_area_livro.grid(row = 14, column = 1)
        self.ent_editora_livro.grid(row = 15, column = 1)
        self.ent_edicao_livro.grid(row = 16, column = 1)
        self.btn_cadastro_livro.grid(row = 17, column = 0)
        self.btn_retirar_livro.grid(row = 17, column = 1)
        self.btn_realizar_emprestimo_devolucao.grid(row = 18, column = 0)
        self.btn_fechar.grid(row = 19, column = 0)
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()