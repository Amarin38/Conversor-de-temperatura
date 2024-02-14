from six.moves import tkinter as tk
from app.views.main_frame import *
import ctypes

id = 'company.product.subproduct.version'

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x250")
    root.iconbitmap("C:/Users/agust/Desktop/Conversor_Temperatura/resources/icons/logo_ventana.ico")
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id) # Sirve para cambiar el ícono de la barra de tareas
    root.resizable(False, False)
    MF = MainFrame(parent=root)
    MF.mainloop()
