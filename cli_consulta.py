import tkinter as tk
from tkinter.constants import S
from pandastable import Table, TableModel
import sql  
import os

class cli_consulta(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        df = sql.select_data("tb_clientes")
        
        pt = Table(self, dataframe=df, showtoolbar=False, showstatusbar=False)
        pt.show()

        mostrar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3)
        mostrar_button.grid(column= 1, row= 1, padx= 20, pady= 5, sticky= S)
        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_clientes"))
        voltar_button.grid(column= 1, row= 1, padx= 20, pady= 5, sticky= S)

        # titulo = tk.Label(self, text= "MENU CLIENTES", font= "Helvetica 12 bold")
        # titulo.pack(side= "top")


        # consultar_button = tk.Button(self, text="CONSULTAR", width= 100, height= 3)
        # consultar_button.pack(side = "top", padx= 20, pady= 5)

        # cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3)
        # cadastrar_button.pack(side = "top", padx= 20, pady= 5)

        # excluir_button = tk.Button(self, text="EXCLUIR", width= 100, height= 3)
        # excluir_button.pack(side = "top", padx= 20, pady= 5)

        # voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_principal"))
        # voltar_button.pack(side = "bottom", padx= 20, pady= 5)