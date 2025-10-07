from typing import List, Protocol

from model.Volume import Volume

class VolumeDao(Protocol):
    # Lista os volumes do manga
    def listarVolume(self) -> List[Volume]: #type: ignore
        pass

    # Pesquisa um volume pelo código
    def pesquisarVolume(self, codVolume: int) -> Volume: #type: ignore
        pass