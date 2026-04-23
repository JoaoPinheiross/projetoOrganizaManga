from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

from model.ConfigManga import ConfigManga

class ConfigMangaDaoImpl():
    load_dotenv()
    DB_HOST = os.getenv("BD_HOST")
    DB_NOME = os.getenv("BD_NOME")
    DB_USUARIO = os.getenv("BD_USUARIO")
    DB_SENHA = os.getenv("BD_SENHA")
    senha = quote_plus(f'{DB_SENHA}')
    engine = create_engine(f"mysql+mysqlconnector://{DB_USUARIO}:{senha}@{DB_HOST}:3306/{DB_NOME}", echo=False)

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
    
    def saveConfig(self, idManga: int, idVolume: int, idCapitulo: int) -> bool:
        '''Salva a nova configuração de manga.
        Args:
            Não possuí parâmetros.
        Returns:
            ConfigManga: Manga atual da configuração.
        '''
        with self.Session() as session:
            try:
                config = session.get(ConfigManga, 1)

                if config:
                    config.idManga = idManga
                    config.idVolume = idVolume
                    config.idCapitulo = idCapitulo
                    session.commit()
                    return True
                else:
                    print(f"Manga com ID {idManga} não encontrado.")
                    return False
            except Exception as e:
                session.rollback()
                print(f"Ocorreu um erro: {e}")
                return False
        