import customtkinter as ct

class BaseTela(ct.CTk):
    def __init__(self):
        super().__init__()
        ct.set_appearance_mode("dark")

        self.title("Organizador De Mangas")
        self.geometry("800x500+100+50")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

class BaseFrame(ct.CTkFrame):
    def __init__(self, tela: BaseTela, controller):
        super().__init__(tela)
        self.controller = controller

    def resetEstado(self):
        pass