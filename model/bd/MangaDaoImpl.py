from sqlalchemy import create_engine, select, Column
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List

from model.Manga import Manga

class MangaDaoImpl:
    senha = quote_plus("Pipoca@04")
    engine = create_engine(f"mysql+mysqlconnector://root:{senha}@localhost:3306/projetomanga", echo=False)

    Session = sessionmaker(bind=engine)

    def listarMangas(self) -> List[Manga]:
        with self.Session() as session:
            query = select(Manga)
            mangas = list(session.scalars(query).all())

        return mangas
    
    def pesquisarManga(self, codManga: int) -> Manga:
        with self.Session() as session:
            query = select(Manga)
            manga = session.get(Manga, codManga)

        return manga