import tkinter as tk
# from tkinter.constants import S
from pandas.core import frame
from pandastable import Table, TableModel
import sql  
import os

class cli_consulta(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        df = sql.select_data("tb_clientes")
        df.set_index("id_clientes")

        table_frame = tk.Frame(self, width= 43, height= 450)
        table_frame.grid(row= 0, column= 0, sticky= "ew")
        
        pt = Table(table_frame, dataframe=df, showtoolbar=False, showstatusbar=False, width= 43, height= 450)
        
        pt.show()
        pt.grid(sticky= "nsew")



        bt_frame = tk.Frame(self)
        bt_frame.grid(column= 0, row= 1, padx= 20, pady= 5, sticky= "s")

        voltar_button = tk.Button(bt_frame, text="VOLTAR", width= 43, height= 3, command= lambda: controller.show_frame("menu_clientes"))
        voltar_button.grid(column= 0, row= 1, padx= 20, pady= 5, sticky= "s")

