import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from time import sleep

class Tab(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Refuero 8')
        self.geometry('600x600+400+90')

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

            img = tk.PhotoImage(file='img\\python-logo.png')
            btn_image = ttk.Button(tab, image=img, command=mostrar_titulo)
            btn_image.grid(row=0,column=0)
            lbl_image = ttk.Label(tab, image=img)
            lbl_image.grid(row=1, column=0)

        def tab_05(tab):
            def ejecutar_barra():
                progress_bar['maximum'] = 100
                for valor in range(101):
                    sleep(0.05)
                    progress_bar['value'] = valor
                    # Actualizar barra
                    progress_bar.update()
                progress_bar['value'] = 0

            def ejecutar_ciclo():
                progress_bar.start()

            def detener_ciclo():
                progress_bar.stop()

            def detener_ciclo_despues():
                esperar_ms = 1000
                self.after(esperar_ms, progress_bar.stop)

            # Crear componente
            progress_bar = ttk.Progressbar(tab, orient='horizontal', length=550)
            progress_bar.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
            # Botones controladores
            btn_inicio = ttk.Button(tab, text='Ejecutar barra', command=ejecutar_barra)
            btn_inicio.grid(row=1, column=0)

            btn_ciclo = ttk.Button(tab, text='Ejecutar ciclo', command=ejecutar_ciclo)
            btn_ciclo.grid(row=1, column=1)

            btn_detener = ttk.Button(tab, text='Detener ciclo', command=detener_ciclo)
            btn_detener.grid(row=1, column=2)

            btn_detener_despues = ttk.Button(tab, text='Detener ciclo despues', command=detener_ciclo_despues)
            btn_detener_despues.grid(row=1, column=3)

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

        tab5 = ttk.Labelframe(control_tab, text='barra progreso')
        control_tab.add(tab5, text='tabulador 5')
        tab_05(tab5)

if __name__ == '__main__':
    tab = Tab()
    tab.mainloop()