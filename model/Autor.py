from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.Base import Base

class Autor(Base):
    # nome da tabela
    __tablename__ = "autores"

    # colunas da tabela
    idAutor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)

    # relacionamentos da tabela
    mangas = relationship("Manga", back_populates="autor")

    