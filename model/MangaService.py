from typing import List
from pathlib import Path

from .bd.MangaDaoImpl import MangaDaoImpl
from .bd.VolumeDaoImpl import VolumeDaoImpl
from .bd.CapituloDaoImpl import CapituloDaoImpl
from .bd.ConfigMangaDaoImpl import ConfigMangaDaoImpl
from model.Manga import Manga

class MangaService:
    def __init__(self):
        self.mangaDaoImpl = MangaDaoImpl()
        self.volumeDaoImpl = VolumeDaoImpl()
        self.capituloDaoImpl = CapituloDaoImpl()
        self.configMangaDaoImpl = ConfigMangaDaoImpl()


    def definirCaminho(self, codManga) -> str:
        manga = self.mangaDaoImpl.pesquisarManga(codManga)

        caminho = rf"c:\mangas\{manga.nome}"

        return caminho
    
    def organizarManga(self, caminho: str) -> bool:
        caminhoOrig = Path(r'C:\Users\jpjoa\Downloads\capManga')
        caminhoDest = caminho

        return True
    
    def listarMangas(self) -> List[Manga]:
        lista = self.mangaDaoImpl.listarMangas()
        
        return lista
    
    def listaConfig(self):
        mangaAtual = self.configMangaDaoImpl.listarConfig()
        nomeManga = self.mangaDaoImpl.pesquisarManga((mangaAtual.idManga)).nome
        numVolume = self.volumeDaoImpl.pesquisarVolume(mangaAtual.idVolume).numero
        numCapitulo = self.capituloDaoImpl.pesquisarCapitulo(mangaAtual.idCapitulo).numero 

        mangaAtual = f"Nome: {nomeManga}\nVolume: {numVolume}\nCapitulo: {numCapitulo}"

        return mangaAtual