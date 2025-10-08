from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from model.Base import Base
from model.Volume import Volume

class ConfigManga(Base):
    # nome da tabela
    __tablename__ = "configManga"

    # colunas da tabela
    codCm: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    idManga: Mapped[int] = mapped_column(Integer, ForeignKey("mangas.idManga"), nullable=False)
    idVolume: Mapped[int] = mapped_column(Integer, ForeignKey("volumes.idVolume"), nullable=False)
    idCapitulo: Mapped[int] = mapped_column(Integer, ForeignKey("capitulos.idCapitulo"), nullable=False)

    # relacionamentos da tabela
    mangas = relationship("Manga", back_populates="configM")
    volumes = relationship("Volume", back_populates="configM")
    capitulos = relationship("Capitulo", back_populates="configM")