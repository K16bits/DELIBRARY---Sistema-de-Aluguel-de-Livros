from tkinter import Tk, StringVar, Label, Entry, Listbox, Scrollbar, Button
from tela import Tela

class Tela_emprestimo_devolucao(Tela):
    '''Classe que modela a interface grafica da tela para realizar emprestimo e devolucao do livro'''
    def __init__(self):
        self.janela = Tk()
        self.janela.wm_title("emprestimo/devolucao - DELIBRARY")
        self.janela.geometry("800x200+50+50")

        self.txt_id_livro = StringVar()
        self.txt_cpf_cliente = StringVar()
        
        self.lbl_id_livro = Label(self.janela, text="Id do livro")
        self.lbl_cpf_cliente = Label(self.janela, text="CPF do cliente")

        self.ent_id_livro = Entry(self.janela,textvariable=self.txt_id_livro)
        self.ent_cpf_cliente = Entry(self.janela,textvariable=self.txt_cpf_cliente)

        self.btn_emprestimo = Button(self.janela, width = 15, text="Emprestimo")
        self.btn_devolucao = Button(self.janela, width = 15, text="Devolução")
        self.btn_sair = Button(self.janela, width = 15, text="Sair")
    def config_layout(self):
        '''Metodo para configurar os widgets da janela'''
        self.lbl_id_livro.grid(row = 0, column = 0)
        self.lbl_cpf_cliente.grid(row = 1, column = 0)
        self.ent_id_livro.grid(row = 0, column = 1)
        self.ent_cpf_cliente.grid(row = 1, column = 1)
        self.btn_emprestimo.grid(row = 2, column = 0)
        self.btn_devolucao.grid(row = 2, column = 1)
        self.btn_sair.grid(row = 3, column = 0)
    def iniciar(self):
        '''Metodo para desenhar a janela e processar eventos'''
        self.config_layout()
        return super().iniciar()