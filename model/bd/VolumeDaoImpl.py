from sqlalchemy import create_engine, select, Column
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List
from dotenv import load_dotenv
import os

from model.Volume import Volume

class VolumeDaoImpl():
    load_dotenv()
    DB_HOST = os.getenv("BD_HOST")
    DB_NOME = os.getenv("BD_NOME")
    DB_USUARIO = os.getenv("BD_USUARIO")
    DB_SENHA = os.getenv("BD_SENHA")
    senha = quote_plus(f'{DB_SENHA}')
    engine = create_engine(f"mysql+mysqlconnector://{DB_USUARIO}:{senha}@{DB_HOST}:3306/{DB_NOME}", echo=False)

    Session = sessionmaker(bind=engine)

    def listarVolumes(self, codManga) -> List[Volume]:
        with self.Session() as session:
            query = select(Volume).where(Volume.idManga == codManga)
            volumes = list(session.scalars(query).all())

        return volumes
    
    def pesquisarVolume(self, codVolume: int) -> Volume:
        with self.Session() as session:
            query = select(Volume)
            volume = session.get(Volume, codVolume)

        return volume

    def pesquisarVolumePorNumero(self, numeroVolume: int, codManga: int) -> Volume:
        with self.Session() as session:
            query = select(Volume).filter(Volume.numero == numeroVolume, Volume.idManga == codManga)
            volume = session.scalar(query)
            
        return volume