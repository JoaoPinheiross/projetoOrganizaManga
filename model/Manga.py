from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from model.Base import Base
from model.Autor import Autor
from model.Volume import Volume

class Manga(Base):
    # nome da tabela
    __tablename__ = "mangas"

    # colunas da tabela
    idManga: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    idAutor: Mapped[int] = mapped_column(Integer, ForeignKey("autores.idAutor"), nullable=False)

    # relacionamentos da tabela
    autor = relationship("Autor", back_populates="mangas")
    volumes = relationship("Volume", back_populates="manga", cascade="all, delete-orphan", order_by="Volume.numero")
    configM = relationship("ConfigManga", back_populates="mangas")

    # função para retorno dos atributos como String
    def toString(self) -> str:
        return f"idManga: {self.idManga}\nnome: {self.nome}\nidAutor: {self.idAutor}"