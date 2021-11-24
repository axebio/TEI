from tkinter import *
from typing import Container
import login_page as lp
import menu

def menu_(file):
	if (file == "tela_start"):
		return menu.menu1()
	else:
		return menu.menu2()