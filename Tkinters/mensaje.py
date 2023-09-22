import os
import tkinter as tk
from tkinter import ttk, messagebox


separador = os.path.sep
direcion_actual = os.getcwd()
direcion = separador.join(direcion_actual.split(separador)[:-1])


window = tk.Tk()
window.geometry('750x500')
window.title('Welcome')
window.iconbitmap(direcion_actual + separador + 'icono' + separador + 'icono.ico')

# Eventos
def welcome():
    texto = text.get()
    text.set('')

    output.config(text=f'Bienvenido!, {inputs.get()}')
    inputs.focus()
    # messagebox.showinfo(f'Mensaje informaivo,', texto + ' Informativo')
    # messagebox.showerror('Es una cadena', texto + ' No es un valor aceptado')
    if not texto:
        messagebox.showwarning('Alerta', 'Esta Vacio')
    else:
        messagebox.showinfo('Te llamas', f'Asi que te llamas {texto}')

# Widgets
label = tk.Label(window, text='Como te llamas?')
text = tk.StringVar(window,'')
inputs = tk.Entry(window, width=30, textvariable=text)
btn_submit = ttk.Button(window, text='Enviar', command=welcome)
output = tk.Label(window, text='')

# Grid
label.grid(row=0, column=0, columnspan=2)
inputs.grid(row=1,column=0)
btn_submit.grid(row=1, column=1)
output.grid(row=2, column=0, sticky='W')

window.mainloop()