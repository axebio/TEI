import tkinter as tk
from PIL import ImageTk, Image
import sql
import os

class func_delete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\diamante.png").resize([100, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 50)

        usuario = tk.Label(self, 
                            text="ID do funcionario para excluir", 
                            font= "Helvetica 11 bold", 
                            justify= "left", 
                            anchor= "w")
        usuario.pack(side="top")

        campo_funcionario = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_funcionario.pack(pady= 10)

        excluir_button = tk.Button(self, 
                                text="EXCLUIR", 
                                width= 100, 
                                height= 3,
                                command=lambda: [sql.delete_data("tb_funcionarios", str(campo_funcionario.get())),
                                clear_text()])
        excluir_button.pack(side = "top", padx= 20, pady= 5)
        
        consultar_button = tk.Button(self, 
                                    text="CONSULTAR", 
                                    width= 100, 
                                    height= 3,
                                    command=lambda: controller.show_frame("func_consulta"))
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_funcionarios"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)

        def clear_text():
            campos = [campo_funcionario]
            for campo in campos:
                campo.delete(0, "end")