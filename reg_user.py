import tkinter as tk
from PIL import ImageTk, Image
from sql import create_tables
import os
import sql
import pandas as pd

class reg_user(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        titulo = tk.Label(self, 
                    text="CADASTRO DE USUÁRIO", 
                    font= "Helvetica 12 bold", 
                    justify= "left", 
                    anchor= "w")
        titulo.pack(side="top", pady=50)

        user = tk.Label(self, 
                            text="Nome de usuário", 
                            font= "Helvetica 12 bold", 
                            justify= "left", 
                            anchor= "w")
        user.pack(side="top")

        campo_user = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_user.pack(pady= 10)


        senha = tk.Label(self, 
                        text="Senha", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        senha.pack(side="top")

        campo_senha = tk.Entry(self, width= 20, font= "Helvetica 12 bold", show = "*")
        campo_senha.pack(pady= 10)

        confirmar = tk.Label(self, 
                text="Confirmar senha", 
                font="Helvetica 12 bold", 
                justify= "left", 
                anchor= "w")
        confirmar.pack(side="top")

        campo_confirmar = tk.Entry(self, width= 20, font= "Helvetica 12 bold", show= "*")
        campo_confirmar.pack(pady= 10)


        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("login_page"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)
        
        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3, command=lambda: validation())
        cadastrar_button.pack(side = "bottom", padx= 20, pady= 20)





        def get_value():
            return [campo_user.get(), campo_senha.get(), campo_confirmar.get()]

        def validation():
            values = get_value()
            msg = ""

            if values[1] != values[2]:
                msg = "A senhas digitadas nos dois campos não são iguais."
            else:
                try:
                    sql.insert_data("tb_user", [values[0], values[1]])
                    msg = "Usuário cadastrado com sucesso."
                except:
                    msg = "Impossível cadastrar. Escolha um novo nome de usuário."
            
            mensagem = tk.Label(self, 
                    text= msg, 
                    font="Helvetica 11 bold", 
                    justify= "left", 
                    anchor= "w")
            mensagem.pack(side="top", pady = 30)

            