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
ventana.iconbitmap(direcion + separador + 'icono' + separador + 'icono.ico')

# Configuracion del Grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=4)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=4)

# Creacion de eventos
def evento_3():
    boton3.config(text='Se presiono', fg='blue', relief=tk.GROOVE, bg='yellow')

# Creacion de botones
boton1 = ttk.Button(text='Boton1')
boton2 = ttk.Button(text='Boton2')
# boton3 = tk.Button(text='Boton3', command=evento_3)
boton4 = ttk.Button(text='Boton4')

# Agregar botones
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=40, ipadx=50, columnspan=2)
boton2.grid(row=1, column=0, sticky='NSWE')
# boton3.grid(row=0, column=1, sticky='NSWE')
boton4.grid(row=1, column=1, sticky='NSWE')

# Abrir ventana
ventana.mainloop()