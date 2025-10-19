from typing import List
from pathlib import Path
from itertools import chain
import re
import subprocess

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


    def definirCaminhoOrg(self) -> Path:
        config = self.configMangaDaoImpl.listarConfig()
        manga = self.mangaDaoImpl.pesquisarManga(config.idManga)
        volume = self.volumeDaoImpl.pesquisarVolume(config.idVolume)
        capitulo = self.capituloDaoImpl.pesquisarCapitulo(config.idCapitulo)
        if (capitulo.numero % 1 != 0):
            caminho = Path(rf"c:\mangas\{manga.nome}\vol_{volume.numero:03}\cap_{capitulo.numero:02}")
        else:
            caminho = Path(rf"c:\mangas\{manga.nome}\vol_{volume.numero:03}\cap_{int(capitulo.numero):02}")
                           
        caminho.mkdir(parents=True, exist_ok=True)

        return caminho
    
    def verificaVazio(self, caminho):
        try:
            listaDaPasta = caminho.iterdir()
            primeiraPag = next(listaDaPasta)
            paginas = chain([primeiraPag], listaDaPasta)
            return paginas
        except StopIteration:
            print(f"Aviso: O diretório de origem '{caminho}' está vazio. Nenhuma organização necessária.")

    def orderPaginas(self, arquivo):
        nome = arquivo.name
        if nome == '_.jpg':
            return (0, 0)  # vem em primeiro
        elif arquivo.suffix == '.jpg':
            return (0, 1)  # vem em primeiro
        elif nome == '_.png':
            return (0, 2)
        else:
            match = re.search(r'\((\d+)\)', nome)
            if match:
                numero = int(match.group(1))
                return (1, numero)  # depois, ordena pelos números
            else:
                return (2, nome)  # qualquer outro tipo, vem por último

    def organizarManga(self) -> bool:
        caminhoOrig = Path(r'C:\Users\jpjoa\Downloads\capManga')
        caminhoDest = self.definirCaminhoOrg()

        # Cria um objeto Path para a pasta desejada
        try:
            paginas = self.verificaVazio(caminhoOrig)
            if paginas:
                paginas = sorted(caminhoOrig.iterdir(), key=self.orderPaginas)
                print("Organizando as páginas...")
                for p in paginas:
                    print(p.name)
                for i, item in enumerate(paginas, start=1):
                    nome = f"{i:02}.png"
                    # item.name extrai apenas o nome do arquivo/pasta
                    caminho = caminhoDest / nome
                    item.replace(caminho)
                    print(f"página {item.name} salva no caminho {caminho}.")

        except FileNotFoundError:
            print(f"Erro: O diretório '{caminhoDest}' não foi encontrado.")

        config = self.configMangaDaoImpl.listarConfig()
        capitulo = self.capituloDaoImpl.pesquisarCapitulo(config.idCapitulo + 1)
        volume = capitulo.idVolume
        self.configMangaDaoImpl.saveConfig(config.idManga, volume, capitulo.idCapitulo)
        return True
    
    def listarMangas(self) -> List[Manga]:
        lista = self.mangaDaoImpl.listarMangas()
        
        return lista
    
    def listarVolumes(self, idManga):
        lista = self.volumeDaoImpl.listarVolumes(idManga)

        return lista
    
    def listarCapitulos(self, idVolume):
        lista = self.capituloDaoImpl.listarCapitulo(idVolume)

        return lista
    
    def listaConfig(self):
        mangaAtual = self.configMangaDaoImpl.listarConfig()
        nomeManga = self.mangaDaoImpl.pesquisarManga((mangaAtual.idManga)).nome
        numVolume = self.volumeDaoImpl.pesquisarVolume(mangaAtual.idVolume).numero
        numCapitulo = self.capituloDaoImpl.pesquisarCapitulo(mangaAtual.idCapitulo).numero 

        mangaAtual = f"Nome: {nomeManga}\nVolume: {numVolume}\nCapitulo: {numCapitulo}"

        return mangaAtual
    
    def saveConfig(self, idManga, idVolume, idCapitulo) -> str:
        return self.configMangaDaoImpl.saveConfig(idManga, idVolume, idCapitulo)
    
    def definirCaminhoConv(self, idManga: int, idVolume: int) -> Path:
        '''Define um caminho para realizar a conversão do manga.
        Args:
            idManga (int): Id do manga selecionado no banco de dados.
            idVolume (int): Id do volume selecionado no banco de dados.
        Returns:
            Path: Retorna o objeto Path com o caminho do volume do manga.
        '''
        manga = self.mangaDaoImpl.pesquisarManga(idManga)
        volume = self.volumeDaoImpl.pesquisarVolume(idVolume)
        
        caminho = Path(rf"c:\mangas\{manga.nome}\vol_{volume.numero:03}")

        return caminho
    
    def converteMobi(self, caminho) -> None:
        """Converte o volume para um arquivo .MOBI.
        Args:
            caminho (Path): O caminho do manga convertido.
        Returns:
            None: Sem retornos.
        """
        # Caminho para a pasta de entrada
        entrada = caminho
        # Caminho para a pasta de saída
        saida = caminho
        
        # Comando a ser executado
        comando = [
            r"C:\mangas\KCC_c2e_9.1.0.exe",
            "-m", "-s", "-c", "2", "-r", "1", "-p", "KPW", "-f", "MOBI",
            "-o", saida, entrada
        ]
        try:
            # Executar o comando
            subprocess.run(comando)
            print(f"Conversão foi enviada para o diretório {saida}.")
        except:
            print("A conversão não foi possível.")