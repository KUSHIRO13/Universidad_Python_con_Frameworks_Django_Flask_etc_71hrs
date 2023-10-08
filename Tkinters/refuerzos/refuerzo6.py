import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

sep = os.path.sep
actual_dir = os.getcwd()
program_dir = sep.join(actual_dir.split(sep)[:-1])


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x130')
        self.resizable(0, 0)
        self.title = 'Refuerzo 6'
        self.iconbitmap(program_dir + sep + 'icono' + sep + 'icono.ico')

        # Grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Menu
        self.menu = Menu(self)
        self.sub_menu = Menu(self.menu, tearoff=False)
        self.sub_menu.add_command(label='Salir', command=self.close)
        self.menu.add_cascade(label='Archivo', menu=self.sub_menu)
        self.config(menu=self.menu)

        self._create_widgets()
        self._txtfield_value()

    def close(self):
        messagebox.showwarning('saliendo', 'Saliendo del programa')
        self.menu.quit()
        self.menu.destroy()
        sys.exit()

    # Eventos
    def _txtfield_value(self):
        user_value = self.txt_user.get()
        password_value = self.txt_password.get()
        if user_value and password_value:
            messagebox.showinfo('Ingreso', f'Usuario: {user_value}\nPassword: {password_value}')
        elif user_value or password_value:
            messagebox.showwarning('Valores incompletos',
                                   f'Falta ingresar {"el usuario" if password_value else "la contraseña"}')
        else:
            messagebox.showerror('Sin valores', 'No has ingresado ningun valor')

        self.txt_user.focus()

    def _create_widgets(self):
        # Labels
        lbl_user = ttk.Label(self, text='Usuario')
        lbl_password = ttk.Label(self, text='Contraseña')

        # TextField
        self.txt_user = ttk.Entry(self, width=30)
        self.txt_password = ttk.Entry(self, width=30, show='*')

        # Buttons
        btn_submit = ttk.Button(self, text='Enviar', command=self._txtfield_value)

        # Inclusion
        lbl_user.grid(row=0, column=0, sticky='E', padx=5)
        lbl_password.grid(row=1, column=0, sticky='E', padx=5)
        self.txt_user.grid(row=0, column=1, sticky='W')
        self.txt_password.grid(row=1, column=1, sticky='W', )
        btn_submit.grid(row=2, column=0, columnspan=2, sticky='N', pady=10)


if __name__ == '__main__':
    windowsLogin = Login()
    windowsLogin.mainloop()
