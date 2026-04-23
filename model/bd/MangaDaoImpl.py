from sqlalchemy import create_engine, select, Column
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List
from dotenv import load_dotenv
import os

from model.Manga import Manga

class MangaDaoImpl:
    load_dotenv()
    DB_HOST = os.getenv("BD_HOST")
    DB_NOME = os.getenv("BD_NOME")
    DB_USUARIO = os.getenv("BD_USUARIO")
    DB_SENHA = os.getenv("BD_SENHA")
    senha = quote_plus(f'{DB_SENHA}')
    engine = create_engine(f"mysql+mysqlconnector://{DB_USUARIO}:{senha}@{DB_HOST}:3306/{DB_NOME}", echo=False)

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
    
    def pesquisarMangaPorNome(self, nomeManga: str) -> Manga:
        with self.Session() as session:
            query = select(Manga).filter(Manga.nome == nomeManga)
            manga = session.scalar(query)

        return manga