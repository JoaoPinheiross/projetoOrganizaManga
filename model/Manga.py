from typing import List

from model.Volume import Volume

class Manga:
    # Construtor
    def __init__(self, nome: str, autor: str, volumes: List[Volume]) -> None:
        '''Inicia o objeto da classe Manga com um nome, autor, e uma lista de Volumes.
        ARGS:
            nome (str): Nome do manga.
            autor (str): Nome do autor do manga.
            volumes (List[Volume]): Uma lista dos volumes do manga.
        Return:
            None: Não possuí retorno.
        '''
        self.__nome = nome
        self.__autor = autor
        self.__volumes = volumes

    # Métodos Getter e Setter
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def autor(self) -> str:
        return self.__autor
    
    @autor.setter
    def autor(self, autor: str) -> None:
        self.__autor = autor

    @property
    def volumes(self) -> List[Volume]:
        return self.__volumes
    
    @volumes.setter
    def volumes(self, volumes: List[Volume]) -> None:
        self.__volumes = volumes