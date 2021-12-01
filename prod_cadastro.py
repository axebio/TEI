import tkinter as tk
from PIL import ImageTk, Image
from cli_consulta import *
import os
import sql
import pandas as pd




class prod_cadastro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        titulo = tk.Label(self, 
                    text="CADASTRO DE PRODUTOS", 
                    font= "Helvetica 12 bold", 
                    justify= "left", 
                    anchor= "w")
        titulo.pack(side="top", pady=50)

        nome = tk.Label(self, 
                            text="Nome do Produto", 
                            font= "Helvetica 12 bold", 
                            justify= "left", 
                            anchor= "w")
        nome.pack(side="top")

        campo_nome = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_nome.pack(pady= 10)


        telefone = tk.Label(self, 
                        text="Preco de Compra", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        telefone.pack(side="top")

        campo_telefone = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_telefone.pack(pady= 10)

        email = tk.Label(self, 
                text="Preco de Venda", 
                font="Helvetica 12 bold", 
                justify= "left", 
                anchor= "w")
        email.pack(side="top")

        campo_email = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_email.pack(pady= 10)

        endereco = tk.Label(self, 
                        text="Quantidade", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        endereco.pack(side="top")

        campo_end = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_end.pack(pady= 10)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_produtos"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)
        
        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3, 
                                    command=lambda: [sql.insert_data("tb_produtos", get_value()),
                                    # controller.atualizar("cli_consulta", parent, controller),
                                    clear_text()])
        cadastrar_button.pack(side = "bottom", padx= 20, pady= 20)

        def get_value():
            return [campo_nome.get(), campo_telefone.get(), campo_email.get(), campo_end.get()]


        def clear_text():
            campos = [campo_nome, campo_telefone, campo_email, campo_end]
            for campo in campos:
                campo.delete(0, "end")
