from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List

from model.Capitulo import Capitulo

class CapituloDaoImpl():
    senha = quote_plus("Pipoca@04")
    engine = create_engine(f"mysql+mysqlconnector://root:{senha}@localhost:3306/projetomanga", echo=False)

    Session = sessionmaker(bind=engine)

    def listarCapitulo(self) -> List[Capitulo]:
        with self.Session() as session:
            query = select(Capitulo)
            capitulos = list(session.scalars(query).all())

        return capitulos

    def pesquisarCapitulo(self, codCapitulo: int) -> Capitulo:
        with self.Session() as session:
            query = select(Capitulo).where(Capitulo.idCapitulo == codCapitulo)
            capitulo = session.scalars(query).first()

        return capitulo