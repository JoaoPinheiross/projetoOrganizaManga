from typing import List
from pathlib import Path
from itertools import chain
import re
import subprocess
import requests

from .bd.MangaDaoImpl import MangaDaoImpl
from .bd.VolumeDaoImpl import VolumeDaoImpl
from .bd.CapituloDaoImpl import CapituloDaoImpl
from .bd.ConfigMangaDaoImpl import ConfigMangaDaoImpl
from model.Manga import Manga
from model.Volume import Volume
from model.Capitulo import Capitulo

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
            match = re.search(r'\((\d+)\)', nome)
            if match:
                numero = int(match.group(1))
                return (1, numero)  # depois, ordena pelos números
            else:
                return (2, nome)  # qualquer outro tipo, vem por último
        elif nome == '_.png':
            return (0, 2)
        elif nome == '_.webp':
            return (0, 1)
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
            return False

        config = self.configMangaDaoImpl.listarConfig()
        capitulo = self.capituloDaoImpl.pesquisarCapitulo(config.idCapitulo + 1) # Confere se o capitulo seguinte existe
        if capitulo == None: # Caso não exista mais capitulos, converte em mobi e finaliza
            print("Convertendo volume...")
            caminho = self.definirCaminhoConv(config.idManga, config.idVolume)
            self.converteMobi(caminho)
            print("Salvando capa do volume...")
            self.baixarCapa(caminho, config.idManga, config.idVolume)
            
            return True
        else:
            volume = self.volumeDaoImpl.pesquisarVolume(capitulo.idVolume).numero
            if volume > self.volumeDaoImpl.pesquisarVolume(config.idVolume).numero:
                print("Convertendo volume...")
                caminho = self.definirCaminhoConv(config.idManga, config.idVolume)
                self.converteMobi(caminho)
                print("Salvando capa do volume...")
                self.baixarCapa(caminho, config.idManga, config.idVolume)
                
            self.configMangaDaoImpl.saveConfig(config.idManga, volume, capitulo.idCapitulo)
            return True
    
    def listarMangas(self) -> List[Manga]:
        lista = self.mangaDaoImpl.listarMangas()
        
        return lista

    def pesquisarMangaPorNome(self, nomeManga: str) -> Manga:
        manga = self.mangaDaoImpl.pesquisarMangaPorNome(nomeManga)

        return manga
    
    def listarVolumes(self, idManga) -> list[Volume]:
        lista = self.volumeDaoImpl.listarVolumes(idManga)

        return lista
    
    def pesquisarVolumePorNumero(self, numeroVolume: int, codManga: int) -> Volume:
        '''pesquisa o volume pelo número.
        Args:
            numeroVolume (int): O número do volume do manga.
            codManga (int): O id do manga do volume.
        Returns:
            Volume: Retorna o volume com o número pesquisado
        '''
        volume = self.volumeDaoImpl.pesquisarVolumePorNumero(numeroVolume, codManga)

        return volume

    def listarCapitulos(self, idVolume):
        lista = self.capituloDaoImpl.listarCapitulo(idVolume)

        return lista
    
    def pesquisarCapituloPorNumero(self, numeroCapitulo: int, codVolume: int) -> Capitulo:
        '''Pesquisar o capítulo pelo número.
        Args:
            numeroCapitulo (int): O número do capítulo.
            codVolume (int): O id do volume do capítulo.
        Returns:
            Capitulo: Retorna o capítulo com o número pesquisado
        '''
        capitulo = self.capituloDaoImpl.pesquisarCapituloPorNumero(numeroCapitulo, codVolume)

        return capitulo
    
    def listaConfig(self) -> tuple[str, int, int]:
        '''Retorna a configuração de manga atual.
        Args:
            Não possuí argumentos.
        Returns
            tuple[str, int, int]: configuração atual do manga.
        '''
        mangaAtual = self.configMangaDaoImpl.listarConfig()
        nomeManga = self.mangaDaoImpl.pesquisarManga((mangaAtual.idManga)).nome
        numVolume = self.volumeDaoImpl.pesquisarVolume(mangaAtual.idVolume).numero
        numCapitulo = self.capituloDaoImpl.pesquisarCapitulo(mangaAtual.idCapitulo).numero

        mangaAtual = (nomeManga, numVolume, numCapitulo)

        return mangaAtual
    
    def saveConfig(self, idManga, idVolume, idCapitulo) -> bool:
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
    
    def converteMobi(self, caminho: Path) -> bool:
        """Converte o volume para um arquivo .MOBI.
        Args:
            caminho (Path): O caminho do manga convertido.
        Returns:
            None: Não possui retorno.
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
            return True
        except:
            print("A conversão não foi possível.")
            return False

    def baixarCapa(self, caminho: Path, idManga: int, idVolume: int) -> bool:
        '''Realiza o download da capa do volume do manga.
        Args:
            caminho (Path): O caminho do volume do manga.
            idManga (int): O id do manga.
            volume (int): O número do volume.
        Returns:
            None: Não possui retorno.
        '''
        capaVol = ""
        manga = self.mangaDaoImpl.pesquisarManga(idManga)
        volume = self.volumeDaoImpl.pesquisarVolume(idVolume)
        url = f"https://api.mangadex.org/manga?title={manga.nome}&limit=10"
        res = requests.get(url).json()
        for m in res['data']: #type: ignore
            titulos = m['attributes']['title'] #type: ignore
            if manga.nome.lower() in [t.lower() for t in titulos.values()]: #type: ignore
                idMangaDex = m['id'] #type: ignore

        limite = "100"
        offset = 0
        continuar = True
        while continuar:
            chapters_url = (
                    f"https://api.mangadex.org/cover?"
                    f"manga[]={idMangaDex}&limit={limite}&offset={offset}" #type: ignore
                )
            
            res = requests.get(chapters_url).json()

            if 'data' not in res or not res['data']:
                continuar = False  # acabou os capítulos
            for c in res['data']: #type: ignore
                if c["attributes"]["volume"] == str(volume.numero):
                    capa: str = c["attributes"]["fileName"]
                    if (type(capa) == str):
                        if (capaVol == ""):
                            capaVol = capa
                    else:
                        raise ValueError(f"Capa do volume {volume.numero} não encontrada.")
                    
            offset += int(limite)
        url_imagem = f"https://uploads.mangadex.org/covers/{idMangaDex}/{capaVol}" #type: ignore
        imagem = requests.get(url_imagem, headers={"User-Agent": "Mozilla/5.0"})
        caminho = caminho / f"capa_vol_{volume.numero:03}.jpeg"
        if imagem.status_code == 200:
            with open(caminho, "wb") as f:
                f.write(imagem.content)
            print(f"Capa salva em {caminho}")
            return True
        else:
            print("Não foi possível salvar a capa.")
            return False