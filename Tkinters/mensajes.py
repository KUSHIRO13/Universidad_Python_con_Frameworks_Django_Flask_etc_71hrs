import tkinter as tk
from tkinter import ttk
import os

# Obtener direcion
separador = os.path.sep
direcion_actual = os.getcwd()
direcion = separador.join(direcion_actual.split(separador)[:-1])

ventana = tk.Tk()
ventana.geometry('700x500')
ventana.title('Refuerzo 2')
ventana.iconbitmap(direcion_actual + separador + 'icono' + separador + 'icono.ico')



ventana.mainloop()