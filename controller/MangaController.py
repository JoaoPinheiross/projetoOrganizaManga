from typing import List

from model.MangaService import MangaService
from model.Manga import Manga
from view.Tela import Tela

class MangaController:
    def __init__(self):
        self.mangaService = MangaService()
    
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
    
    def listaConfig(self) -> str:
        '''Pesquisa a configuração de manga atual.
        Args:
            Não possuí argumentos.
        Returns
            str: texto que exibe a configuração de manga atual.
        '''
        mangaAtual = self.mangaService.listaConfig()

        return mangaAtual
    
    def saveConfig(self, idManga, idVolume, idCapitulo) -> str:
        return self.mangaService.saveConfig(idManga, idVolume, idCapitulo)
    
    def converteMobi(self) -> None:
        self.mangaService.converteMobi()