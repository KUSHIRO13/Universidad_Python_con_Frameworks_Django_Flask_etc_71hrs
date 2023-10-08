import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class Tab(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Refuero 8')
        self.geometry('600x600')

        self._create_tab()

    def _create_tab(self):
        control_tab = ttk.Notebook(self)
        def tab_01(tab):
            lbl_content = ttk.Label(tab, text='Contenido')

            lbl_content.grid(row=0, column=0)

        def tab_02(tab):
            content = 'Borrar'
            line_output = scrolledtext.ScrolledText(tab, width=10, height=20, wrap=tk.WORD)
            line_output.insert(tk.INSERT, content)
            line_output.grid(row=0,column=0)


        def tab_03(tab):
            def mostrar_valor():
                messagebox.showinfo('valor', f'{combobox.get()}')
            datas = [x + 1 for x in range(10)]
            combobox = ttk.Combobox(tab, width=15, values=datas)
            combobox.grid(row=0, column=0, padx=10, pady=10)

            # Seleccionar elemento por defecto por indice
            combobox.current(5)
            # boton para saber que opcion se escogio
            button1 = ttk.Button(tab, text='Mostrar', command=mostrar_valor)
            button1.grid(row=0, column=1)

        def tab_04(tab):
            def mostrar_titulo():
                messagebox.showinfo('titulo', f'Imagen: {img.cget("file")}')

            img = tk.PhotoImage(file='python-logo.png')
            btn_image = ttk.Button(tab, image=img, command=mostrar_titulo)
            btn_image.grid(row=0,column=0)
            lbl_image = ttk.Label(tab, image=img)
            lbl_image.grid(row=1, column=0)

        tab_1 = ttk.Frame(control_tab)
        control_tab.add(tab_1, text='Tabulacion 1')
        control_tab.pack(fill='both')
        tab_01(tab_1)

        tab_2 = ttk.Labelframe(control_tab, text='Tab 2')
        control_tab.add(tab_2, text='Tabulacion 2')
        control_tab.pack(fill='both')
        tab_02(tab_2)

        tab3 = ttk.Frame(control_tab)
        control_tab.add(tab3, text='tabulador 3')
        control_tab.pack(fill='both')
        tab_03(tab3)

        tab4 = ttk.Labelframe(control_tab)
        control_tab.add(tab4, text='Tabulador 4')
        tab_04(tab4)

if __name__ == '__main__':
    tab = Tab()
    tab.mainloop()