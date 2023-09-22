import tkinter as tk
from tkinter import ttk, messagebox, Menu
import os


separador = os.path.sep
direcion_actual = os.getcwd()
direcion = separador.join(direcion_actual.split(separador)[:-1])

windows = tk.Tk()
windows.geometry('500x500')
windows.title('Menus')
windows.iconbitmap(direcion_actual + separador + 'icono' + separador + 'icono.ico')

# Eventos
def entrada_datos():
    text = texto.get()
    if not text:
        messagebox.showerror('No hay valor', 'No has ingresado algun valor')
        label.config(text='¡¡¡ERROR!!!')
    else:
        messagebox.showinfo('Tu nombre', 'Se imprimira tu nombre')
        label.config(text=f'Bienvenido!, {text}')
    texto.set('')
    entrada.focus()

def crear_menu():
    # Configurar menu
    menu_principal = Menu(windows)
    menu_archivo = Menu(menu_principal, tearoff=False)

    # Opciones
    menu_archivo.add_command(label='Nuevo')
    # Submenu
    menu_principal.add_cascade(menu=menu_archivo, label='Archivo')
    # Miostra menu
    windows.config(menu=menu_principal)

crear_menu()

# Widgets
texto = tk.StringVar(windows, value='')
entrada = tk.Entry(windows, width=20,textvariable=texto)
btn1 = tk.Button(windows, text='Enviar', command=entrada_datos)
label = tk.Label(windows, text='')

# Grid
entrada.grid(row=0, column=0)
btn1.grid(row=0, column=1)
label.grid(row=1,column=0)

windows.mainloop()