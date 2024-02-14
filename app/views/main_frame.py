from six.moves import tkinter as tk
from app.conversor import *


class MainFrame(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # inicializo a la ventana padre
        self.entrada_temp = None
        self.salida_temp = None
        self.converter = Conversor()  # inicializo el conversor
        self.parent = parent
        self.init_ui()  # inicializo los widgets

    def init_ui(self):
        self.parent.title("Conversor de Temperatura")
        self.parent.config(bg="#d4cce4")
        # Imagenes -----------------------------------------------

        # Labels -----------------------------------------------
        titulo = tk.Label(self.parent, text="Elige el tipo de conversión", bg="#d4cce4", font=("Arial", 13))

        # Entries -----------------------------------------------
        self.entrada_temp = tk.Entry(self.parent, width=20,
                                     font=("Arial", 13))  # Cuadro de entrada para el valor de la temperatura
        self.salida_temp = tk.Entry(self.parent, width=20, font=("Arial", 13),
                                    state="readonly")  # Cuadro de salida para el valor de la temperatura

        # Buttons -----------------------------------------------
        boton = tk.Button(self.parent, text="Calcular", command=self.convertir_y_calcular,
                          border=1, font=("Arial", 13))  # Este boton muestra el resultado de las cuentas

        # Option Menues -----------------------------------------------
        texto_interno = tk.StringVar()  # valor para ingresar en los widgets
        texto_interno.set("--- Selecciona una opción ---")  # texto interno del recuadro de option menu
        lista_menu = ["Celsius a Fahrenheit", "Celsius a Kelvin", "Fahrenheit a Celsius", "Fahrenheit a Kelvin",
                      "Kelvin a Celsius", "Kelvin a Fahrenheit"]

        menu_opciones = tk.OptionMenu(self.parent, texto_interno, *lista_menu)  # le puse un * para que tome más de 1 valor
        menu_opciones["font"] = ("Arial", 11) #fuente para el menu

        # Ajustes widgets ---------------------------------------------
        titulo.place(x=130, y=16)
        menu_opciones.place(x=97, y=55, width=255, height=40)
        self.entrada_temp.place(x=28, y=120, width=175, height=30)
        self.salida_temp.place(x=245, y=120, width=175, height=30)
        boton.place(x=140, y=175, width=170, height=45)

    def convertir_y_calcular(self):  # convierte al valor en flotante justo cuando se presiona el botón
        try:
            resultado = float(self.entrada_temp.get())
            self.converter.celsius_fahrenheit(resultado)
        except ValueError:
            print("Por favor ingresa un número")

    # Cuando clickea el boton que aparezca el resultado acá
    # def mostrar_entry(self):
    #    if self.salida_temp.get() == '':
    #        self.salida_temp
