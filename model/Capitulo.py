from typing import List

class Capitulo:
    # Construtor
    def __init__(self, nome: str, numero: float, paginas: List[Pagina]) -> None:
        '''Inicia o objeto da classe Capitulo com um nome, número, e uma lista de páginas.
        ARGS:
            nome (str): Nome do capítulo.
            numero (float): Número do capítulo.
            paginas (List[Pagina]): Uma lista das páginas do capitulo.
        Return:
            None: Não possuí retorno.
        '''
        self.__nome = nome
        self.__numero = numero
        self.__paginas = paginas

    # Métodos Getter e Setter
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def numero(self) -> float:
        return self.__numero

    @numero.setter
    def numero(self, numero: float):
        self.__numero = numero

    @property
    def paginas(self) -> List[Pagina]:
        return self.__paginas
    
    @paginas.setter
    def paginas(self, paginas: List[Pagina]):
        self.__paginas = paginas