# GUI (Graphical User Interface)
# Tkinter (TK Interface)
import tkinter as tk
from tkinter import ttk
import os

def evento_click():
    boton1.config(text='Boton presionado')
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()
    print('Ejecucion del evento')

# Crear objecto
ventana = tk.Tk()
# MOdificar el tamaño de la ventana
ventana.geometry('800x500')
# Cambiar el nombre de la ventana
ventana.title('Hola Mundo')
# Cambiar icono
direcion = os.getcwd()
ventana.iconbitmap(direcion + '\icono\icono.ico')
# Creacion de boton
boton1 = ttk.Button(ventana, text='Boton de click', command=evento_click)
# El pack layout manager muestra los objectos como botones
boton1.pack()
# Inicar ventana
ventana.mainloop()
