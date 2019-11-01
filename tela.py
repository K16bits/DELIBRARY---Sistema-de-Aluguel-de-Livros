from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button

class Tela_inicial():
    '''Classe que modela a interface grafica da tela inicial'''
    def __init__(self):
        self.janela_inicial = Tk()
        self.janela_inicial.wm_title("DELIBRARY")
        self.janela_inicial.geometry("600x400+100+100")
        
        self.lb_janela_inicial = Label(self.janela_inicial, text = "ENTRAR NO SISTEMA COMO: ")
        
        self.btn_administrador = Button(self.janela_inicial, width = 15, text="Administrador")
        self.btn_bibliotecario = Button(self.janela_inicial, width = 15, text="Bibliotecario")
        self.btn_cliente = Button(self.janela_inicial, width = 15, text="Cliente")        
        self.btn_fechar = Button(self.janela_inicial, width = 15, text="Sair")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_inicial.grid(row=0,column=0)
        self.btn_administrador.grid(row=1,column=0)
        self.btn_bibliotecario.grid(row=2,column=0)
        self.btn_cliente.grid(row=3,column=0)
        self.btn_fechar.grid(row=4,column=0)
    def configure_sizes(self):
        '''definindo o tamanho dos elementos'''
        x_pad = 5
        y_pad = 3

        for child in self.janela_inicial.winfo_children():
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
        self.config_layout()
        self.configure_sizes()
        self.janela_inicial.mainloop()
        
