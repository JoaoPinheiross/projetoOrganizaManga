from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Base import Base

class Autor(Base):
    __tablename__ = "autores"

    idAutor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)

    mangas = relationship("Manga", back_populates="autor")
    @property
    def idAutor(self) -> int:
        return self.__idAutor
    
    @idAutor.setter
    def idAutor(self, idAutor: int) -> None:
        self.__idAutor = idAutor
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    