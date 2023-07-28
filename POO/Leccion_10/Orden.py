class Orden:
    contador_ordenes = 0
    def __init__(self, computadora):
        Orden.contador_ordenes += 1
        self._computadora = list(computadora)

    def agregar_computadora(self, computadora):
        return self._computadora.append(computadora)