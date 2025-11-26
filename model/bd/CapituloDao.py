from typing import List, Protocol

from model.Capitulo import Capitulo

class CapituloDao(Protocol):
    def listarCapitulo(self, codVol) -> List[Capitulo]: #type: ignore
        pass

    def pesquisarCapitulo(self, codCapitulo: int) -> Capitulo: #type: ignore
        pass

    def pesquisarCapituloPorNumero(self, numeroCapitulo: int, codVolume: int) -> Capitulo: #type: ignore
        pass