import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

sep = os.path.sep
actual_dir = os.getcwd()
icon_img_dir = sep.join(actual_dir.split(sep)[:-1])

class Tab(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tabulaciones')
        self.geometry('650x400+350+200')
        self.iconbitmap(icon_img_dir + sep + 'icono' + sep + 'icono.ico')
        self.resizable(0,0)

        # Widgets
        self.create_tab()
        self.create_widgets_tab()

    def create_tab(self):
        control_tab = ttk.Notebook(self)
        control_tab.pack(fill='both')

        self.tab_1 = ttk.Frame(control_tab)
        control_tab.add(self.tab_1, text='Tabulacion 1')

        self.tab_2 = ttk.Labelframe(control_tab, text='Texto con Scroll')
        control_tab.add(self.tab_2, text='Tabulacion 2')

        self.tab_3 = ttk.Frame(control_tab)
        control_tab.add(self.tab_3, text='Tabulacion 3')

        self.tab_4 = ttk.Labelframe(control_tab, text='Imagenes')
        control_tab.add(self.tab_4, text='Tabulacion 4')

        self.tab_5 = ttk.Labelframe(control_tab, text='Barra progreso')
        control_tab.add(self.tab_5, text='Tabulacion 5')


    def create_widgets_tab(self):
        def tab_01(tab):
            def saludo():
                messagebox.showinfo('Bienvenido', f'Hola {txt_name.get()}')

            lbl_name = ttk.Label(tab, text='Nombre:')
            txt_name = ttk.Entry(tab, width=30)
            btn_submit = ttk.Button(tab, text='Enviar', command=saludo)

            lbl_name.grid(row=0, column=0, sticky='E')
            txt_name.grid(row=0, column=1, padx=5, pady=5)
            btn_submit.grid(row=1, column=0, columnspan=2)

        def tab_02(tab):
            content = 'Este es un contenido'
            scroll_text = scrolledtext.ScrolledText(tab, width=50, height=22, wrap=tk.WORD)
            scroll_text.insert(tk.INSERT, content)
            scroll_text.grid(row=0, column=0)


        def tab_03(tab):
            def show_data():
                messagebox.showinfo('Datos seleccionado', f'El dato seleccionado es "{cbx_datas.get()}"')

            data = [x + 1 for x in range(10)]
            cbx_datas = ttk.Combobox(tab, values=data)
            btn_submit = ttk.Button(tab, text='Mostrar', command=show_data)


            cbx_datas.grid(row=0, column=0)
            btn_submit.grid(row=0, column=1)
            cbx_datas.current(1)

        def tab_04(tab):
            def show_info():
                messagebox.showinfo('Info de la imagen', f'{img.cget("file")}')
            img = tk.PhotoImage(file='..\\img\\python-logo.png')
            btn_img = ttk.Button(tab, image=img, command=show_info)

            btn_img.grid(row=0, column=0)
        def tab_05(tab):
            def upload():
                progress_bar['maximum'] = 100
                for progress in range(101):
                    sleep(0.05)
                    progress_bar['value'] = progress
                    progress_bar.update()
                progress_bar['value'] = 0

            def loop():
                progress_bar.start()

            def stop():
                progress_bar.stop()

            def stop_one_seg():
                ms = 1000
                progress_bar.after(ms, progress_bar.stop)

            progress_bar = ttk.Progressbar(tab, length=630, orient='horizontal')
            btn_progress_bar = ttk.Button(tab, text='Comenzar', command=upload)
            btn_loop = ttk.Button(tab, text='Ciclo', command=loop)
            btn_stop = ttk.Button(tab, text='Detener', command=stop)
            btn_stop_one_seg = ttk.Button(tab, text='Detener en un segundo', command=stop_one_seg)

            progress_bar.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
            btn_progress_bar.grid(row=1, column=0)
            btn_loop.grid(row=1, column=1)
            btn_stop.grid(row=1, column=2)
            btn_stop_one_seg.grid(row=1, column=3)

        # Llamadas
        tab_01(self.tab_1)
        tab_02(self.tab_2)
        tab_03(self.tab_3)
        tab_04(self.tab_4)
        tab_05(self.tab_5)


if __name__ == '__main__':
    windows = Tab()
    windows.mainloop()