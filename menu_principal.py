import tkinter as tk
from PIL import ImageTk, Image
import os
from import_csv import import_csv
from menu_exportar import *



class menu_principal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        titulo = tk.Label(self, text= "MENU", font= "Helvetica 12 bold")
        titulo.pack(side= "top")

        clientes_button = tk.Button(self, 
                                    text="CLIENTES", 
                                    width= 100, 
                                    height= 3, 
                                   command=lambda: controller.show_frame("menu_clientes"))

        clientes_button.pack(side = "top", padx= 20, pady= 5)

        produtos_button = tk.Button(self, 
                                    text="PRODUTOS", 
                                    width= 100, 
                                    height= 3,
                                    command=lambda: controller.show_frame("menu_produtos"))
        produtos_button.pack(side = "top", padx= 20, pady= 5)

        funcionarios_button = tk.Button(self, 
                                        text="FUNCIONARIOS", 
                                        width= 100, 
                                        height= 3,
                                        command=lambda: controller.show_frame("menu_funcionarios"))
        funcionarios_button.pack(side = "top", padx= 20, pady= 5)
        
        vendas_button = tk.Button(self, 
                                text="VENDAS", 
                                width= 100, 
                                height= 3,
                                command=lambda: controller.show_frame("menu_vendas"))
        vendas_button.pack(side = "top", padx= 20, pady= 5)
        
        exportar_button = tk.Button(self, 
                                    text="EXPORTAR DADOS", 
                                    width= 100, 
                                    height= 3,
                                    command=lambda: exportar_json())
        exportar_button.pack(side = "top", padx= 20, pady= 5)

        importar_button = tk.Button(self, 
                                    text="IMPORTAR DADOS", 
                                    width= 100, 
                                    height= 3,
                                    command=lambda: controller.show_frame("import_csv"))
        importar_button.pack(side = "top", padx= 20, pady= 5)