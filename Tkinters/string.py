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

# Eventos
def btn_text():
    texto = entrada1.get()
    caja = ttk.Entry(ventana, width=30)
    caja.insert(0, f'Hola¡ {texto}')
    entrada1.delete(0, tk.END)
    caja.config(state=tk.DISABLED)
    caja.grid(row=1, column=0)


variable1 = tk.StringVar(value='Valor por default')
# Creacion de entradas
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL, textvariable=variable1)
entrada1.grid(row=0, column=0)
# entrada1.insert(0, 'Introduce una cadena de texto')
# entrada1.config(state='readonly')

# Creacion de botones
boton1 = ttk.Button(ventana, text='Enviar', command=btn_text)
boton1.grid(row=0, column=1)

ventana.mainloop()