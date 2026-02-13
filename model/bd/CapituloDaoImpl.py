from sqlalchemy import create_engine, select, Column
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List

from model.Capitulo import Capitulo

class CapituloDaoImpl():
    senha = quote_plus("Pinheiro@04")
    engine = create_engine(f"mysql+mysqlconnector://root:{senha}@localhost:3306/projetomanga", echo=False)

    Session = sessionmaker(bind=engine)

    def listarCapitulo(self, codVol) -> List[Capitulo]:
        with self.Session() as session:
            query = select(Capitulo).where(Capitulo.idVolume == codVol)
            capitulos = list(session.scalars(query).all())

        return capitulos
    
    def pesquisarCapitulo(self, codCapitulo: int) -> Capitulo:
        with self.Session() as session:
            query = select(Capitulo).where(Capitulo.idCapitulo == codCapitulo)
            capitulo = session.get(Capitulo, codCapitulo)

        return capitulo

    def pesquisarCapituloPorNumero(self, numeroCapitulo: int, codVolume: int) -> Capitulo:
        with self.Session() as session:
            query = select(Capitulo).where(Capitulo.numero == numeroCapitulo, Capitulo.idVolume == codVolume)
            capitulo = session.scalar(query)

        return capitulo