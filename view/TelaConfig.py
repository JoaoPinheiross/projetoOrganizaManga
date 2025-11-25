import customtkinter as ct

from view.BaseView import BaseFrame, BaseTela

class TelaConfig(BaseFrame):
    def __init__(self, tela: BaseTela, controller):
        super().__init__(tela, controller)

        fonte = ct.CTkFont(size=24, weight="bold")
        self.labelTitulo = ct.CTkLabel(self, text="Configurações", font=fonte)
        self.labelTitulo.grid(row=1, column=2, pady=50)

        self.btnVoltar = ct.CTkButton(self, text="Voltar", command=lambda: self.controller.trocaFrame("menu"))
        self.btnVoltar.grid(row=2, column=1, pady=10)

        # Centraliza tela
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(self.grid_size()[1] + 1, weight=1)