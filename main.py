import tkinter as tk
from tkinter import Label, font as tkfont
from tkinter.constants import LEFT
from PIL import ImageTk, Image
import os


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        menu(self)

        self.title("ValeFarma")
        origin_path = os.path.abspath(os.getcwd())
        self.iconbitmap(origin_path + "\\images\\diamante.ico")

        

        self.title_font = tkfont.Font(family='Helvetica', size=12, slant="italic")
        self.geometry("{}x{}+{}+{}".format(400,600, 200, 200))
        self.resizable(False, False)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (login_page, menu_principal, sobre_page, menu_clientes, menu_produtos, menu_funcionarios, menu_vendas):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login_page")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class login_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\diamante.png").resize([100, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 50)

        usuario = tk.Label(self, 
                            text="Nome de usuario", 
                            font= "Helvetica 12 bold", 
                            justify= "left", 
                            anchor= "w")
        usuario.pack(side="top")

        campo_user = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_user.pack(pady= 10)


        senha = tk.Label(self, 
                        text="Senha", 
                        font="Helvetica 12 bold", 
                        justify= "left", 
                        anchor= "w")
        senha.pack(side="top")

        campo_senha = tk.Entry(self, width= 20, font= "Helvetica 12 bold")
        campo_senha.pack(pady= 10)

        bt_entrar = tk.Button(self, 
                    text="Entrar",
                    width= 15,
                    height= 2,
                    command=lambda: controller.show_frame("menu_principal"))
        bt_entrar.pack(pady= 10)

        bt_registrar = tk.Button(self,
                            text="Registrar",
                            width= 15,
                            height= 2,
                            command=lambda: controller.show_frame("menu_clientes"))

        bt_registrar.pack(pady= 10)

class menu_principal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        titulo = Label(self, text= "MENU", font= "Helvetica 12 bold")
        titulo.pack(side= "top")

        clientes_button = tk.Button(self, 
                                    text="CLIENTES", 
                                    width= 100, 
                                    height= 3, 
                                   command=lambda: controller.show_frame("menu_clientes"))

        clientes_button.pack(side = "top", padx= 20, pady= 5)

        produtos_button = tk.Button(self, 
                                    text="PRODUTOS", 
                                    width= 100, 
                                    height= 3,
                                    command=lambda: controller.show_frame("menu_produtos"))
        produtos_button.pack(side = "top", padx= 20, pady= 5)

        funcionarios_button = tk.Button(self, 
                                        text="FUNCIONARIOS", 
                                        width= 100, 
                                        height= 3,
                                        command=lambda: controller.show_frame("menu_funcionarios"))
        funcionarios_button.pack(side = "top", padx= 20, pady= 5)
        
        vendas_button = tk.Button(self, 
                                text="VENDAS", 
                                width= 100, 
                                height= 3,
                                command=lambda: controller.show_frame("menu_vendas"))
        vendas_button.pack(side = "top", padx= 20, pady= 5)
        
        exportar_button = tk.Button(self, 
                                    text="EXPORTAR DADOS", 
                                    width= 100, 
                                    height= 3,
                                    command=lambda: controller.show_frame("menu_exportar"))
        exportar_button.pack(side = "top", padx= 20, pady= 5)

class menu_clientes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        titulo = Label(self, text= "MENU CLIENTES", font= "Helvetica 12 bold")
        titulo.pack(side= "top")


        consultar_button = tk.Button(self, text="CONSULTAR", width= 100, height= 3)
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3)
        cadastrar_button.pack(side = "top", padx= 20, pady= 5)

        excluir_button = tk.Button(self, text="EXCLUIR", width= 100, height= 3)
        excluir_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_principal"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)

class menu_produtos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        titulo = Label(self, text= "MENU PRODUTOS", font= "Helvetica 12 bold")
        titulo.pack(side= "top")


        consultar_button = tk.Button(self, text="CONSULTAR", width= 100, height= 3)
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3)
        cadastrar_button.pack(side = "top", padx= 20, pady= 5)

        excluir_button = tk.Button(self, text="EXCLUIR", width= 100, height= 3)
        excluir_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_principal"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)

class menu_funcionarios(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        titulo = Label(self, text= "MENU FUNCIONARIOS", font= "Helvetica 12 bold")
        titulo.pack(side= "top")


        consultar_button = tk.Button(self, text="CONSULTAR", width= 100, height= 3)
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3)
        cadastrar_button.pack(side = "top", padx= 20, pady= 5)

        excluir_button = tk.Button(self, text="EXCLUIR", width= 100, height= 3)
        excluir_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_principal"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)

class menu_vendas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\valefarma.png").resize([200, 100]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side = "top", pady= 30)

        titulo = Label(self, text= "MENU VENDAS", font= "Helvetica 12 bold")
        titulo.pack(side= "top")


        consultar_button = tk.Button(self, text="CONSULTAR", width= 100, height= 3)
        consultar_button.pack(side = "top", padx= 20, pady= 5)

        cadastrar_button = tk.Button(self, text="CADASTRAR", width= 100, height= 3)
        cadastrar_button.pack(side = "top", padx= 20, pady= 5)

        excluir_button = tk.Button(self, text="EXCLUIR", width= 100, height= 3)
        excluir_button.pack(side = "top", padx= 20, pady= 5)

        voltar_button = tk.Button(self, text="VOLTAR", width= 100, height= 3, command= lambda: controller.show_frame("menu_principal"))
        voltar_button.pack(side = "bottom", padx= 20, pady= 5)

class sobre_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\Rafael.jpg").resize([180, 200]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side="top", fill="x", pady=50)

        nome = Label(self, text= "Desenvolvido por: \n\nRafael Rossi Valentim\nRA: 2840482013009", justify= "left")
        nome.pack(side = "top", pady= 30)
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("menu_principal"))
        button.pack(side= "bottom", pady= 30)

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



if __name__ == "__main__":
    app = App()
    app.mainloop()

