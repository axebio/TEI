import pandas as pd
import urllib.request
import tkinter as tk
# from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from tkinter import filedialog


import sql




class import_csv(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        titulo = tk.Label(self, text= "MENU IMPORTAR DADOS", font= "Helvetica 12 bold")
        titulo.pack(side= "top", pady= 20)

        cb_label = tk.Label(self, 
                        text="Escolha o destino dos dados que serão importados.", 
                        font="Helvetica 10 bold", 
                        justify= "left", 
                        anchor= "w")
        cb_label.pack(side="top", pady= 20)

        opcoes = ["Clientes", "Produtos", "Funcionarios", "Vendas"]

        cb = ttk.Combobox(self, 
                            text = "Escolha o tipo de dados que deseja importar:",
                            values= opcoes)
        cb.pack(pady=30)

        url_csv = tk.Label(self, 
                        text="Insira o endereço URL do arquivo .csv para importar", 
                        font="Helvetica 10 bold", 
                        justify= "left", 
                        anchor= "w")
        url_csv.pack(side="top")

        campo_url = tk.Entry(self, width= 40, font= "Helvetica 12 bold")
        campo_url.pack(pady= 10)

        OK_button = tk.Button(self, text="IMPORTAR", width= 100, height= 3, command= lambda: self.usar_url(campo_url.get(), cb.get()))
        OK_button.pack(side = "top", padx= 20, pady= 5)


        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_principal"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 10)

        import_button = tk.Button(self, text="SELECIONAR ARQUIVO", 
                                    width= 100, 
                                    height= 3, 
                                    command= lambda: [self.usar_arquivo(cb.get())])
        import_button.pack(side = "bottom", padx= 20, pady= 5)

        select_csv = tk.Label(self, 
                        text="Ou selecione um arquivo .csv para importar.", 
                        font="Helvetica 10 bold", 
                        justify= "left", 
                        anchor= "w")
        select_csv.pack(side="bottom", pady= 20)

        def exito(i):
            if i == True:
                msg = "O arquivo foi importado com sucesso."
                messagebox.showinfo("Erro ao acessar o sistema.", msg)
            else:
                msg = "Erro ao importar o arquivo."
                messagebox.showinfo("Erro ao acessar o sistema.", msg)
    
    def usar_url(self, url, escolha):
        df = pd.DataFrame


        response = urllib.request.urlopen(url)

        if url[-4:] == ".csv":
            df = pd.read_csv(response)
        elif url[-4:] == "json":
            df = pd.read_json(response)

        escolha = self.get_cb(escolha)
        sql.prepara_import(escolha, df)


    def usar_arquivo(self, escolha):
        df = pd.DataFrame
        origin_path = os.path.abspath(os.getcwd())
        self.filename = filedialog.askopenfilename(initialdir=origin_path, title= "Selecione um arquivo .csv ou .json")

        if self.filename[-4:] == ".csv":
            df = pd.read_csv(self.filename, index_col= False)
        elif self.filename[-4:] == "json":
            df = pd.read_json(self.filename, index_col = False)

        escolha = self.get_cb(escolha)
        sql.prepara_import(escolha, df)

    def get_cb(self, escolha):
        if escolha == "Clientes":
            return "tb_clientes"
        elif escolha == "Produtos":
            return "tb_produtos"
        elif escolha == "Funcionarios":
            return "tb_funcionarios"
        elif escolha == "Vendas":
            return "tb_vendas"
    



