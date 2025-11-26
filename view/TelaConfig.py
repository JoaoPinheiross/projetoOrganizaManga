# importando bibliotecas
import customtkinter as ct
from tkinter import ttk
import tkinter as tk

# importando módulos
from view.BaseView import BaseFrame, BaseTela

class TelaConfig(BaseFrame):
    # -- Construtor --
    def __init__(self, tela: BaseTela, controller):
        super().__init__(tela, controller)

        # -- Atributos --
        self.idManga = 0
        self.idVolume = 0
        self.idCapitulo = 0

        self.grid(row=0, column=0, sticky="nsew")

        # -- Título da tela --
        fonte = ct.CTkFont(size=36, weight="bold")
        self.labelTitulo = ct.CTkLabel(self, text="Configurações", font=fonte)
        self.labelTitulo.grid(row=1, column=1, pady=50)

        # -- Botão de Voltar --
        self.btnVoltar = ct.CTkButton(self, text="Voltar", command=lambda: self.controller.trocaFrame("menu"))
        self.btnVoltar.grid(row=6, column=0, pady=10, padx=10, sticky='sw')

        # -- Botão de Alinhamento
        self.btn1 = ct.CTkButton(
            self,
            text="Voltar",
            fg_color='#2b2b2b',
            hover_color='#2b2b2b',
            text_color='#2b2b2b'
            
        )
        self.btn1.grid(row=4, column=2, pady=10, padx=10)

        # Centralização da tela
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.configFrameMangaAtual()
        self.configFrameSelManga()
        
    # -- Métodos --
    def configFrameMangaAtual(self) -> None:
        '''
            Configuração do frame da configuraçaõ atual do manga.
        '''
        # Recebe os dados da configuração atual
        self.dadosConfigManga = [self.controller.listaConfig()]
        
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

        self.popularConfig()

    def popularConfig(self):
        '''Preenche os dados da tabela da configuração atual do manga.
        '''
        for item in self.dadosConfigManga:
            self.tree.insert('', tk.END, values=item)

    def configFrameSelManga(self) -> None:
        '''
            Configuração do frame da seleção do manga.
        '''

        # Recebe os nomes dos mangas cadastros
        self.dadosMangas = self.controller.listarMangas()

        # -- Combo Box --
        # Frame do Combo Box
        self.frameSelManga = ct.CTkFrame(self, fg_color="#2b2b2b")
        self.frameSelManga.grid(row=3, column=1, pady=20)

        # Label Manga
        fonte = ct.CTkFont(size=18, weight="bold")
        self.labelManga = ct.CTkLabel(self.frameSelManga, text="Manga", font=fonte)
        self.labelManga.grid(row=0, column=0, sticky="nsew")

        # Criando o Combo Box
        self.comboboxManga = ct.CTkComboBox(self.frameSelManga, width=170, values=self.dadosMangas, command=self.mudarSelManga)
        self.comboboxManga.grid(row=1, column=0, sticky="nsew")

        # Define um valor padrão (opcional)
        self.comboboxManga.set("Selecione um Manga")

    def mudarSelManga(self, nomeManga: str) -> None:
        self.idManga = self.controller.pesquisarMangaPorNome(nomeManga)
        self.configFrameSelVolume(self.idManga)

    def configFrameSelVolume(self, idManga: int) -> None:
        '''
            Configuração do frame da seleção do volume.
        '''
        # Recebe os números dos volumes cadastros
        self.dadosVolumes = self.controller.listarVolumes(idManga)

        # -- Combo Box --
        # Frame do Combo Box
        self.frameSelVolume = ct.CTkFrame(self, fg_color="#2b2b2b")
        self.frameSelVolume.grid(row=4, column=1, pady=(0, 20))

        # Label Volume
        fonte = ct.CTkFont(size=18, weight="bold")
        self.labelVolume = ct.CTkLabel(self.frameSelVolume, text="Volume", font=fonte)
        self.labelVolume.grid(row=0, column=0, sticky="nsew")
        
        # Criando o Combo Box
        self.comboboxVolume = ct.CTkComboBox(self.frameSelVolume, width=170, values=self.dadosVolumes, command=self.mudarSelVolume)
        self.comboboxVolume.grid(row=1, column=0, sticky="nsew")

        # Define um valor padrão (opcional)
        self.comboboxVolume.set("Selecione um Volume")

    def mudarSelVolume(self, numeroVolume: str) -> None:
        self.idVolume = self.controller.pesquisarVolumePorNumero(int(numeroVolume), self.idManga)
        self.configFrameSelCapitulo()

    def configFrameSelCapitulo(self) -> None:
        # Recebe os números dos volumes cadastros
        self.dadosCapitulos = self.controller.listarCapitulos(self.idVolume)

        # -- Combo Box --
        # Frame do Combo Box
        self.frameSelCapitulo = ct.CTkFrame(self, fg_color="#2b2b2b")
        self.frameSelCapitulo.grid(row=5, column=1)

        # Label Capítulo
        fonte = ct.CTkFont(size=18, weight="bold")
        self.labelCapitulo = ct.CTkLabel(self.frameSelCapitulo, text="Capítulo", font=fonte)
        self.labelCapitulo.grid(row=0, column=0, sticky="nsew")
        
        # Criando o Combo Box
        self.comboboxCapitulo = ct.CTkComboBox(self.frameSelCapitulo, width=170, values=self.dadosCapitulos, command=self.mudarSelCapitulo)
        self.comboboxCapitulo.grid(row=1, column=0, sticky="nsew")

        # Define um valor padrão (opcional)
        self.comboboxCapitulo.set("Selecione um Capítulo")

    def mudarSelCapitulo(self, numeroCapitulo) -> None:
        self.idCapitulo = self.controller.pesquisarCapituloPorNumero(numeroCapitulo, self.idVolume)
        self.configBtnSalvar()

    def configBtnSalvar(self) -> None:
        # -- Botão de Salvar --
        self.btnSalver = ct.CTkButton(self, text="Salvar", command=lambda: self.salvarAtualizar())
        self.btnSalver.grid(row=6, column=1, pady=10, padx=10)

    def salvarAtualizar(self) -> None:
        # 1. SALVAR a nova configuração
        self.controller.saveConfig(self.idManga, self.idVolume, self.idCapitulo)

        # 2. ATUALIZAR a Treeview
        self.atualizaConfigAtual()
        self.comboboxManga.set("Selecione um Manga")
        self.comboboxVolume.set("Selecione um Volume")
        self.comboboxCapitulo.set("Selecione um Capítulo")

    def atualizaConfigAtual(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        # 2. Recebe os dados da nova configuração atual
        # Você deve chamar o método do controller novamente para garantir que os dados sejam os mais recentes
        self.dadosConfigManga = [self.controller.listaConfig()] 

        # 3. Repopular a Treeview com os novos dados
        self.popularConfig()