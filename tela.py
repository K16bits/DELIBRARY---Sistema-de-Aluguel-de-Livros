from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button, Place

class Tela():
    def __init__(self):
        self.janela = Tk()
        self.janela.wm_title("DELIBRARY")
        self.janela.geometry("600x400+100+100")
        self.lb_janela = Label(self.janela, text = "ENTRAR NO SISTEMA COMO: ")
        self.btn_administrador = Button(self.janela, width = 20, text="Administrador")
        self.btn_bibliotecario = Button(self.janela, width = 20, text="Bibliotecario")
        self.btn_cliente = Button(self.janela, width = 20, text="Cliente")        
        self.btn_fechar = Button(self.janela, width = 20, text="Sair")
    def config_layout(self):
        self.lb_janela.place(x=0,y=0)
        self.btn_administrador.place(x=0,y=30)
        self.btn_bibliotecario.place(x=0,y=60)
        self.btn_cliente.place(x=0,y=90)
        self.btn_fechar.place(x=0,y=120)
    def iniciar(self):
        self.config_layout()
        self.janela.mainloop()
        
class Tela_administrador():
    def __init__(self):
        self.janela_administrador = Tk()
        self.janela_administrador.geometry("600x400+100+100")
        self.janela_administrador.wm_title("administrador - DELIBRARY") 
        self.btn_voltar_tela = Button(self.janela_administrador, width = 20, text = "Voltar")
    def config_layout(self):
        self.btn_voltar_tela.place(x=0,y=120)
    def iniciar(self):
        self.config_layout()
        self.janela_administrador.mainloop() 

class Tela_bibliotecario():
    def __init__(self):
        self.janela_bibliotecario = Tk()
        self.janela_bibliotecario.geometry("600x400+100+100")
        self.janela_bibliotecario.wm_title("bibliotecario - DELIBRARY")
        self.btn_voltar_tela = Button(self.janela_bibliotecario, width = 20, text = "Voltar")
    def config_layout(self):
        self.btn_voltar_tela.place(x=0,y=120)
    def iniciar(self):
        self.config_layout()
        self.janela_bibliotecario.mainloop()
         
class Tela_cliente():
    def __init__(self):
        self.janela_cliente = Tk()
        self.janela_cliente.geometry("600x400+100+100")
        self.janela_cliente.wm_title("cliente - DELIBRARY")
        self.btn_voltar_tela = Button(self.janela_cliente, width = 20, text = "Voltar")
    def config_layout(self):
        self.btn_voltar_tela.place(x=0,y=120)
    def iniciar(self):
        self.config_layout()
        self.janela_cliente.mainloop()



