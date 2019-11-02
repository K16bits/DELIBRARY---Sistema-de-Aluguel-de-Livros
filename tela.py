from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button

class Tela():
    '''classe pai para as telas'''
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("600x400+100+100")
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
    # def configure_sizes(self):
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()        
    # def iniciar(self):
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
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        return super().iniciar()

class Tela_bibliotecario(Tela):
    '''Classe que modela a interface grafica da tela do bibliotecario depois de feito o login'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("bibliotecario - DELIBRARY")
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        return super().iniciar()

class Tela_administrador(Tela):
    '''Classe que modela a interface grafica da tela do administrador depois de feito o login'''
    def __init__(self):
        super().__init__()
        self.janela.wm_title("administrador - DELIBRARY")

        self.txt_nome = StringVar()
        self.txt_sobrenome = StringVar()
        self.txt_cpf = StringVar()
        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        self.txt_email = StringVar()

        self.lbl_nome = Label(self.janela, text="Nome:")
        self.lbl_sobrenome = Label(self.janela, text="Sobrenome:")
        self.lbl_cpf = Label(self.janela, text="CPF:")
        self.lbl_login = Label(self.janela, text="Criar login:")
        self.lbl_senha = Label(self.janela, text="Criar senha:")
        self.lbl_email = Label(self.janela, text = "Email: ")

        self.ent_nome = Entry(self.janela, textvariable=self.txt_nome)
        self.ent_sobrenome = Entry(self.janela, textvariable=self.txt_sobrenome)
        self.ent_cpf = Entry(self.janela, textvariable=self.txt_cpf)
        self.ent_login = Entry(self.janela, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela, textvariable=self.txt_senha)
        self.ent_email = Entry(self.janela, textvariable=self.txt_email)
        
        self.btn_criar_acesso_bibliotecario = Button(self.janela, width = 15, text="Criar Acesso")
        self.btn_retirar_acesso_bibliotecario = Button(self.janela, width = 15, text="Retirar Acesso")
        self.btn_ver_todos_bibliotecario = Button(self.janela, width = 15, text="Ver Todos")
        self.btn_fechar = Button(self.janela, width = 15, text="Sair")

        self.list_bibliotecario = Listbox(self.janela, width=52)
        self.scroll_bibliotecario = Scrollbar(self.janela)
    def config_sizes(self):
        '''definindo o tamanho dos elementos'''
        return super().config_sizes()   
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
        self.config_layout()
        return super().iniciar()