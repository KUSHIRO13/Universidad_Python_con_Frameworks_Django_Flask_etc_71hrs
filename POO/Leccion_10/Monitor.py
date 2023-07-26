class Monitor:
    contador_monitor = 0
    def __init__(self, marca, tamano):
        Monitor.contador_monitor += 1
        self.idMonitor = Monitor.contador_monitor
        self._marca = marca
        self._tamano = tamano

    def __str__(self):
        monitor = " Monitor ".center(29,"=")
        return f"{monitor}\nId: {self.idMonitor}\nMarca: {self._marca}\nTamaño: {self._tamano}"

    # Creaccion del Get
    @property
    def marca(self):
        return self._marca
    @property
    def tamano(self):
        return self._tamano

    # Creacion del Set
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

if __name__ == "__main__":
    monito1 = Monitor("Acer", "27 pulgadas")
    print(monito1)
    monito2 = Monitor("Hp", "30 pulgadas")
    print(monito2)