from six.moves import tkinter as tk
from app.views.main_frame import MainFrame
import ctypes

id_ventana = 'company.product.subproduct.version'


def centrar_ventana(ventana):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    posicion_x = (ancho_pantalla - 468) / 2
    posicion_y = (alto_pantalla - 470) / 2
    ventana.geometry("+%d+%d" % (posicion_x, posicion_y))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x250")
    root.iconbitmap("C:/Users/agust/Desktop/Conversor_Temperatura/resources/icons/logo_ventana.ico")
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id_ventana)  # Cambia el ícono de la barra de tareas
    root.resizable(False, False)
    centrar_ventana(root)
    MF = MainFrame(parent=root)
    MF.mainloop()
