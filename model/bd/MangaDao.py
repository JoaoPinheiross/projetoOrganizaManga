from typing import List, Protocol

from model.Manga import Manga

class MangaDao(Protocol):
    def listarMangas(self) -> List[Manga]:
        pass

    def pesquisarManga(self, codManga: int) -> Manga:
        pass