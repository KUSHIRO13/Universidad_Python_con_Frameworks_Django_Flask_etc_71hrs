class ManejoArchivo:
    def __init__(self, archivo):
        self.archivo = archivo

    def __enter__(self):
        print(f"Se abre al archivo {self.archivo}")
        self.archivo = open(self.archivo, "r", encoding="UTF-8")
        return self.archivo
    def __exit__(self, tipo_exp, valor_exp, traza):
        print(f"Se cierra el archivo {self.archivo}")
        if self.archivo:
            self.archivo.close()
