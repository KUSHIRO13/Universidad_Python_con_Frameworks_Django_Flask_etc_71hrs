import sys
import os
import tkinter as tk
from tkinter import messagebox, Menu

def ventanas():
    # Buscar la direcion

    separador = os.path.sep
    dir_actual = os.getcwd()
    dir_ = separador.join(dir_actual.split(separador)[:-1])

    ventana = tk.Tk()
    ventana.title('login/Ingreso')
    ventana.geometry('300x130')
    ventana.iconbitmap(dir_ + separador + 'icono' + separador + 'icono.ico')

    # Menu
    def crear_menu():
        # Eventos del menu
        def exit():
            messagebox.showwarning('Saliendo', 'Saliendo del programa')
            menu.quit()
            menu.destroy()
            sys.exit()

        menu = Menu(ventana)

        # Crear submenu
        sub_menu1 = Menu(menu, tearoff=False)

        # Crear opciones
        sub_menu1.add_command(label='Salir', command=exit)

        menu.add_cascade(menu=sub_menu1, label='Archivo')

        # Añadir menu
        ventana.config(menu=menu)

    crear_menu()

    # Configuraciones
    ventana.rowconfigure(0, weight=1)
    ventana.rowconfigure(1, weight=1)
    ventana.rowconfigure(2, weight=3)
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=4)

    # Eventos
    def entrar():
        usuario = txtfield1.get()
        contrasena = txtfield2.get()
        resultados = ['Usuario', 'Contraseña']

        if not usuario and not contrasena:
            messagebox.showerror('No existen datos','Error: No ingresastes ni tu usuario ni tu contraseña')
        elif not contrasena or not usuario:
            messagebox.showwarning('Datos inconclusos', f'No ingresastes tu {resultados[int(bool(usuario))]}')
        else:
            messagebox.showinfo('Bienvenido', f'Usuario: {usuario}\nContraseña: {contrasena}')
    # Widgets
    label1 = tk.Label(ventana, text='Usuario:')
    label2 = tk.Label(ventana, text='Password:')
    txtfield1 = tk.Entry(ventana, width=25)
    txtfield2 = tk.Entry(ventana, width=25, show='*')
    btn_submit = tk.Button(ventana, text='Login', command=entrar)

    # Grid
    label1.grid(row=0, column=0, padx='25')
    label2.grid(row=1, column=0, sticky='N', padx='25')
    txtfield1.grid(row=0, column=1, sticky='W')
    txtfield2.grid(row=1, column=1, sticky='NW')
    btn_submit.grid(row=2,column=0, columnspan=2,sticky='N')


    return tk.mainloop()

if __name__ == '__main__':
    ventanas()