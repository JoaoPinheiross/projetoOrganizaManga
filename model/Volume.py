from typing import List

from model.Capitulo import Capitulo

class Volume:
    # Construtor
    def __init__(self, nome: str, capitulos: List[Capitulo]) -> None:
        '''Inicia o objeto da classe Volume com um nome, número, e uma lista de capitulos.
        ARGS:
            nome (str): Nome do volume.
            numero (float): Número do volume.
            capitulos (List[Capitulo]): Uma lista de capitulos do volume.
        Return:
            None: Não possuí retorno.
        '''
        self.__nome = nome
        self.__capitulos = capitulos

    # Métodos Getter e Setter
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