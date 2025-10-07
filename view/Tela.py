import os

class Tela:
    def __init__(self, mangaController):
        self.mangaController = mangaController

    def espaco(self):
        print("")

    def limparTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mudarTela(self, tela):
        tela.exibir()