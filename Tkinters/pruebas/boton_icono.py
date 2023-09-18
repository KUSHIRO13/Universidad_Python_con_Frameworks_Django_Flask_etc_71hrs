import tkinter as tk
from tkinter import ttk
import os

# Conseguimos la direcion
direcion_actual = os.getcwd()
separador = os.path.sep
direcion = separador.join(direcion_actual.split(separador)[:-1])
# print(direcion_actual + '')
# print(separador)
# print(direcion)

# Creamos el objeto
ventana = tk.Tk()

# Cambiamos el tamaño
ventana.geometry('500x500')

# Cambiamos el titulo
ventana.title('Creacion del boton y del icono')

# Cambiar el icono
ventana.iconbitmap(direcion + separador + 'icono' + separador + 'icono.ico')

# Creacion del boton
boton1 = ttk.Button(ventana, text='Creacion del boton')
boton1.pack()

# Inicio del programa
ventana.mainloop()