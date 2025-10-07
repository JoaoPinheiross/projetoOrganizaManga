from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from model.Base import Base

class Capitulo(Base):
    # nome da tabela
    __tablename__ = "capitulos"

    # colunas da tabela
    idCapitulo = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Float, nullable=False)
    nome = Column(String(80), nullable=False)
    idVolume = Column(Integer, ForeignKey("volumes.idVolume"), nullable=False)

    # relacionamentos da tabela
    volumes = relationship("Volume", back_populates="capitulos")
    configM = relationship("ConfigManga", back_populates="capitulos")