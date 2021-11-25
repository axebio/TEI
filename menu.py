import tkinter as tk
from PIL import ImageTk, Image
import os

class menu(tk.Frame):
	def __init__(self, master):
            menubar = tk.Menu(master)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Sair", command=master.quit)
            sobremenu = tk.Menu(menubar, tearoff = 0)
            sobremenu.add_command(label = "Sobre o aplicativo", command= lambda: master.show_frame("sobre_page"))
            menubar.add_cascade(label="Arquivo", menu=filemenu, )
            menubar.add_cascade(label = "Sobre", menu= sobremenu)
            master.config(menu=menubar)