import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
import json
import zipfile as zp
from sql import *
import os

origin_path = os.path.abspath(os.getcwd())
path = origin_path + "\\output.json"

tabelas = ["tb_user", "tb_clientes", "tb_produtos"]
df = []

for i in tabelas:
    a = select_data(i)
    foo = i
    exec(foo + " = '' ")
    i = pd.DataFrame()
    i = a
    df.append(i)

out_file = open("output.json", "w", encoding= "utf-8")

for i in range(len(df)):
    json.dump(pd.DataFrame.to_json(df[i]), out_file, indent= 4)
    f = df[i].reset_index().to_json(orient= 'records')
    with zp.ZipFile("compressed_data.zip", mode= "a" , compression=zp.ZIP_DEFLATED, compresslevel=9) as zip_file: 
        dumped_JSON: str = json.dumps(f, ensure_ascii=False, indent=4)

        zip_file.writestr("{}.json".format(tabelas[i]), data=dumped_JSON)

        zip_file.testzip()

out_file.close()
os.remove(path)
    

