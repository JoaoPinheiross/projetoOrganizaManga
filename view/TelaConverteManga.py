from typing import Optional

from view.Tela import Tela

class TelaConverteManga(Tela):
    def __init__(self, mangaController):
        super().__init__(mangaController)

    def exibir(self):
        r = True
        self.espaco()
        print("--- Converter Manga ---")
        self.espaco()
        
        self.selConversao()

    def selConversao(self) -> bool:
        idManga = self.selManga()
        if idManga is None:
            return False

        idVolume = self.selVol(idManga)
        if idVolume is None:
            return False

        resultado = self.mangaController.converteMobi(idManga, idVolume)

        return False
            
    def selManga(self) -> Optional[int|None]:
        mangas = self.mangaController.listarMangas()
        
        if not mangas:
            print("Nenhum mangá encontrado.")
            return None

        print("\n--- Selecione o Mangá ---")
        for i, manga in enumerate(mangas):
            print(f"{i+1} - {manga.nome}")

        while True:
            try:
                escolha = int(input("Digite o número do mangá: "))
                if 1 <= escolha <= len(mangas):
                    return mangas[escolha - 1].idManga
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def selVol(self, idManga) -> Optional[int|None]:
        volumes = self.mangaController.listarVolumes(idManga)

        if not volumes:
            print("Nenhum volume encontrado.")
            return None
        
        print("\n--- Selecione o Volume ---")
        for i, vol in enumerate(volumes):
            print(f"{i+1} - {vol.numero}")

        while True:
            try:
                escolha = int(input("Digite o número do volume: "))
                if 1 <= escolha <= len(volumes):
                    return volumes[escolha - 1].idVolume
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")