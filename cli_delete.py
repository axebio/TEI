import tkinter as tk
from PIL import ImageTk, Image
import sql
import os
import function as fc

class cli_delete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\diamante.png").resize([100, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 50)

        usuario = tk.Label(self, 
                            text="ID do Cliente para excluir", 
                            font= "Helvetica 11 bold", 
                            justify= "left", 
                            anchor= "w")
        usuario.pack(side="top")

        campo_cliente = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_cliente.pack(pady= 10)

        excluir_button = tk.Button(self, 
                                text="EXCLUIR", 
                                width= 100, 
                                height= 3,
                                command=lambda: sql.delete_data("tb_clientes", str(campo_cliente.get())))
        excluir_button.pack(side = "top", padx= 20, pady= 5)
        
        consultar_button = tk.Button(self, 
                                    text="CONSULTAR", 
                                    width= 100, 
                                    height= 3,
                                    command=lambda: [controller.show_frame("cli_consulta"), fc.refresh("tb_cliente")])
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_clientes"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)