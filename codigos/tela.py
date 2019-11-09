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