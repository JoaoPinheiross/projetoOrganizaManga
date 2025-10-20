from typing import Optional

from view.Tela import Tela

class TelaSel(Tela):
    def __init__(self, mangaController):
        super().__init__(mangaController)
    
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

    def selCap(self, idVolume) -> Optional[int|None]:
        capitulos = self.mangaController.listarCapitulos(idVolume)

        if not capitulos:
            print("Nenhum capitulo encontrado.")
            return None
        
        print("\n--- Selecione o Capitulo ---")
        for i, cap in enumerate(capitulos):
            print(f"{i+1} - {cap.numero}")

        while True:
            try:
                escolha = int(input("Digite o número do capitulo: "))
                if 1 <= escolha <= len(capitulos):
                    return capitulos[escolha - 1].idCapitulo
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")