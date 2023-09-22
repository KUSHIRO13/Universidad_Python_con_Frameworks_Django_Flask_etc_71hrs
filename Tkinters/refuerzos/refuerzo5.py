import sys
import tkinter as tk
from tkinter import messagebox, Menu

windows = tk.Tk()
windows.geometry('600x300')
windows.title('Refuerzo 5')

def crear_menu():
    def salir():
        messagebox.showwarning('Salir', 'Saliendo del programa')
        windows.quit()
        windows.destroy()
        sys.exit()

    menu = Menu(windows)

    # Sub menu
    sub_menu1 = Menu(menu, tearoff=False)

    # Opciones
    sub_menu1.add_command(label='Nuevo')
    sub_menu1.add_command(label='Salir', command=salir)

    menu.add_cascade(menu=sub_menu1, label='Archivo')
    menu.add_cascade(menu=sub_menu1, label='Ayuda')



    windows.config(menu=menu)

crear_menu()

windows.mainloop()