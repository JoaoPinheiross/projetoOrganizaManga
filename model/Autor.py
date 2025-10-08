from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from model.Base import Base

class Autor(Base):
    # nome da tabela
    __tablename__ = "autores"

    # colunas da tabela
    idAutor: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)

    # relacionamentos da tabela
    mangas = relationship("Manga", back_populates="autor")

    