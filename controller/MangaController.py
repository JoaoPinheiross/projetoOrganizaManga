from typing import List
import tkinter.messagebox as msg

from model.MangaService import MangaService
from model.Manga import Manga
from view.BaseView import BaseTela
from view.TelaMenu import TelaMenu
from view.TelaConfig import TelaConfig

class MangaController:
    def __init__(self):
        self.mangaService = MangaService()
        self. tela = BaseTela()
        self.telaMenu = TelaMenu(self.tela, self)

        self.frame_classes = {
            "menu": TelaMenu,
            "config": TelaConfig
        }
        self.frameAtivo = None
        self.trocaFrame("menu")

    def iniciar(self) -> None:
        '''
            Inicia o Programa.
        '''
        self.tela.mainloop()
    
    def encerrar(self) -> None:
        '''
            Encerra o Programa.
        '''
        self.tela.destroy()

    def trocaFrame(self, frame) -> None:
        if self.frameAtivo is not None:
            self.frameAtivo.destroy()
            self.frameAtivo = None
        
        # 2. Criar uma NOVA INSTÂNCIA da classe do Frame
        FrameClass = self.frame_classes[frame]
        
        # 3. Instanciar e posicionar o novo frame
        # Passamos self.tela como master e self (o controller) como controller
        novoFrame = FrameClass(self.tela, self) 
        
        # Posicionamento para tkraise
        novoFrame.grid(row=0, column=0, sticky="nsew")
        
        # 4. Exibir o novo frame
        novoFrame.tkraise()
        
        # 5. Rastrear o novo frame como o ativo
        self.frameAtivo = novoFrame
    
    def organizaManga(self) -> bool:
        '''Organiza os capitulos baixados.
        Args:
            Não possuí argumentos.
        Returns
            Não possuí retornos.
        '''
        return self.mangaService.organizarManga()
    
    def listarMangas(self) -> List[str]:
        '''Lista os mangas do banco de dados.
        Args:
            Não possuí argumentos.
        Returns
            List[str]: Lista dos nomes dos Mangas cadastrados
        '''
        lista = self.mangaService.listarMangas()
        lista = [m.nome for m in lista]
        
        return lista
    
    def pesquisarMangaPorNome(self, nomeManga):
        manga = self.mangaService.pesquisarMangaPorNome(nomeManga)
        
        return manga.idManga
    
    def listarVolumes(self, idManga: int) -> list[str]:
        '''Lista os volumes do banco de dados.
        Args:
            Não possuí argumentos.
        Returns
            List[str]: Lista dos números dos volumes cadastrados
        '''
        lista = self.mangaService.listarVolumes(idManga)

        lista = [str(v.numero) for v in lista]

        return lista
    
    def pesquisarVolumePorNumero(self, numeroVolume: int, codManga: int) -> int:
        '''Pesquisar o volume pelo número.
        Args:
            numeroVolume (int): O número do volume.
            codManga (int): O id do manga do volume.
        Returns:
            int: Retorna o id do volume com o número pesquisado
        '''
        volume = self.mangaService.pesquisarVolumePorNumero(numeroVolume, codManga)

        return volume.idVolume
    
    def listarCapitulos(self, idVolume):
        '''Lista os capítulos do banco de dados.
        Args:
            Não possuí argumentos.
        Returns
            List[str]: Lista dos números dos capítulos cadastrados
        '''
        lista = self.mangaService.listarCapitulos(idVolume)

        lista = [str(c.numero) for c in lista]
        
        return lista
    
    def pesquisarCapituloPorNumero(self, numeroCapitulo: int, codVolume: int) -> int:
        '''Pesquisar o capítulo pelo número.
        Args:
            numeroCapitulo (int): O número do capítulo.
            codVolume (int): O id do volume do capítulo.
        Returns:
            int: Retorna o id do capítulo com o número pesquisado
        '''
        capitulo = self.mangaService.pesquisarCapituloPorNumero(numeroCapitulo, codVolume)

        return capitulo.idCapitulo
    
    def listaConfig(self) -> tuple[str, int, int]:
        '''Pesquisa a configuração de manga atual.
        Args:
            Não possuí argumentos.
        Returns
            tuple[str, int, int]: configuração atual do manga.
        '''
        mangaAtual = self.mangaService.listaConfig()

        return mangaAtual
    
    def saveConfig(self, idManga, idVolume, idCapitulo) -> None:
        salvou = self.mangaService.saveConfig(idManga, idVolume, idCapitulo)
        if salvou:
            msg.showinfo("Organizador De Mangas", "Configuração salva com sucesso!")
        else:
            msg.showerror("Organizador De Mangas", "Ocorreu algum erro ao salvar a configuração.")

    def converteMobi(self) -> bool:
        config = self.mangaService.configMangaDaoImpl.listarConfig()
        idManga = config.idManga
        idVolume = config.idVolume
        caminho = self.mangaService.definirCaminhoConv(idManga, idVolume)
        try:
            self.mangaService.converteMobi(caminho)
            return True
        except Exception:
            return False

    def baixaCapa(self) -> bool:
        config = self.mangaService.configMangaDaoImpl.listarConfig()
        idManga = config.idManga
        idVolume = config.idVolume
        caminho = self.mangaService.definirCaminhoConv(idManga, idVolume)
        try:
            self.mangaService.baixarCapa(caminho, idManga, idVolume)
            return True
        except Exception:
            return False