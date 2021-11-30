import tkinter as tk
from PIL import ImageTk, Image
from menu_func import *
from menu_principal import *
from menu_cliente import *
from login_page import *
from reg_user import reg_user
from sobre_page import *
from menu_produto import *
from menu_vendas import *
from menu import *
from import_csv import *
from cli_delete import *
from cli_cadastro import *
import os


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        menu(self)

        self.title("ValeFarma")
        origin_path = os.path.abspath(os.getcwd())
        self.iconbitmap(origin_path + "\\images\\diamante.ico")

        
        self.geometry("{}x{}+{}+{}".format(400,600, 200, 200))
        self.resizable(False, False)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (login_page, 
                    menu_principal, 
                    sobre_page, 
                    menu_clientes, 
                    menu_produtos, 
                    menu_funcionarios, 
                    menu_vendas,
                    import_csv,
                    cli_consulta,
                    cli_delete,
                    cli_cadastro,
                    reg_user):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("cli_consulta")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()




if __name__ == "__main__":
    app = App()
    app.mainloop()

