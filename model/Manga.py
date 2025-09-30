from typing import List

from model.Volume import Volume

class Manga:
    def __init__(self, nome: str, autor: str, volumes: List[Volume]):
        self.__nome = nome
        self.__autor = autor
        self.__volumes = volumes

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def autor(self) -> str:
        return self.__autor
    
    @autor.setter
    def autor(self, autor: str):
        self.__autor = autor

    @property
    def volumes(self) -> List[Volume]:
        return self.__volumes
    
    @volumes.setter
    def volumes(self, volumes: List[Volume]):
        self.__volumes = volumes