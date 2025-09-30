from typing import List

from model.Capitulo import Capitulo

class Volume:
    def __init__(self, nome: str, capitulos: List[Capitulo]):
        self.__nome = nome
        self.__capitulos = capitulos

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def capitulos(self) -> List[Capitulo]:
        return self.__capitulos
    
    @capitulos.setter
    def capitulos(self, capitulos: List[Capitulo]):
        self.__capitulos = capitulos