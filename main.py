from controller.MangaController import MangaController

from view.TelaMenu import TelaMenu

mangaController = MangaController()
#print(mangaController.listarMangas()[0].nome)
telaMenu = TelaMenu(mangaController)
telaMenu.exibir()