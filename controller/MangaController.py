from typing import List

from model.MangaService import MangaService
from model.Manga import Manga
from view.Tela import Tela

class MangaController:
    def __init__(self):
        self.mangaService = MangaService()
    
    def mostrarCaminho(self, codManga: int) -> str:
        '''Retorna o caminho do manga.
        Args:
            codManga (int): Código do manga.
        Returns
            str: Caminho do manga
        '''
        manga = self.mangaService.definirCaminho(codManga)

        return manga
    
    def listarMangas(self) -> List[Manga]:
        '''Lista os mangas do banco de dados.
        Args:
            Não possuí argumentos.
        Returns
            List[Manga]: Lista de objetos Manga
        '''
        lista = self.mangaService.listarMangas()
        
        return lista
    
    def listaConfig(self) -> str:
        '''Pesquisa a configuração de manga atual.
        Args:
            Não possuí argumentos.
        Returns
            str: texto que exibe a configuração de manga atual.
        '''
        mangaAtual = self.mangaService.listaConfig()

        return mangaAtual