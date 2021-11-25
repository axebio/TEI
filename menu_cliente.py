import tkinter as tk
from PIL import ImageTk, Image
import os

class menu_clientes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        titulo = tk.Label(self, text= "MENU CLIENTES", font= "Helvetica 12 bold")
        titulo.pack(side= "top")


        consultar_button = tk.Button(self, text="CONSULTAR", width= 100, height= 3)
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3)
        cadastrar_button.pack(side = "top", padx= 20, pady= 5)

        excluir_button = tk.Button(self, text="EXCLUIR", width= 100, height= 3)
        excluir_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_principal"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)