import tkinter as tk
from tkinter import ttk
import os

separador = os.path.sep
direccion_actual = os.getcwd()
direccion = separador.join(direccion_actual.split(separador)[:-1])

ventana = tk.Tk()
ventana.title('Refuerzo 3')
ventana.geometry('750x400')
ventana.iconbitmap(direccion + separador + 'icono' + separador + 'icono.ico')

# Eventos
def guardar():
    texto = textfield1.get()
    textfield2.config(state=tk.NORMAL)
    textfield2.delete(0, tk.END)
    textfield2.insert(0,texto)
    textfield2.config(state='readonly')

    textfield1.delete(0, tk.END)
    textfield1.focus()


# Widgets
textfield1 = ttk.Entry(ventana)
textfield2 = ttk.Entry(ventana, state='readonly')
btn1 = ttk.Button(ventana, text='Enviar', command=guardar)

# Grid
textfield1.grid(row=0,column=0)
textfield2.grid(row=1,column=0)
btn1.grid(row=0, column=1)

ventana.mainloop()