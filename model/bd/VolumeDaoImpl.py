from sqlalchemy import create_engine, select, Column
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List

from model.Volume import Volume

class VolumeDaoImpl():
    senha = quote_plus("Pipoca9190")
    engine = create_engine(f"mysql+mysqlconnector://root:{senha}@localhost:3306/projetomanga", echo=False)

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