import tkinter as tk
from typing import Container
from cli_consulta import cli_consulta
import login_page as lp
import menu
import cli_consulta
import sql

def refresh(table):
	Frame = tk.Frame
	if table == "tb_user":
		Frame = cli_consulta
	if table == "tb_clientes":
		Frame = cli_consulta
	elif table == "tb_produto":
		Frame = cli_consulta
	Frame.destroy()
	Frame.__init__()