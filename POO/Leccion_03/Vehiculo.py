class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f"es de color {self._color} y tiene {self._ruedas} ruedas"

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

class Bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        super().__init__(color,ruedas)
        self._tipo = tipo

    def __str__(self):
        return f"La bicicleta de {self._tipo} {super().__str__()}"

    def __del__(self):
        print(f"La bicicleta de {self._tipo} de color {self.color} a sido eliminada")

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return f"El vehiculo va a {self._velocidad} y {super().__str__()}"

    def __del__(self):
        print(f"El vehiculo de color {self.color} a sido eliminado")

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

if __name__ == "__main__":
    # Crear objeto bicicleta e imprimirlo
    bicicleta1 = Bicicleta("Urbanisacion", "Roja", 2)
    print(bicicleta1)
    # Modificarlo e imprimirlo
    bicicleta1.tipo = "Velocidad"
    print(bicicleta1)
    # Eliminarlo
    del bicicleta1

    # Crear objeto de vehiculo e imprimirlo
    coche1 = Coche("Amarillo", 4, "24Km/h")
    print(coche1)
    # Modificar e imprimirlo
    coche1.ruedas = 6
    print(coche1)
    # Eliminarlo
    del coche1

