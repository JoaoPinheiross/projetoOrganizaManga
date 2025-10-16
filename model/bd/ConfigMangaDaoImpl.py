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
    
    def saveConfig(self, idManga: int, idVolume: int, idCapitulo: int) -> str:
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
                    msg = "Configuração atualizada com sucesso!"
                else:
                    msg = f"Manga com ID {idManga} não encontrado."
            except Exception as e:
                session.rollback()
                msg = f"Ocorreu um erro: {e}"
        
        return msg