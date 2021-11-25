import tkinter as tk
from PIL import ImageTk, Image
from sql import create_tables
import os

class login_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\diamante.png").resize([100, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 50)

        usuario = tk.Label(self, 
                            text="Nome de usuario", 
                            font= "Helvetica 12 bold", 
                            justify= "left", 
                            anchor= "w")
        usuario.pack(side="top")

        campo_user = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_user.pack(pady= 10)


        senha = tk.Label(self, 
                        text="Senha", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        senha.pack(side="top")

        campo_senha = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_senha.pack(pady= 10)

        bt_entrar = tk.Button(self, 
                    text="Entrar",
                    width= 15,
                    height= 2,
                    command=lambda: controller.show_frame("menu_principal"))
        bt_entrar.pack(pady= 10)

        bt_registrar = tk.Button(self,
                            text="Registrar",
                            width= 15,
                            height= 2,
                            command=lambda: controller.show_frame(create_tables()))

        bt_registrar.pack(pady= 10)