import tkinter as tk
from PIL import ImageTk, Image
from func_consulta import *
import os
import sql
import pandas as pd




class func_cadastro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        titulo = tk.Label(self, 
                    text="CADASTRO DE FUNCIONARIOS", 
                    font= "Helvetica 12 bold", 
                    justify= "left", 
                    anchor= "w")
        titulo.pack(side="top", pady=50)

        nome = tk.Label(self, 
                            text="Nome do funcionario", 
                            font= "Helvetica 12 bold", 
                            justify= "left", 
                            anchor= "w")
        nome.pack(side="top")

        campo_nome = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_nome.pack(pady= 10)


        cpf = tk.Label(self, 
                        text="CPF", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        cpf.pack(side="top")

        campo_cpf = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_cpf.pack(pady= 10)

        telefone = tk.Label(self, 
                text="Telefone", 
                font="Helvetica 12 bold", 
                justify= "left", 
                anchor= "w")
        telefone.pack(side="top")

        campo_telefone = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_telefone.pack(pady= 10)

        funcao = tk.Label(self, 
                        text="Funcao", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        funcao.pack(side="top")

        campo_funcao = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_funcao.pack(pady= 10)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_funcionarios"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)
        
        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3, 
                                    command=lambda: [sql.insert_data("tb_funcionarios", get_value()),
                                    clear_text()])
        cadastrar_button.pack(side = "bottom", padx= 20, pady= 20)

        def get_value():
            return [campo_nome.get(), campo_cpf.get(), campo_telefone.get(), campo_funcao.get()]


        def clear_text():
            campos = [campo_nome, campo_cpf, campo_telefone, campo_funcao]
            for campo in campos:
                campo.delete(0, "end")
