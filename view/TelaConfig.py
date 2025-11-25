# importando bibliotecas
import customtkinter as ct
from tkinter import ttk
import tkinter as tk

# importando módulos
from view.BaseView import BaseFrame, BaseTela

class TelaConfig(BaseFrame):
    # Construtor
    def __init__(self, tela: BaseTela, controller):
        super().__init__(tela, controller)

        # Recebe os dados da configuração atual
        self.dados = [self.controller.listaConfig()]

        # -- Título da tela --
        fonte = ct.CTkFont(size=24, weight="bold")
        self.labelTitulo = ct.CTkLabel(self, text="Configurações", font=fonte)
        self.labelTitulo.grid(row=1, column=1, pady=50)
        
        # -- TreeView --
        # Frame do TreeView
        self.frameConfigAtual = ct.CTkFrame(self)
        self.frameConfigAtual.grid(row=2, column=1)

        # Criando o TreeView
        self.tree = ttk.Treeview(
            self.frameConfigAtual,
            columns=('Manga', 'Volume', 'Capítulo'),
            show='headings',
            selectmode='none',
            height=1
        )
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Configuração do cabeçalho
        self.tree.heading('Manga', text='Título do Manga', anchor=tk.W)
        self.tree.heading('Volume', text='Volume', anchor=tk.CENTER)
        self.tree.heading('Capítulo', text='Capítulo', anchor=tk.CENTER)

        # Configuração das colunas
        self.tree.column('Manga', width=200, stretch=tk.NO, anchor=tk.W)
        self.tree.column('Volume', width=100, anchor=tk.CENTER)
        self.tree.column('Capítulo', width=100, anchor=tk.CENTER)

        # Estiliazação do TreeView
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="#1f1f1f",
            fieldbackground="#1f1f1f",
            foreground="white",
            )
        style.configure(
            "Treeview.Heading",
            background="#2b2b2b",
            foreground="white",
            relief="flat"
        )
        style.map("Custom.Treeview", 
            background=[('selected', '#1f538d')], # Opcional: mantém a seleção CTk
            foreground=[('selected', 'white')]    # Opcional: mantém o texto branco na seleção
        )

        # -- Botão de Voltar --
        self.btnVoltar = ct.CTkButton(self, text="Voltar", command=lambda: self.controller.trocaFrame("menu"))
        self.btnVoltar.grid(row=4, column=0, pady=10, padx=10, sticky='sw')

        # -- Botão de Alinhamento
        self.btn1 = ct.CTkButton(
            self, 
            text="Voltar", 
            fg_color='#2b2b2b',           # Cor de fundo do botão
            hover_color='#2b2b2b',        # Cor quando o mouse passa sobre ele
            text_color='#2b2b2b'
            
        )
        self.btn1.grid(row=4, column=2, pady=10, padx=10)

        # Centralização da tela
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.popularConfig()

    def popularConfig(self):
        for item in self.dados:
            self.tree.insert('', tk.END, values=item)