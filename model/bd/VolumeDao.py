from typing import List, Protocol

from model.Volume import Volume

class VolumeDao(Protocol):
    # Lista os volumes do manga
    def listarVolumes(self) -> List[Volume]: #type: ignore
        pass
    
    # Pesquisa um volume
    def pesquisarVolume(self, numeroVolume: int, codManga: int) -> Volume: #type: ignore
        pass

    # Pesquisa um volume pelo número
    def pesquisarVolumePorNumero(self, numeroVolume: int) -> Volume: #type: ignore
        pass