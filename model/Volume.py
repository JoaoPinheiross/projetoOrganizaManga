from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model.Base import Base

class Volume(Base):
    # nome da tabela
    __tablename__ = "volumes"

    # colunas da tabela
    idVolume = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, nullable=False)
    nome = Column(String(80), nullable=False)
    idManga = Column(Integer, ForeignKey("mangas.idManga"), nullable=False)

    # relacionamentos da tabela
    manga = relationship("Manga", back_populates="volumes")
    capitulos = relationship("Capitulo", back_populates="volumes")
    configM = relationship("ConfigManga", back_populates="volumes")