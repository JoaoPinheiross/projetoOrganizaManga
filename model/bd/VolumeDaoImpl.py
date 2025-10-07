from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List

from model.Volume import Volume

class VolumeDaoImpl():
    senha = quote_plus("Pipoca@04")
    engine = create_engine(f"mysql+mysqlconnector://root:{senha}@localhost:3306/projetomanga", echo=False)

    Session = sessionmaker(bind=engine)

    def listarVolume(self) -> List[Volume]:
        with self.Session() as session:
            query = select(Volume)
            volumes = session.scalars(query).all()

        return volumes

    def pesquisarVolume(self, codVolume: int) -> Volume:
        with self.Session() as session:
            query = select(Volume).where(Volume.idVolume == codVolume)
            volumes = session.scalars(query).first()

        return volumes