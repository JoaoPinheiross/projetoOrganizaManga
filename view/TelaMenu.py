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
            print("3 - Converter Manga")
            print("4 - Baixar Capa")
            print("9 - Sair")

            try:

                ent = int(input())

                casos = {
                    1: lambda: self.mangaController.organizaManga(),
                    2: lambda: self.telaConfigManga.exibir(),
                    3: lambda: self.mangaController.converteMobi(),
                    4: "capa",
                    9: lambda: self.encerrar()
                }
                
                caso = casos.get(ent, lambda: print("Opção inválida. Tente novamente."))

                result = caso()
            except ValueError:
                print("Digite um valor númerico.")

    def encerrar(self):
        self.r = False