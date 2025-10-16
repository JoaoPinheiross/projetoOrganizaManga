from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from model.Base import Base

class Volume(Base):
    # nome da tabela
    __tablename__ = "volumes"

    # colunas da tabela
    idVolume: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    numero: Mapped[int] = mapped_column(Integer, nullable=False)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    idManga: Mapped[int] = mapped_column(Integer, ForeignKey("mangas.idManga"), nullable=False)

    # relacionamentos da tabela
    manga = relationship("Manga", back_populates="volumes")
    capitulos = relationship("Capitulo", back_populates="volumes")
    configM = relationship("ConfigManga", back_populates="volumes")