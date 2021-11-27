import pandas as pd
import urllib.request
import tkinter as tk
from tkinter import filedialog
import os

from pandas.io.parsers import read_csv


class import_csv(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        origin_path = os.path.abspath(os.getcwd())
        # tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        # label = tk.Label(self, image=tkimage)
        # label.image = tkimage
        # label.pack(side = "top", pady= 30)

        titulo = tk.Label(self, text= "MENU FUNCIONARIOS", font= "Helvetica 12 bold")
        titulo.pack(side= "top")


        consultar_button = tk.Button(self, text="CONSULTAR", width= 100, height= 3, command= lambda: self.importar_csv())
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3)
        cadastrar_button.pack(side = "top", padx= 20, pady= 5)

        excluir_button = tk.Button(self, text="EXCLUIR", width= 100, height= 3)
        excluir_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3)
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)
    
    def importar_url(url):
        response = urllib.request.urlopen(url)

        df = pd.read_csv(response)

        return df


    def importar_csv(self):
        origin_path = os.path.abspath(os.getcwd())
        self.filename = filedialog.askopenfilename(initialdir=origin_path, title= "Selecione um arquivo .csv")
        print(self.filename)
        df = read_csv(self.filename)


# for i in dataframe.index:
#     query = """
#     INSERT into emissions(column1, column2, column3) values('%s',%s,%s);
#     """ % (dataframe['column1'], dataframe['column2'], dataframe['column3'])
#     single_insert(conn, query)