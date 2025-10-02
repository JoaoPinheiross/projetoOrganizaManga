from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Base import Base
'''from model.Autor import Autor
from model.Volume import Volume'''

class Manga(Base):
    # Construtor
    '''def __init__(self, nome: str, autor: str, volumes: List[Volume]) -> None:
        Inicia o objeto da classe Manga com um nome, autor, e uma lista de Volumes.
        ARGS:
            nome (str): Nome do manga.
            autor (str): Nome do autor do manga.
            volumes (List[Volume]): Uma lista dos volumes do manga.
        Return:
            None: Não possuí retorno.
        
        self.__nome = nome
        self.__autor = autor
        self.__volumes = volumes'''
    __tablename__ = "mangas"

    __idManga = Column(Integer, primary_key=True, autoincrement=True)
    __nome = Column(String(60), nullable=False)
    __idAutor = Column(Integer, ForeignKey("autores.idAutor"), nullable=False)

    autor = relationship("Autor", back_populates="mangas")
    volumes = relationship("Volume", back_populates="manga", cascade="all, delete-orphan", order_by="Volume.numero")

    # Métodos Getter e Setter
    @property
    def idManga(self) -> int:
        return self.__idManga
    
    @idManga.setter
    def idManga(self, idManga: int) -> None:
        self.__idManga = idManga
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def idAutor(self) -> int:
        return self.__idAutor
    
    @idAutor.setter
    def idAutor(self, idAutor: int) -> None:
        self.__idAutor = idAutor