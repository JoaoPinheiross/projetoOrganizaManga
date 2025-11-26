from typing import List, Protocol

from model.Manga import Manga

class MangaDao(Protocol):
    def listarMangas(self) -> List[Manga]: #type: ignore
        pass

    def pesquisarManga(self, codManga: int) -> Manga: #type: ignore
        pass

    def pesquisarMangaPorNome(self, nomeManga: str) -> Manga: #type: ignore
        pass