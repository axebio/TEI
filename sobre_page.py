import tkinter as tk
from PIL import ImageTk, Image
import os

class sobre_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        origin_path = os.path.abspath(os.getcwd())
        tkimage = ImageTk.PhotoImage(Image.open(origin_path + "\\images\\Rafael.jpg").resize([180, 200]))
        label = tk.Label(self, image=tkimage)
        label.image = tkimage
        label.pack(side="top", fill="x", pady=50)

        nome = tk.Label(self, text= "Desenvolvido por: \n\nRafael Rossi Valentim\nRA: 2840482013009", justify= "left")
        nome.pack(side = "top", pady= 30)
        
        button = tk.Button(self, text="LOGOUT",
                           command=lambda: controller.show_frame("login_page"))
        button.pack(side= "bottom", pady= 30)