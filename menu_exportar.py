import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
import json
import zipfile as zp
from sql import *
import os

def exportar_json():
    try:
        origin_path = os.path.abspath(os.getcwd())
        path = origin_path + "\\output.json"

        tabelas = ["tb_user", "tb_clientes", "tb_produtos", "tb_funcionarios"]
        df = []

        for i in tabelas:
            id = 'id_' + i.split("_")[1]
            a = select_data(i)
            foo = i
            exec(foo + " = '' ")
            i = pd.DataFrame
            i = a
            i.set_index([id], inplace= True)
            df.append(i)
            

        out_file = open("output.json", "w", encoding= "utf-8")

        for i in range(len(df)):
            json.dump(pd.DataFrame.to_json(df[i]), out_file, indent= 4 )
            f = df[i].reset_index().to_json(orient= 'records')
            f= json.loads(f)
            with zp.ZipFile("output.zip", mode= "a" , compression=zp.ZIP_DEFLATED, compresslevel=9) as zip_file: 
                dp_JSON: str = json.dumps(f, ensure_ascii=False, indent=4)

                zip_file.writestr("{}.json".format(tabelas[i]), data=dp_JSON)

                zip_file.testzip()

        out_file.close()
        msg = "O arquivo {}/output.zip contem todos os .json e foi gerado com sucesso".format(origin_path)
        messagebox.showinfo("Dados exportados", msg)
    except:
        msg = "Erro ao exportar os dados, por favor verifique e tente novamente."
        messagebox.showinfo("Impossivel exportar os dados.", msg)

    

