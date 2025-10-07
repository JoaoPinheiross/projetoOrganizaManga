from controller.MangaController import MangaController

from view.TelaMenu import TelaMenu

mangaController = MangaController()
print(mangaController.listarMangas()[0].nome)
telaMenu = TelaMenu(mangaController)
#telaMenu.exibir()

'''from pathlib import Path

# Cria um objeto Path para a pasta desejada
caminho = Path(r'C:UserspjoaDownloadscapManga')

try:
    print(f"Conteúdo da pasta '{caminho}':")
    for item in caminho.iterdir():
        # item.name extrai apenas o nome do arquivo/pasta
        print(item.name)

except FileNotFoundError:
    print(f"Erro: O diretório '{caminho}' não foi encontrado.")'''