import tkinter as tk
from pandastable import Table, TableModel
import sql  
import os

class func_consulta(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
   
        self.create_frame(parent, controller)
        
    def create_frame(self, parent, controller):

        self.controller = controller
        self.parent = parent
        
        df = sql.select_data("tb_funcionarios")
        df.set_index("id_funcionarios")

        table_frame = tk.Frame(self, width= 60, height= 450)
        table_frame.grid(row= 0, column= 0, sticky= "ew")

        pt = Table(table_frame, dataframe=df, showtoolbar=False, showstatusbar=False, width= 43, height= 450)
        
        pt.show()
        bt_frame = tk.Frame(self)
        bt_frame.grid(column= 0, row= 1, pady= 5, sticky= "s", columnspan=1)

        atualizar_button = tk.Button(bt_frame, text= "ATUALIZAR", width=  25, height= 3,
                                    command= lambda: self.create_frame(parent, controller),
                                    )
        atualizar_button.grid(column= 0, row= 1, padx= 5, pady= 5, sticky= "s")

        voltar_button = tk.Button(bt_frame, text="VOLTAR", width= 25, height= 3,
                                    command=  lambda: controller.show_frame("menu_funcionarios")                      
                                    )
        voltar_button.grid(column= 1, row= 1, padx= 5, pady= 5, sticky= "s")
    
            