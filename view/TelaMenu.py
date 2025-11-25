import tkinter as tk
import customtkinter as ct
import tkinter.messagebox as msg

from view.BaseView import BaseFrame, BaseTela

class TelaMenu(BaseFrame):
    def __init__(self, tela: BaseTela, control):
        super().__init__(tela, control)
        self.control = control

        # Botão
        fonte = ct.CTkFont(size=24, weight="bold")
        self.labelTitulo = ct.CTkLabel(self, text="Organizador De Mangas", font=fonte)
        self.labelTitulo.grid(row=1, column=1, pady=50)

        self.btnOrg = ct.CTkButton(self, text="Organizar Manga", command=lambda: self.organizarManga())
        self.btnOrg.grid(row=2, column=1, pady=10)

        self.btnConfig = ct.CTkButton(self, text="Configuração", command=lambda: self.control.trocaFrame("config"))
        self.btnConfig.grid(row=3, column=1, pady=10)

        self.btnConv = ct.CTkButton(self, text="Converter Manga")
        self.btnConv.grid(row=4, column=1, pady=10)

        self.btnCapa = ct.CTkButton(self, text="Baixar Capa")
        self.btnCapa.grid(row=5, column=1, pady=10)

        self.btnSair = ct.CTkButton(self, text="Sair", command=lambda: self.control.encerrar())
        self.btnSair.grid(row=6, column=1, pady=10)

        # Centraliza tela
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(self.grid_size()[1] + 1, weight=1)
    
    def organizarManga(self) -> None:
        organizou = self.control.organizarManga()
        if organizou:
            msg.showinfo("Organizador De Mangas", "Manga organizado com sucesso!")
        else:
            msg.showerror("Organizador De Mangas", "Ocorreu algum erro ao organizar o manga.")