from view.Tela import Tela
from view.TelaSel import TelaSel

class TelaBaixaCapa(Tela):
    def __init__(self, mangaController):
        super().__init__(mangaController)
        self.telaSel = TelaSel(mangaController)
    
    def exibir(self):
        print("-- Baixar Capa --")
        idManga = self.telaSel.selManga()
        idVolume = self.telaSel.selVol(idManga)
        print("Baixando capa do volume...")
        self.mangaController.baixaCapa(idManga, idVolume)
        print("Capa baixada com sucesso!")
        