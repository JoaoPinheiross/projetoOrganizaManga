from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

from model.ConfigManga import ConfigManga

class ConfigMangaDaoImpl():
    senha = quote_plus("Pipoca@04")
    engine = create_engine(f"mysql+mysqlconnector://root:{senha}@localhost:3306/projetomanga", echo=False)

    Session = sessionmaker(bind=engine)

    def listarConfig(self) -> ConfigManga:
        '''Seleciona a primeira configuração de manga.
        Args:
            Não possuí parâmetros.
        Returns:
            ConfigManga: Manga atual da configuração.
        '''
        with self.Session() as session:
            query = select(ConfigManga)
            mangaAtual = session.scalars(query).one()

        return mangaAtual