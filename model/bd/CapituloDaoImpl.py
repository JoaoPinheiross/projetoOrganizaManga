from sqlalchemy import create_engine, select, Column
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from typing import List
from dotenv import load_dotenv
import os

from model.Capitulo import Capitulo

class CapituloDaoImpl():
    load_dotenv()
    DB_HOST = os.getenv("BD_HOST")
    DB_NOME = os.getenv("BD_NOME")
    DB_USUARIO = os.getenv("BD_USUARIO")
    DB_SENHA = os.getenv("BD_SENHA")
    senha = quote_plus(f'{DB_SENHA}')
    engine = create_engine(f"mysql+mysqlconnector://{DB_USUARIO}:{senha}@{DB_HOST}:3306/{DB_NOME}", echo=False)

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