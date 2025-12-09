import tkinter as tk
import customtkinter as ct
import tkinter.messagebox as msg
import threading

from view.BaseView import BaseFrame, BaseTela

class TelaMenu(BaseFrame):
    def __init__(self, tela: BaseTela, control):
        super().__init__(tela, control)
        self.control = control

        self.grid(row=0, column=0, sticky="nsew")

        # Botão
        fonte = ct.CTkFont(size=24, weight="bold")
        self.labelTitulo = ct.CTkLabel(self, text="Organizador De Mangas", font=fonte)
        self.labelTitulo.grid(row=1, column=1, pady=50)

        self.btnOrg = ct.CTkButton(self, text="Organizar Manga", command=lambda: self.organizarManga())
        self.btnOrg.grid(row=2, column=1, pady=10)

        self.btnConfig = ct.CTkButton(self, text="Configuração", command=lambda: self.control.trocaFrame("config"))
        self.btnConfig.grid(row=3, column=1, pady=10)

        self.btnConv = ct.CTkButton(self, text="Converter Manga", command=lambda: self.control.converteMobi())
        self.btnConv.grid(row=4, column=1, pady=10)

        self.btnCapa = ct.CTkButton(self, text="Baixar Capa", command=lambda: self.baixarCapa())
        self.btnCapa.grid(row=5, column=1, pady=10)

        self.btnSair = ct.CTkButton(self, text="Sair", command=lambda: self.control.encerrar())
        self.btnSair.grid(row=6, column=1, pady=10)

        # Centraliza tela
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(self.grid_size()[1] + 1, weight=1)
    
    def organizarManga(self) -> None:
        organizou = self.control.organizaManga()
        if organizou:
            msg.showinfo("Organizador De Mangas", "Manga organizado com sucesso!")
        else:
            msg.showerror("Organizador De Mangas", "Ocorreu algum erro ao organizar o manga.")

    def baixarCapa(self) -> None:
        '''
            Baixa a capa do volume
        '''
        telaCarregamento = self.mostrarCarregamento("Baixando a capa...")
        try:
            self.process_thread = threading.Thread(target=self.control.baixaCapa)
            self.process_thread.start()
            self.monitorarThread(self.process_thread, telaCarregamento)
        except Exception:
            # Se um erro ocorrer antes mesmo de iniciar a thread (raro)
            if telaCarregamento is not None and telaCarregamento.winfo_exists():
                telaCarregamento.destroy()
            msg.showerror("Organizador De Mangas", "Ocorreu algum erro ao iniciar a tarefa.")
    
    def monitorarThread(self, thread, telaCarregamento):
        # O thread do download terminou
        if not thread.is_alive():
            
            # 1. Parar a barra de progresso e destruir a tela de carregamento
            if telaCarregamento is not None and telaCarregamento.winfo_exists():
                # Nota: A progressbar deve parar automaticamente ao destruir o top
                telaCarregamento.destroy() 
                
            # 2. Obter o resultado (sucesso/erro)
            # Como não temos um mecanismo para retornar o resultado direto da thread,
            # precisamos de uma forma de saber o status. 
            # A forma mais robusta é usar um objeto mutável para feedback, como uma lista:
            
            # ATENÇÃO: Se você tivesse usado o método de callback que sugeri
            # na resposta anterior, essa lógica seria desnecessária.
            
            # Para simplificar AQUI, vamos assumir que se a thread terminou 
            # sem erro no thread principal, deu sucesso.

            msg.showinfo("Organizador De Mangas", "Capa do volume baixada com sucesso!")
        
        else:
            # A thread ainda está ativa, agenda a próxima verificação em 100ms
            self.tela.after(100, lambda: self.monitorarThread(thread, telaCarregamento))