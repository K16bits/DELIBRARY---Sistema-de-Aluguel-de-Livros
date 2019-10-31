from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, Place

class Tela_inicial():
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
        self.lb_janela_inicial.place(x=0,y=0)
        self.btn_administrador.place(x=0,y=30)
        self.btn_bibliotecario.place(x=0,y=60)
        self.btn_cliente.place(x=0,y=90)
        self.btn_fechar.place(x=0,y=120)

    def iniciar(self):
        self.config_layout()
        self.janela_inicial.mainloop()
        
class Tela_administrador():
    def __init__(self):
        self.janela_administrador = Tk()
        self.janela_administrador.geometry("600x400+100+100")
        self.janela_administrador.wm_title("administrador - DELIBRARY")
        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        self.ent_login = Entry(self.janela_administrador, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela_administrador, textvariable=self.txt_senha)       
        self.btn_voltar_tela = Button(self.janela_administrador, width = 20, text = "Voltar")
        self.btn_login = Button(self.janela_administrador, width = 20, text = "Entrar")
        self.lb_janela_administrador_login = Label(self.janela_administrador, text = "LOGIN: ")
        self.lb_janela_administrador_senha = Label(self.janela_administrador, text = "SENHA: ")

    def config_layout(self):
        self.ent_login.place(x=50,y=1)
        self.ent_senha.place(x=50,y=30)
        self.lb_janela_administrador_login.place(x=0,y=0)
        self.lb_janela_administrador_senha.place(x=0,y=30)
        self.btn_login.place(x=0,y=60)
        self.btn_voltar_tela.place(x=0,y=90)

    def iniciar(self):
        self.config_layout()
        self.janela_administrador.mainloop() 

class Tela_bibliotecario():
    def __init__(self):
        self.janela_bibliotecario = Tk()
        self.janela_bibliotecario.geometry("600x400+100+100")
        self.janela_bibliotecario.wm_title("bibliotecario - DELIBRARY")
        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        self.ent_login = Entry(self.janela_bibliotecario, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela_bibliotecario, textvariable=self.txt_senha)  
        self.btn_voltar_tela = Button(self.janela_bibliotecario, width = 20, text = "Voltar")
        self.btn_login = Button(self.janela_bibliotecario, width = 20, text = "Entrar")
        self.lb_janela_bibliotecario_login = Label(self.janela_bibliotecario, text = "LOGIN: ")
        self.lb_janela_bibliotecario_senha = Label(self.janela_bibliotecario, text = "SENHA: ")


    def config_layout(self):
        self.ent_login.place(x=50,y=1)
        self.ent_senha.place(x=50,y=30)
        self.lb_janela_bibliotecario_login.place(x=0,y=0)
        self.lb_janela_bibliotecario_senha.place(x=0,y=30)
        self.btn_voltar_tela.place(x=0,y=90)
        self.btn_login.place(x=0,y=60)
    def iniciar(self):
        self.config_layout()
        self.janela_bibliotecario.mainloop()
         
class Tela_cliente():
    def __init__(self):
        self.janela_cliente = Tk()
        self.janela_cliente.geometry("600x400+100+100")
        self.janela_cliente.wm_title("cliente - DELIBRARY")
        self.txt_login = StringVar()
        self.txt_senha = StringVar()
        self.ent_login = Entry(self.janela_cliente, textvariable=self.txt_login)
        self.ent_senha = Entry(self.janela_cliente, textvariable=self.txt_senha)  
        self.btn_voltar_tela = Button(self.janela_cliente, width = 20, text = "Voltar")
        self.btn_login = Button(self.janela_cliente, width = 20, text = "Entrar")
        self.lb_janela_cliente_login = Label(self.janela_cliente, text = "LOGIN: ")
        self.lb_janela_cliente_senha = Label(self.janela_cliente, text = "SENHA: ")


    def config_layout(self):
        self.ent_login.place(x=50,y=1)
        self.ent_senha.place(x=50,y=30)
        self.lb_janela_cliente_login.place(x=0,y=0)
        self.lb_janela_cliente_senha.place(x=0,y=30)
        self.btn_login.place(x=0,y=60)
        self.btn_voltar_tela.place(x=0,y=90)
    def iniciar(self):
        self.config_layout()
        self.janela_cliente.mainloop()



