from tkinter import messagebox
from six.moves import tkinter as tk
from app.conversor import Conversor


class MainFrame(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # Inicializo a la ventana padre
        self.resultado = None
        self.entrada_temperatura = None
        self.salida_temperatura = None
        self.opcion_seleccionada = None
        self.opciones = []
        self.converter = Conversor()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        # Frame ------------------------------------------------
        self.parent.title("Conversor de Temperatura")
        self.parent.config(bg="#d4cce4")
        self.parent.bind("<Return>", self.convertir_y_calcular)  # Vinculo la tecla "Enter" para ejecutar el cálculo

        # Labels -----------------------------------------------
        titulo = tk.Label(self.parent, text="Elige el tipo de conversión", bg="#d4cce4", font=("Arial", 13))

        # Entries ----------------------------------------------
        self.entrada_temperatura = tk.Entry(self.parent, width=20, font=("Arial", 13))

        self.salida_temperatura = tk.Entry(self.parent, width=20, font=("Arial", 13))

        # Buttons ----------------------------------------------
        boton_resultado = tk.Button(self.parent, text="Calcular", command=self.convertir_y_calcular,
                                    border=1, font=("Arial", 13))  # Calcula el cambio de temperatura

        # Option Menues ----------------------------------------
        self.opcion_seleccionada = tk.StringVar(self.parent)  # Toma como valor_temperatura StringVar
        self.opcion_seleccionada.set("--- Selecciona una opción ---")  # Texto por defecto del recuadro de option menu

        self.opciones = ["Celsius a Fahrenheit", "Celsius a Kelvin",
                         "Fahrenheit a Celsius", "Fahrenheit a Kelvin",
                         "Kelvin a Celsius", "Kelvin a Fahrenheit"]  # Lista de opciones para el menu

        menu_opciones = tk.OptionMenu(self.parent, self.opcion_seleccionada,
                                      *self.opciones)  # Le puse un * para que tome más de 1 valor_temperatura

        # Ajustes widgets ---------------------------------------------
        titulo.place(x=130, y=16)
        menu_opciones.place(x=97, y=55, width=255, height=40)
        menu_opciones["font"] = ("Arial", 11)  # Fuente para el menu
        self.entrada_temperatura.place(x=28, y=120, width=175, height=30)
        self.salida_temperatura.place(x=245, y=120, width=175, height=30)
        boton_resultado.place(x=140, y=175, width=170, height=45)

    # event=None sirve para que no me tire un error al ejecutar con el enter
    def convertir_y_calcular(self, event=None):  # convierte al valor en flotante justo cuando se presiona el botón
        opcion = self.opcion_seleccionada.get()  # obtengo el valor de la opción seleccionada en el option menu

        try:
            valor_temperatura = float(self.entrada_temperatura.get())  # Transformo el valor_temperatura de str a float

            if opcion == self.opciones[0]:
                self.resultado = self.converter.celsius_fahrenheit(valor_temperatura)

            elif opcion == self.opciones[1]:
                self.resultado = self.converter.celsius_kelvin(valor_temperatura)

            elif opcion == self.opciones[2]:
                self.resultado = self.converter.fahrenheit_celsius(valor_temperatura)

            elif opcion == self.opciones[3]:
                self.resultado = self.converter.fahrenheit_kelvin(valor_temperatura)

            elif opcion == self.opciones[4]:
                self.resultado = self.converter.kelvin_celsius(valor_temperatura)

            elif opcion == self.opciones[5]:
                self.resultado = self.converter.kelvin_fahrenheit(valor_temperatura)

            self.salida_temperatura.delete(0, tk.END)  # Elimino el valor actual en la salida de datos
            try:
                # Inserto la temperatura nueva redondeandola
                self.salida_temperatura.insert(0, round(self.resultado, 2))
            except TypeError:
                messagebox.showerror("Error", "Selecciona un tipo de conversión")

            return 0

        except ValueError or TypeError:  # ValueError y TypeError para suplir los problemas
            messagebox.showerror("Error", "Por favor introduce un valor válido")
