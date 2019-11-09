from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_cliente(Tela):
    '''Classe que modela a interface grafica da tela do cliente depois de feito o login'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("cliente - DELIBRARY")

        self.txt_id_livro = StringVar()
        self.txt_nome_livro = StringVar()
        self.txt_genero_livro = StringVar()
        self.txt_autor_livro = StringVar()
        self.txt_area_livro = StringVar()
        self.txt_editora_livro = StringVar()
        self.txt_edicao_livro = StringVar()

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
        self.btn_ver_livros = Button(self.janela, width = 15, text ="Ver meus livros")
        self.btn_renovar = Button(self.janela, width = 15, text ="Renovar")
        self.btn_sair = Button(self.janela, width = 15, text ="Sair")

        self.txt_id_livro_renova = StringVar()
        self.lbl_renovar_livro = Label(self.janela, text = "Renovar livro")
        self.lbl_id_livro_renova = Label(self.janela, text = "ID")
        self.ent_id_livro_renova = Entry(self.janela,textvariable=self.txt_id_livro_renova)

        self.list = Listbox(self.janela, width=85)
        self.scroll = Scrollbar(self.janela)
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_pesquisar_livro.grid(row = 0, column=0)
        self.lbl_id_livro.grid(row=1,column=0)
        self.lbl_nome_livro.grid(row=2,column=0)
        self.lbl_genero_livro.grid(row=3,column=0)
        self.lbl_autor_livro.grid(row=4,column=0)  
        self.lbl_area_livro.grid(row=5,column=0) 
        self.lbl_editora_livro.grid(row=6,column=0)
        self.lbl_edicao_livro.grid(row=7,column=0)
        self.ent_id_livro.grid(row = 1, column = 1)
        self.ent_nome_livro.grid(row = 2, column = 1)
        self.ent_genero_livro.grid(row = 3, column = 1)
        self.ent_autor_livro.grid(row = 4, column = 1)
        self.ent_area_livro.grid(row = 5, column = 1)
        self.ent_editora_livro.grid(row = 6, column = 1)
        self.ent_edicao_livro.grid(row = 7, column = 1)
        self.btn_pesquisar.grid(row = 8, column = 0)
        self.btn_ver_livros.grid(row = 9, column = 0)

        self.lbl_renovar_livro.grid(row = 10, column = 0)
        self.lbl_id_livro_renova.grid(row = 11, column = 0)
        self.ent_id_livro_renova.grid(row = 11, column = 1)
        self.btn_renovar.grid(row = 12, column = 0)
        self.btn_sair.grid(row = 13, column = 0)

        self.list.grid(row=1, column=2,rowspan=7)
        self.scroll.grid(row=1, column=3, rowspan=7)
        self.list.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.list.yview)
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout() 
        return super().iniciar()