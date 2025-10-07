from view.Tela import Tela

class TelaConfigManga(Tela):
    def __init__(self, mangaController):
        super().__init__(mangaController)

    def exibir(self):
        self.espaco()
        print("--- Configuração de Leitura ---")
        print("Configuração Atual:")
        print(self.mangaController.listaConfig())
        self.espaco()
        print("O que você deseja fazer?")
        print("1 - Alterar a Configuração de Leitura")
        print("2 - Sair")

        while True:
            try:
                escolha = input("Digite sua opção: ")
                if escolha == '1':
                    self.altConfig()
                elif escolha == '2':
                    print("Saindo da configuração.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

    def altConfig(self):
        idManga = self.selManga()
        if idManga is None:
            return

        idVolume = self.selVol(idManga)
        if idVolume is None:
            return

        idCapitulo = self.selCap(idVolume)
        if idCapitulo is None:
            return

        resultado = self.controller.salvarConfiguracao(idManga, idVolume, idCapitulo)
        print(f"\n{resultado}")

        self.controller.listaConfig()
            
    def selManga(self) -> int:
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

    def selVol(self):
        volumes = self.mangaController.listarVolumes()

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

    def selCap(self):
        capitulos = self.mangaController.listarCapitulos()

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