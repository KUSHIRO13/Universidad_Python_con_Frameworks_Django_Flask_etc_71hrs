class Orden:
    contador_ordenes = 0
    def __init__(self, computadora):
        Orden.contador_ordenes += 1
        self.idOrden = Orden.contador_ordenes
        self._computadora = list(computadora)

    def agregar_computadora(self, computadora):
        return self._computadora.append(computadora)

    def __str__(self):
        orden_str = ""
        s = "-".center(29,"-")
        for o_str in self._computadora:
            orden_str += o_str.__str__()
        return f"{s}\nOrden: {self.idOrden}{orden_str}"