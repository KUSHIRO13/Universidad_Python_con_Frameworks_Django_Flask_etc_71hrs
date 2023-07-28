from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.__idComputador = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        s = "/".center(29, "/")
        return f"\n{s}\nComputadora {self._nombre} Id: {self.__idComputador}" \
               f"\n{self._monitor.__str__()}\n{self._teclado.__str__()}\n{self._raton.__str__()}"

    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self._raton

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


if __name__ == "__main__":
    monitor1 = Monitor("Acer", "12 pulgadas")
    teclado1 = Teclado("Integrado", "Acer")
    raton1 = Raton("USB", "Havit")
    computadora1 = Computadora("Acer", monitor1, teclado1, raton1)
    print(computadora1)
    computadora1.nombre = "Hp"
    print(computadora1)

    monitor2 = Monitor("Toshiba", "14 pulgadas")
    teclado2 = Teclado("Integrado", "Toshiba")
    raton2 = Raton("USB", "WIT")
    computadora2 = Computadora("Toshiba", monitor2, teclado2, raton2)
    print(computadora2)
