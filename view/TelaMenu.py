from view.Tela import Tela
from view.TelaConfigManga import TelaConfigManga

class TelaMenu(Tela):
    def __init__(self, mangaController):
        super().__init__(mangaController)
        self.telaConfigManga = TelaConfigManga(mangaController)
        self.r = True

    def exibir(self):
        while self.r:
            print("MENU")
            print("1 - Organizar Manga")
            print("2 - Configura Manga")
            print("3 - Baixar Capa")
            print("4 - Sair")

            ent = int(input())

            casos = {
                1: "dev",
                2: lambda: self.telaConfigManga.exibir(),
                3: "capa",
                4: lambda: self.encerrar()
            }
            
            caso = casos.get(ent, lambda: print("Opção inválida. Tente novamente."))

            result = caso()

    def encerrar(self):
        self.r = False