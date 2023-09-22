import tkinter as tk
from tkinter import ttk
import os

# Obtener la direcion
separador = os.path.sep
direcion_actual = os.getcwd()

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap(direcion_actual + separador + 'icono' + separador + 'icono.ico')

# Eventos
def evento_1():
    boton1.config(text='Boton 1 Presionado')

def evento_2():
    boton2.config(text='Boton 2 Presionado')

# N, S, E,W
# Definir botones
boton1 = ttk.Button(ventana,text='Boton 1', command=evento_1)
boton1.grid(row=0,column=0, sticky= tk.E)

boton2 = ttk.Button(ventana, text='Boton 2', command=evento_2)
boton2.grid(row=1,column=0, sticky='W')


# MOstrar ventana
ventana.mainloop()