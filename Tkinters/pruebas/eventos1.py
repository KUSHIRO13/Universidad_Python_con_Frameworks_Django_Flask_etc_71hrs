import tkinter as tk
from tkinter import ttk
import os

# Eventos
def creacion_boton():
    boton = ttk.Button(ventana, text='Boton')
    boton1.config(text='Se presiono el boton ')
    boton.pack()

# Obtener la direcion
separador = os.path.sep
dir_actual = os.getcwd()
direcion = separador.join(dir_actual.split(separador)[:-1])


# Creacion de la ventana
ventana = tk.Tk()

# Cambiar el tamaño de la ventana
ventana.geometry('600x300')

# Cambiar titulo
ventana.title('Eventos')

# Cambiar icono
ventana.iconbitmap(direcion + separador + 'icono' + separador + 'icono.ico')

# Palabras
palabras = ['Hola', 'como', 'Andres', 'Python', 'Pycharm']


# Creacion del boton
boton1 = ttk.Button(ventana, text='Has click', command=creacion_boton)
boton1.pack()

# Iniciar programa
ventana.mainloop()