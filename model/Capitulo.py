from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column

from model.Base import Base

class Capitulo(Base):
    # nome da tabela
    __tablename__ = "capitulos"

    # colunas da tabela
    idCapitulo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    numero: Mapped[int] = mapped_column(Float, nullable=False)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    idVolume: Mapped[int] = mapped_column(Integer, ForeignKey("volumes.idVolume"), nullable=False)

    # relacionamentos da tabela
    volumes = relationship("Volume", back_populates="capitulos")
    configM = relationship("ConfigManga", back_populates="capitulos")