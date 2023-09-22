import tkinter as tk
from tkinter import ttk
import os

# Obtener la direcion
separador = os.path.sep
direcion_actual = os.getcwd()
direcion = separador.join(direcion_actual.split(separador)[:-1])

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap(direcion + separador + 'icono' + separador + 'icono.ico')
# Confugirar Grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=10)

# Creacion de botones
boton1 = ttk.Button(ventana, text='Boton 1')
boton2 = ttk.Button(ventana, text='Boton 2')
boton3 = ttk.Button(ventana, text='Boton 3')
boton4 = ttk.Button(ventana, text='Boton 4')

# Grib de botones
boton1.grid(row=0, column=0, sticky='NSWE')
boton2.grid(row=1, column=0, sticky='NSWE')
boton3.grid(row=0, column=1, sticky='NSWE')
boton4.grid(row=1, column=1, sticky='NSWE')

# Inicio
ventana.mainloop()