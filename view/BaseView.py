import customtkinter as ct

class BaseTela(ct.CTk):
    def __init__(self):
        super().__init__()
        ct.set_appearance_mode("dark")

        self.title("Organizador De Mangas")
        
        self.resizable(False, False)

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.width = 800
        self.height = 500

        self.x_position = int((self.screen_width / 2) - (self.width / 2))
        self.y_position = int((self.screen_height / 2) - self.height)

        self.geometry(f"{self.width}x{self.height}+{self.x_position}+{self.y_position}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

class BaseFrame(ct.CTkFrame):
    def __init__(self, tela: BaseTela, controller):
        super().__init__(tela)
        self.controller = controller
        self.tela = tela

    def mostrarCarregamento(self, msg: str) -> ct.CTkToplevel:
        """Cria e mostra a janela de carregamento Toplevel."""

        top = ct.CTkToplevel(self)
        top.title("Carregando...")

        top.grid_rowconfigure(0, weight=1)
        top.grid_rowconfigure(3, weight=1)
        top.grid_columnconfigure(0, weight=1)
        top.grid_columnconfigure(2, weight=1)

        child_width = 400
        child_height = 250
        
        # Posição e Dimensões da Janela Principal
        master_width = self.tela.width
        master_height = self.tela.height
        master_x = self.tela.x_position
        master_y = self.tela.y_position

        # 3. Calcula a nova posição (x, y)
        # Calcula onde o canto superior esquerdo da nova janela deve ficar
        # para que ela esteja centralizada dentro da janela principal.
        
        # Posição X calculada: (X do Master) + (Metade da Largura do Master) - (Metade da Largura do Child)
        x = int(master_x + (master_width / 2) - (child_width / 2))
        
        # Posição Y calculada: (Y do Master) + (Metade da Altura do Master) - (Metade da Altura do Child)
        y = int(master_y + (master_height / 2) - (child_height / 2))

        # 4. Aplica a nova geometria
        # Formato: "largura x altura + posiçãoX + posiçãoY"
        top.geometry(f"{child_width}x{child_height}+{x}+{y}")

        top.wait_visibility()
        
        top.grab_set() # Bloqueia eventos para a janela principal (opcional, mas comum para loading)

        lblMsg = ct.CTkLabel(top, text=msg)
        lblMsg.grid(row=1, column=1)


        progressbar = ct.CTkProgressBar(top, orientation="horizontal", mode="indeterminate")
        progressbar.grid(row=2, column=1)
        progressbar.start()
        
        # Garante que a janela de carregamento seja desenhada imediatamente
        top.update()

        return top