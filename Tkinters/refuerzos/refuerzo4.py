import tkinter as tk
from tkinter import Menu, messagebox


ventana = tk.Tk()
ventana.geometry('500x500')
ventana.title('Refuerzo 4')

# Crear menu
def crear_menu():
    menu = Menu(ventana)
    # Sub menus
    sub_menu1 = Menu(menu, tearoff=False)
    sub_menu2 = Menu(menu, tearoff=False)

    # Opciones
    sub_menu1.add_command(label='Nuevo')
    # Agregar separador
    sub_menu1.add_separator()
    sub_menu1.add_command(label='Salir')

    sub_menu2.add_command(label='Acerca de')
    # Agregar menu,
    menu.add_cascade(menu=sub_menu1, label='Archivo')
    menu.add_cascade(menu=sub_menu2, label='Ayuda')

    ventana.config(menu=menu)

crear_menu()

# Eventos
def aceptar():
    if txt1.get():
        label.config(text=txt1.get())
        txt1.set('')
        txtfield1.focus()
    else:
        messagebox.showerror('Ocurrio un error', 'La casilla esta vacia')

# Widgets
txt1 = tk.StringVar(ventana, value='')
txtfield1 = tk.Entry(ventana, textvariable=txt1)
btn_submit1 = tk.Button(ventana, text='Enviar', command=aceptar)
label = tk.Label(ventana, text='')

# Grid
txtfield1.grid(row=0, column=0)
btn_submit1.grid(row=0, column=1)
label.grid(row=1, column=0, sticky='W')

ventana.mainloop()