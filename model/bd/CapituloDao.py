from typing import List, Protocol

from model.Capitulo import Capitulo

class CapituloDao(Protocol):
    def listarCapitulo(self) -> List[Capitulo]:
        pass

    def pesquisarCapitulo(self, codCapitulo: int) -> Capitulo:
        pass