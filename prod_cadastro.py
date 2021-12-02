import tkinter as tk
from PIL import ImageTk, Image
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
                            text="Nome do produto", 
                            font= "Helvetica 12 bold", 
                            justify= "left", 
                            anchor= "w")
        nome.pack(side="top")

        campo_nome = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_nome.pack(pady= 10)

        compra = tk.Label(self, 
                        text="Preco de Compra", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        compra.pack(side="top")

        campo_compra = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_compra.pack(pady= 10)

        venda = tk.Label(self, 
                text="Preco de vendas", 
                font="Helvetica 12 bold", 
                justify= "left", 
                anchor= "w")
        venda.pack(side="top")

        campo_venda = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_venda.pack(pady= 10)

        qnt = tk.Label(self, 
                        text="Quantidade", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        qnt.pack(side="top")

        campo_qnt = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_qnt.pack(pady= 10)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_produtos"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)
        
        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3, 
                                    command=lambda: [sql.insert_data("tb_produtos", get_value()),
                                    # controller.atualizar("cli_consulta", parent, controller),
                                    clear_text()])
        cadastrar_button.pack(side = "bottom", padx= 20, pady= 20)

        def get_value():
            return [campo_nome.get(), campo_compra.get(), campo_venda.get(), campo_qnt.get()]


        def clear_text():
            campos = [campo_nome, campo_compra, campo_venda, campo_qnt]
            for campo in campos:
                campo.delete(0, "end")
