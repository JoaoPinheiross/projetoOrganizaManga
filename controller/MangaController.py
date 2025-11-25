from typing import List
import customtkinter as ct

from model.MangaService import MangaService
from model.Manga import Manga
from view.BaseView import BaseTela
from view.TelaMenu import TelaMenu
from view.TelaConfig import TelaConfig

class MangaController:
    def __init__(self):
        self.mangaService = MangaService()

        self. tela = BaseTela()

        self.frames: dict[str, ct.CTkFrame] = {}
        self.definirFrames()

    def iniciar(self) -> None:
        '''
            Inicia o Programa.
        '''
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.tela.mainloop()
    
    def encerrar(self) -> None:
        '''
            Encerra o Programa.
        '''
        self.tela.destroy()

    def definirFrames(self) -> None:
        '''
            Define os frames utilizados no programa.
        '''
        self.frames["menu"] = TelaMenu(self.tela, self)
        self.frames["config"] = TelaConfig(self.tela, self)

        self.trocaFrame("menu")

    def trocaFrame(self, frame) -> None:
        frame = self.frames[frame]
        frame.tkraise()
    
    def organizaManga(self) -> None:
        '''Organiza os capitulos baixados.
        Args:
            Não possuí argumentos.
        Returns
            Não possuí retornos.
        '''
        self.mangaService.organizarManga()
    
    def listarMangas(self) -> List[Manga]:
        '''Lista os mangas do banco de dados.
        Args:
            Não possuí argumentos.
        Returns
            List[Manga]: Lista de objetos Manga
        '''
        lista = self.mangaService.listarMangas()
        
        return lista
    
    def listarVolumes(self, idManga):
        lista = self.mangaService.listarVolumes(idManga)

        return lista
    
    def listarCapitulos(self, idVolume):
        lista = self.mangaService.listarCapitulos(idVolume)

        return lista
    
    def listaConfig(self) -> tuple[str, int, int]:
        '''Pesquisa a configuração de manga atual.
        Args:
            Não possuí argumentos.
        Returns
            tuple[str, int, int]: configuração atual do manga.
        '''
        mangaAtual = self.mangaService.listaConfig()

        return mangaAtual
    
    def saveConfig(self, idManga, idVolume, idCapitulo) -> str:
        return self.mangaService.saveConfig(idManga, idVolume, idCapitulo)
    
    def converteMobi(self, idManga: int, idVolume: int) -> None:
        caminho = self.mangaService.definirCaminhoConv(idManga, idVolume)
        self.mangaService.converteMobi(caminho)

    def baixaCapa(self, idManga: int, idVolume: int) -> None:
        caminho = self.mangaService.definirCaminhoConv(idManga, idVolume)
        self.mangaService.baixarCapa(caminho, idManga, idVolume)