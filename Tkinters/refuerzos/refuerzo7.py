
import sys
import os
import tkinter as tk
from tkinter import ttk, Menu, messagebox

sep = os.path.sep
actual_dir = os.getcwd()
programm_dir = sep.join(actual_dir.split(sep)[:-1])
class LoginUser(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuracion de pagina
        self.geometry('300x130')
        self.resizable(0,0)
        self.iconbitmap(programm_dir + sep + 'icono' + sep + 'icono.ico')
        self.title('Refuerzo 7')

        # Eventos iniciales
        self._set_limits()
        self._create_menu()
        self._create_widgets()

    def _set_limits(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def _create_menu(self):
        self.menu = Menu(self)
        sub_menu1 = Menu(self.menu, tearoff=False)
        sub_menu1.add_command(label='Salir', command=self.close)
        self.menu.add_cascade(label='Archivos', menu=sub_menu1)
        self.config(menu=self.menu)

    def close(self):
        messagebox.showwarning('Saliendo', 'Saliendo del programa')
        self.menu.quit()
        self.menu.destroy()
        sys,quit()

    def _create_widgets(self):
        # Etiquetas
        lbl_user = ttk.Label(self, text='Usuario:')
        lbl_password = ttk.Label(self, text='Contraseña:')

        # Entradas
        self.txt_user = ttk.Entry(self, width=30)
        self.txt_password = ttk.Entry(self, show='*', width=30)

        # Botones
        btn_submit = ttk.Button(self, text='Ingresar', command=self._events)
        
        # Grid
        lbl_user.grid(row=0, column=0, sticky='E', padx=5, pady= 5)
        lbl_password.grid(row=1, column=0, sticky='E', padx=5, pady= 5)

        self.txt_user.grid(row=0, column=1, pady= 5, sticky='W', padx=5)
        self.txt_password.grid(row=1,column=1, pady= 5, sticky='W', padx=5)

        btn_submit.grid(row=2, column=0, columnspan=2, sticky='N', pady= 5)

    def _events(self):
        txt_user_value = self.txt_user.get()
        txt_password_value = self.txt_password.get()
        if txt_password_value and txt_user_value:
            messagebox.showinfo('Datos completos', f'Usuario: {txt_user_value}\n'
                                                   f'Password: {txt_password_value}')
        elif txt_user_value or txt_password_value:
            messagebox.showwarning('Datos incompletos',
                                   f'Dato faltante "{"Usuario" if txt_password_value else "Contraseña"}"')
        else:
            messagebox.showerror('Sin datos', 'No has ingresado ningun dato')


if __name__ == '__main__':
    windows = LoginUser()
    windows.mainloop()