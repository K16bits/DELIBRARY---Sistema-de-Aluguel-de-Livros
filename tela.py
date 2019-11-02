from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button

class Tela():
    '''classe pai para as telas'''
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("800x600+50+50")
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        x_pad = 5
        y_pad = 3
        for child in self.janela.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_sizes()
        self.janela.mainloop()

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
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()        
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()
    
class Tela_administrador_login(Tela):
    '''Classe que modela a interface grafica da tela de login do administrador'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("administrador - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        
        self.ent_login = Entry(self.janela, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela, textvariable=self.txt_senha)       
        
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
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()   
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()

class Tela_bibliotecario_login(Tela):
    '''Classe que modela a interface grafica da tela de login do bibliotecario'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("bibliotecario - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()

        self.ent_login = Entry(self.janela, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela, textvariable=self.txt_senha)  

        self.btn_voltar_tela = Button(self.janela, width = 15, text = "Voltar")
        self.btn_login = Button(self.janela, width = 15, text = "Entrar")

        self.lb_janela_bibliotecario_login = Label(self.janela, text = "LOGIN: ")
        self.lb_janela_bibliotecario_senha = Label(self.janela, text = "SENHA: ")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_bibliotecario_login.grid(row=0,column=0)
        self.lb_janela_bibliotecario_senha.grid(row=1,column=0)
        self.ent_login.grid(row=0,column=1)
        self.ent_senha.grid(row=1,column=1)
        self.btn_login.grid(row=2,column=1)
        self.btn_voltar_tela.grid(row=3,column=1)
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()   
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()
         
class Tela_cliente_login(Tela):
    '''Classe que modela a interface grafica da tela de login do cliente'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("cliente - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()

        self.ent_login = Entry(self.janela, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela, textvariable=self.txt_senha)  

        self.btn_voltar_tela = Button(self.janela, width = 15, text = "Voltar")
        self.btn_login = Button(self.janela, width = 15, text = "Entrar")

        self.lb_janela_cliente_login = Label(self.janela, text = "LOGIN: ")
        self.lb_janela_cliente_senha = Label(self.janela, text = "SENHA: ")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_cliente_login.grid(row=0,column=0)
        self.lb_janela_cliente_senha.grid(row=1,column=0)
        self.ent_login.grid(row=0,column=1)
        self.ent_senha.grid(row=1,column=1)
        self.btn_login.grid(row=2,column=1)
        self.btn_voltar_tela.grid(row=3,column=1)
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()   
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()

class Tela_cliente(Tela):
    '''Classe que modela a interface grafica da tela do cliente depois de feito o login'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("cliente - DELIBRARY")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        pass
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        # self.config_layout()
        return super().iniciar()

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

        self.txt_nome_livro = StringVar()
        self.txt_genero_livro = StringVar()
        self.txt_autor_livro = StringVar()
        self.txt_area_livro = StringVar()
        self.txt_editora_livro = StringVar()
        self.txt_edicao_livro = StringVar()

        self.lbl_janela_cliente = Label(self.janela, text="CADASTRO DE CLIENTE")
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

        self.list_cliente = Listbox(self.janela, width=83)
        self.scroll_cliente = Scrollbar(self.janela)

        self.lbl_janela_livro = Label(self.janela, text="CADASTRO DE LIVRO")
        self.lbl_nome_livro = Label(self.janela,text="Nome")
        self.lbl_genero_livro = Label(self.janela,text="Genero")
        self.lbl_autor_livro = Label(self.janela,text="Autor")
        self.lbl_area_livro = Label(self.janela,text="Area")
        self.lbl_editora_livro = Label(self.janela,text="Editora")
        self.lbl_edicao_livro = Label(self.janela,text="Edicao")

        self.ent_nome_livro = Entry(self.janela, textvariable=self.txt_nome_livro)
        self.ent_genero_livro = Entry(self.janela, textvariable=self.txt_genero_livro)
        self.ent_autor_livro = Entry(self.janela, textvariable=self.txt_autor_livro)
        self.ent_area_livro = Entry(self.janela, textvariable=self.txt_area_livro)
        self.ent_editora_livro = Entry(self.janela, textvariable=self.txt_editora_livro)
        self.ent_edicao_livro = Entry(self.janela, textvariable=self.txt_edicao_livro)

        self.btn_cadastro_livro = Button(self.janela, width = 15, text="Cadastrar Livro")
        self.btn_retirar_livro = Button(self.janela, width = 15, text="Retirar Livro")


        self.list_livro = Listbox(self.janela, width=83)
        self.scroll_livro = Scrollbar(self.janela)
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()  
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
        self.list_cliente.grid(row=1, column=3,rowspan=7)
        self.scroll_cliente.grid(row=1, column=4, rowspan=7)
        self.list_cliente.configure(yscrollcommand=self.scroll_cliente.set)
        self.scroll_cliente.configure(command=self.list_cliente.yview)

        self.lbl_janela_livro.grid(row = 9, column = 0)
        self.lbl_nome_livro.grid(row = 10, column = 0)
        self.lbl_genero_livro.grid(row = 11, column = 0)
        self.lbl_autor_livro.grid(row = 12, column = 0)
        self.lbl_area_livro.grid(row = 13, column = 0)
        self.lbl_editora_livro.grid(row = 14, column = 0)
        self.lbl_edicao_livro.grid(row = 15, column = 0)
        self.ent_nome_livro.grid(row = 10, column = 1)
        self.ent_genero_livro.grid(row = 11, column = 1)
        self.ent_autor_livro.grid(row = 12, column = 1)
        self.ent_area_livro.grid(row = 13, column = 1)
        self.ent_editora_livro.grid(row = 14, column = 1)
        self.ent_edicao_livro.grid(row = 15, column = 1)
        self.btn_cadastro_livro.grid(row = 16, column = 0)
        self.btn_retirar_livro.grid(row = 16, column = 1)
        self.list_livro.grid(row=10, column=3,rowspan=7)
        self.scroll_livro.grid(row=10, column=4, rowspan=7)
        self.list_livro.configure(yscrollcommand=self.scroll_livro.set)
        self.scroll_livro.configure(command=self.list_livro.yview)

    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()

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
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()   
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