class Tela_administrador_login():
    '''Classe que modela a interface grafica da tela de login do administrador'''
    def __init__(self):
        self.janela_administrador_login = Tk()
        self.janela_administrador_login.geometry("600x400+100+100")
        self.janela_administrador_login.wm_title("administrador - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        
        self.ent_login = Entry(self.janela_administrador_login, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela_administrador_login, textvariable=self.txt_senha)       
        
        self.btn_voltar_tela = Button(self.janela_administrador_login, width = 15, text = "Voltar")
        self.btn_login = Button(self.janela_administrador_login, width = 15, text = "Entrar")
        
        self.lb_janela_administrador_login = Label(self.janela_administrador_login, text = "LOGIN: ")
        self.lb_janela_administrador_senha = Label(self.janela_administrador_login, text = "SENHA: ")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_administrador_login.grid(row=0,column=0)
        self.lb_janela_administrador_senha.grid(row=1,column=0)
        self.ent_login.grid(row=0,column=1)
        self.ent_senha.grid(row=1,column=1)
        self.btn_login.grid(row=2,column=1)
        self.btn_voltar_tela.grid(row=3,column=1)
    def configure_sizes(self):
        '''definindo o tamanho dos elementos'''
        x_pad = 5
        y_pad = 3

        for child in self.janela_administrador_login.winfo_children():
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
        self.config_layout()
        self.configure_sizes()
        self.janela_administrador_login.mainloop() 

class Tela_bibliotecario_login():
    '''Classe que modela a interface grafica da tela de login do bibliotecario'''
    def __init__(self):
        self.janela_bibliotecario_login = Tk()
        self.janela_bibliotecario_login.geometry("600x400+100+100")
        self.janela_bibliotecario_login.wm_title("bibliotecario - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()

        self.ent_login = Entry(self.janela_bibliotecario_login, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela_bibliotecario_login, textvariable=self.txt_senha)  

        self.btn_voltar_tela = Button(self.janela_bibliotecario_login, width = 15, text = "Voltar")
        self.btn_login = Button(self.janela_bibliotecario_login, width = 15, text = "Entrar")

        self.lb_janela_bibliotecario_login = Label(self.janela_bibliotecario_login, text = "LOGIN: ")
        self.lb_janela_bibliotecario_senha = Label(self.janela_bibliotecario_login, text = "SENHA: ")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_bibliotecario_login.grid(row=0,column=0)
        self.lb_janela_bibliotecario_senha.grid(row=1,column=0)
        self.ent_login.grid(row=0,column=1)
        self.ent_senha.grid(row=1,column=1)
        self.btn_login.grid(row=2,column=1)
        self.btn_voltar_tela.grid(row=3,column=1)
    def configure_sizes(self):
        '''definindo o tamanho dos elementos'''
        x_pad = 5
        y_pad = 3

        for child in self.janela_bibliotecario_login.winfo_children():
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
        self.config_layout()
        self.configure_sizes()
        self.janela_bibliotecario_login.mainloop()
         
class Tela_cliente_login():
    '''Classe que modela a interface grafica da tela de login do cliente'''
    def __init__(self):
        self.janela_cliente_login = Tk()
        self.janela_cliente_login.geometry("600x400+100+100")
        self.janela_cliente_login.wm_title("cliente - DELIBRARY")

        self.txt_login = StringVar()
        self.txt_senha = StringVar()

        self.ent_login = Entry(self.janela_cliente_login, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela_cliente_login, textvariable=self.txt_senha)  

        self.btn_voltar_tela = Button(self.janela_cliente_login, width = 15, text = "Voltar")
        self.btn_login = Button(self.janela_cliente_login, width = 15, text = "Entrar")

        self.lb_janela_cliente_login = Label(self.janela_cliente_login, text = "LOGIN: ")
        self.lb_janela_cliente_senha = Label(self.janela_cliente_login, text = "SENHA: ")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lb_janela_cliente_login.grid(row=0,column=0)
        self.lb_janela_cliente_senha.grid(row=1,column=0)
        self.ent_login.grid(row=0,column=1)
        self.ent_senha.grid(row=1,column=1)
        self.btn_login.grid(row=2,column=1)
        self.btn_voltar_tela.grid(row=3,column=1)
    def configure_sizes(self):
        '''definindo o tamanho dos elementos'''
        x_pad = 5
        y_pad = 3

        for child in self.janela_cliente_login.winfo_children():
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
        self.config_layout()
        self.configure_sizes()
        self.janela_cliente_login.mainloop()

class Tela_cliente():
    '''Classe que modela a interface grafica da tela do cliente depois de feito o login'''
    def __init__(self):
        self.janela_cliente = Tk()
        self.janela_cliente.geometry("600x400+100+100")
        self.janela_cliente.wm_title("cliente - DELIBRARY")
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.janela_cliente.mainloop()

class Tela_bibliotecario():
    '''Classe que modela a interface grafica da tela do bibliotecario depois de feito o login'''
    def __init__(self):
        self.janela_bibliotecario = Tk()
        self.janela_bibliotecario.geometry("600x400+100+100")
        self.janela_bibliotecario.wm_title("bibliotecario - DELIBRARY")
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.janela_bibliotecario.mainloop()

class Tela_administrador():
    '''Classe que modela a interface grafica da tela do administrador depois de feito o login'''
    def __init__(self):
        self.janela_administrador = Tk()
        self.janela_administrador.geometry("600x400+100+100")
        self.janela_administrador.wm_title("administrador - DELIBRARY")

        self.txt_nome = StringVar()
        self.txt_sobrenome = StringVar()
        self.txt_cpf = StringVar()
        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        self.txt_email = StringVar()

        self.lbl_nome = Label(self.janela_administrador, text="Nome:")
        self.lbl_sobrenome = Label(self.janela_administrador, text="Sobrenome:")
        self.lbl_cpf = Label(self.janela_administrador, text="CPF:")
        self.lbl_login = Label(self.janela_administrador, text="Criar login:")
        self.lbl_senha = Label(self.janela_administrador, text="Criar senha:")
        self.lbl_email = Label(self.janela_administrador, text = "Email: ")

        self.ent_nome = Entry(self.janela_administrador, textvariable=self.txt_nome)
        self.ent_sobrenome = Entry(self.janela_administrador, textvariable=self.txt_sobrenome)
        self.ent_cpf = Entry(self.janela_administrador, textvariable=self.txt_cpf)
        self.ent_login = Entry(self.janela_administrador, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela_administrador, textvariable=self.txt_senha)
        self.ent_email = Entry(self.janela_administrador, textvariable=self.txt_email)
        
        self.btn_criar_acesso_bibliotecario = Button(self.janela_administrador, width = 15, text="Criar Acesso")
        self.btn_retirar_acesso_bibliotecario = Button(self.janela_administrador, width = 15, text="Retirar Acesso")
        self.btn_ver_todos_bibliotecario = Button(self.janela_administrador, width = 15, text="Ver Todos")
        self.btn_fechar = Button(self.janela_administrador, width = 15, text="Sair")

        self.list_bibliotecario = Listbox(self.janela_administrador, width=52)
        self.scroll_bibliotecario = Scrollbar(self.janela_administrador)
    def configure_sizes(self):
        '''definindo o tamanho dos elementos'''
        x_pad = 5
        y_pad = 3

        for child in self.janela_administrador.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            elif widget_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    def configure_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lbl_nome.grid(row = 0, column = 1)
        self.lbl_sobrenome.grid(row = 1, column = 1)
        self.lbl_cpf.grid(row = 2, column = 1)
        self.lbl_email.grid(row = 3, column = 1)
        self.lbl_login.grid(row = 4, column = 1)
        self.lbl_senha.grid(row = 5, column = 1)
        self.btn_ver_todos_bibliotecario.grid(row = 6, column = 1)
        self.btn_criar_acesso_bibliotecario.grid(row = 7, column = 1)
        self.btn_retirar_acesso_bibliotecario.grid(row = 8, column = 1)
        self.btn_fechar.grid(row = 9, column = 1)
        self.ent_nome.grid(row = 0, column = 2)
        self.ent_sobrenome.grid(row = 1, column = 2)
        self.ent_cpf.grid(row = 2, column = 2)
        self.ent_email.grid(row = 3, column = 2)
        self.ent_login.grid(row = 4, column = 2)
        self.ent_senha.grid(row = 5, column = 2)
        self.list_bibliotecario.grid(row=0, column=3,rowspan=10)
        self.scroll_bibliotecario.grid(row=0, column=4, rowspan=10)
        self.list_bibliotecario.configure(yscrollcommand=self.scroll_bibliotecario.set)
        self.scroll_bibliotecario.configure(command=self.list_bibliotecario.yview)

    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.configure_layout()
        self.configure_sizes()
        self.janela_administrador.mainloop()



