import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

sep = os.path.sep
actual_dir = os.getcwd()

windows = tk.Tk()
windows.geometry('600x400')
windows.title('Componentes')
windows.iconbitmap(actual_dir + sep + 'icono' + sep + 'icono.ico')

def create_tabs():
    # Creamos un Tabs control
    control_tab = ttk.Notebook(windows)



    def tabulacion1():    # Agregar Frame
        tab1 = ttk.Frame(control_tab)
        def enviar():
            messagebox.showinfo('Datos', f'Usuario: {entrada1.get()}')
        control_tab.add(tab1, text='Tabulador 1')
        control_tab.pack(fill='both')

        etiqueta1 = ttk.Label(tab1, text='Nombre:')
        etiqueta1.grid(row=0, column=0, sticky='E')

        entrada1 = ttk.Entry(tab1, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        boton1 = ttk.Button(tab1, text='Enviar', command=enviar)
        boton1.grid(row=1, column=0, columnspan=2)

    def tabulacion2(tab):

        content = 'Este es mi contenido'

        scroll = scrolledtext.ScrolledText(tab, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, content)

        scroll.grid(row=0, column=0)

    tab2 = ttk.Labelframe(control_tab, text='Contenido')
    control_tab.add(tab2, text='Tabulacion 2')
    control_tab.pack(fill='both')

    tabulacion1()
    tabulacion2(tab2)

create_tabs()

windows.mainloop()