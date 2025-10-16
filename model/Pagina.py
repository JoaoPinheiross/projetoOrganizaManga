class Pagina:
    # Construtor
    def __init__(self, numero: int, caminho: str) -> None:
        '''Inicia o objeto da classe Pagina com um número e um caminho.
        ARGS:
            numero (int): Número da página do capitulo.
            caminho (str): Caminho do repositório onde deve ser baixado o manga
        RETURNS:
            None: Não possuí retorno.
        '''
        self.__numero = numero
        self.__caminho = caminho

    # Métodos Getter e Setter
    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero) -> None:
        self.__numero = numero
    
    @property
    def caminho(self) -> str:
        return self.__caminho
    
    @caminho.setter
    def caminho(self, caminho) -> None:
        self.__caminho = caminho