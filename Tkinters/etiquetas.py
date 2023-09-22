import tkinter as tk
from tkinter import ttk
import os

# Obtener direcion
separador = os.path.sep
direcion_actual = os.getcwd()
direcion = separador.join(direcion_actual.split(separador)[:-1])

ventana = tk.Tk()
ventana.geometry('700x500')
ventana.title('Etiquetas')
ventana.iconbitmap(direcion_actual + separador + 'icono' + separador + 'icono.ico')

# Eventos
def bienvenida():
    # Obtener texto
    texto = text.get()
    # Vaciar casilla
    text.set('')
    textfield.focus()

    # Agregar texto al labels
    etiqueta2.config(text=f'Bienvenido!, {texto}')

# Widgets
text = tk.StringVar(value='')
etiqueta1 = tk.Label(ventana,text='Ingrese un nombre')
etiqueta2 = tk.Label(ventana,)
textfield = ttk.Entry(ventana, width=30, textvariable=text)
btn_submit = ttk.Button(ventana,text='Enviar', command=bienvenida)

# Grid
etiqueta1.grid(row=0, column=0, columnspan=2)
textfield.grid(row=1, column=0)
btn_submit.grid(row=1,column=1)
etiqueta2.grid(row=2, column=0)

ventana.mainloop()