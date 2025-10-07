from typing import List, Protocol

from model.ConfigManga import ConfigManga

class ConfigMangaDao(Protocol):
    # Lista a configuração do manga atual
    def listarConfig(self) -> ConfigManga:
        pass