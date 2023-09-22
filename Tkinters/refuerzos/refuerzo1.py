import tkinter as tk
from tkinter import ttk
import os

# Eventos
def evento_click():
    boton = ttk.Button(ventana, text='Boton nuevo')
    boton.pack()
    boton1.config(text='Presionastes el boton')

separador = os.path.sep
direccion_actual = os.getcwd()
direcion = separador.join(direccion_actual.split(separador)[:-1])

# Creacion de la ventana
ventana = tk.Tk()

# Cambiar tamaño
ventana.geometry('500x500')

# Cambiar titulo
ventana.title('Refuerzo 1')

# Cambiar icono
ventana.iconbitmap(direcion + separador + 'icono' + separador + 'icono.ico')

# Añadir boton
boton1 = ttk.Button(ventana, text='Has click', command=evento_click)
boton1.pack()

# Inicio del programa
ventana.mainloop()