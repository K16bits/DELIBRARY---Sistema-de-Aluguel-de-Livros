from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button

class Tela_inicial():
    '''Classe que modela a interface grafica da tela inicial'''
    def __init__(self):
        self.janela_inicial = Tk()
        self.janela_inicial.wm_title("DELIBRARY")
        self.janela_inicial.geometry("600x400+100+100")
        
        self.lb_janela_inicial = Label(self.janela_inicial, text = "ENTRAR NO SISTEMA COMO: ")
        
        self.btn_administrador = Button(self.janela_inicial, width = 20, text="Administrador")
        self.btn_bibliotecario = Button(self.janela_inicial, width = 20, text="Bibliotecario")
        self.btn_cliente = Button(self.janela_inicial, width = 20, text="Cliente")        
        self.btn_fechar = Button(self.janela_inicial, width = 20, text="Sair")
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
        
        self.btn_voltar_tela = Button(self.janela_administrador_login, width = 20, text = "Voltar")
        self.btn_login = Button(self.janela_administrador_login, width = 20, text = "Entrar")
        
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
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
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

        self.btn_voltar_tela = Button(self.janela_bibliotecario_login, width = 20, text = "Voltar")
        self.btn_login = Button(self.janela_bibliotecario_login, width = 20, text = "Entrar")

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
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
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

        self.btn_voltar_tela = Button(self.janela_cliente_login, width = 20, text = "Voltar")
        self.btn_login = Button(self.janela_cliente_login, width = 20, text = "Entrar")

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
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
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

    #     self.listClientes = Listbox(self.janela_administrador, width=45)
    #     self.scrollClientes = Scrollbar(self.janela_administrador)
    
    # def configure_layout(self):
    #     self.listClientes.grid(row=10, column=110, rowspan=50)#rowspan para fazer com que o objeto ocupe mais de uma linha.
    #     self.scrollClientes.grid(row=10, column=50, rowspan=50)
    #     self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
    #     self.scrollClientes.configure(command=self.listClientes.yview)

    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        # self.configure_layout()
        self.janela_administrador.mainloop()



